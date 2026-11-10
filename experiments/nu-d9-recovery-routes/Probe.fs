namespace NuD9RecoveryRoutes

// D9 direction 1: getting back to work after a game-code fault in Gaia, on Nu master 47ef39e (Vulkan).
// Routes: H = automatic rewind to the Advance snapshot; F = F7 restore point at clock 20, then automatic rewind;
// C1/C2 = screen checkpoint file at clock 20 in an imperative session that the fault ends, then a fresh process
// that imports the file. Observations only; check.py applies the pass conditions.
// Protocol: docs/nu-d9-recovery-routes-2026-11-10.md. Serializers copied from experiments/nu-vulkan-r06-recovery-cost.

open System
open System.Diagnostics
open System.IO
open System.Numerics
open System.Text.Json
open System.Text.Json.Nodes
open System.Collections.Generic
open Prime
open Nu
open Nu.Gaia
open Breakout

module Program =
    let fields (pairs : (string * obj) list) = Dictionary<string, obj> (dict pairs)
    let json value = JsonSerializer.Serialize value
    let bits (value : single) = (BitConverter.SingleToInt32Bits value).ToString "X8"
    let vector (value : Vector3) = [| bits value.X; bits value.Y; bits value.Z |]
    let colorBits (value : Color) = [| bits value.R; bits value.G; bits value.B; bits value.A |]
    let modelData (g : Gameplay) =
        fields
            [ "time", box g.GameplayTime; "state", box (string g.GameplayState)
              "paddlePosition", box (vector g.Paddle.Position); "paddleSize", box (vector g.Paddle.Size)
              "ballPosition", box (vector g.Ball.Position); "ballSize", box (vector g.Ball.Size)
              "ballSpeed", box (bits g.Ball.Speed); "ballDirection", box (vector g.Ball.Direction)
              "bricks", box [| for KeyValue (name, brick) in g.Bricks ->
                                  fields ["name", box name; "position", box (vector brick.Position)
                                          "size", box (vector brick.Size); "color", box (colorBits brick.Color)] |]
              "score", box g.Score; "lives", box g.Lives ]

    let scene = Simulants.GameplayScene
    let projection (world : World) =
        let g = Simulants.Gameplay.GetGameplay world
        let sprite name =
            let entity = scene / name
            if entity.GetExists world then
                fields ["name", box name; "exists", box true
                        "position", box (vector (entity.GetPosition world))
                        "size", box (vector (entity.GetSize world))
                        "color", box (colorBits (entity.GetColor world))]
            else fields ["name", box name; "exists", box false]
        fields
            [ "names", box (World.getEntities scene world |> Seq.map (fun entity -> entity.Name) |> Seq.sort |> Seq.toArray)
              "paddle", box (sprite "Paddle"); "ball", box (sprite "Ball")
              "bricks", box (g.Bricks |> Map.toArray |> Array.map (fun (name, _) -> sprite name))
              "scoreText", box ((scene / "Score").GetText world)
              "messageText", box ((scene / "Message").GetText world) ]

    let projectionErrors (g : Gameplay) (world : World) =
        let failures = ResizeArray<string> ()
        let check label passed = if not passed then failures.Add label
        let checkSprite name position size =
            let entity = scene / name
            check (name + ":exists") (entity.GetExists world)
            if entity.GetExists world then
                check (name + ":position") (vector (entity.GetPosition world) = vector position)
                check (name + ":size") (vector (entity.GetSize world) = vector size)
        checkSprite "Paddle" g.Paddle.Position g.Paddle.Size
        checkSprite "Ball" g.Ball.Position g.Ball.Size
        for KeyValue (name, brick) in g.Bricks do
            checkSprite name brick.Position brick.Size
            if (scene / name).GetExists world then
                check (name + ":color") (colorBits ((scene / name).GetColor world) = colorBits brick.Color)
        check "score" ((scene / "Score").GetText world = "Score: " + string g.Score)
        let expectedMessage = if g.Lives <= 0 then "Game over!" elif g.Bricks.Count = 0 then "You win!" else ""
        check "message" ((scene / "Message").GetText world = expectedMessage)
        let actualLives = World.getEntities scene world |> Seq.map (fun entity -> entity.Name) |> Seq.filter (fun name -> name.StartsWith "Life+") |> Set.ofSeq
        check "life-icons" (actualLives = Set.ofList [for i in 0 .. g.Lives - 1 -> "Life+" + string i])
        failures.ToArray ()


    let sameTree (a : JsonNode) (b : JsonNode) = JsonNode.DeepEquals (a, b)
    let toNode value = JsonNode.Parse (json value)

    let utcMs () = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds ()
    let tickMs (t0 : int64) (t1 : int64) = float (t1 - t0) * 1000.0 / float Stopwatch.Frequency
    let CheckpointClock = 20L
    let FaultClock = 30L
    let ContinuationUpdates = 5

    [<EntryPoint; STAThread>]
    let main args =
        if args.Length <> 4 || not (List.contains args[0] ["H"; "F"; "C1"; "C2"]) then
            eprintfn "Usage: Probe <H|F|C1|C2> <Breakout DLL> <transfer dir> <new receipt dir>"
            2
        else
            let route, dll, transfer, output = args[0], Path.GetFullPath args[1], Path.GetFullPath args[2], Path.GetFullPath args[3]
            let imperative = route = "C1" || route = "C2"
            if Directory.Exists output then invalidOp "Receipt directory must be new."
            Directory.CreateDirectory output |> ignore
            Directory.CreateDirectory transfer |> ignore
            let checkpointFile = Path.Combine (transfer, "checkpoint.nuscreen")
            let trace = Path.Combine (output, "trace.jsonl")
            let emit label (values : (string * obj) list) =
                File.AppendAllText (trace, json (fields (("event", box label) :: ("utcMs", box (utcMs ())) :: values)) + Environment.NewLine)
            let mutable callbacks, updates, timeAdvances = 0, 0, 0
            let mutable phase = "initialize"
            let mutable done_, complete = false, false
            let mutable maxPasts = 0
            let mutable s0Model, s0Projection = "", (null : JsonNode)
            let mutable expectedModel, expectedProjection = "", (null : JsonNode)
            let mutable recoveredClock = -1L
            let mutable continuationStart = 0
            let mutable lastHookUtc, lastHookTick = 0L, 0L
            let modelsByClock = Dictionary<int64, string> ()
            let mutable settle = 0
            let require m c = if not c then invalidOp m
            let finish ok detail (world : World) =
                complete <- ok
                done_ <- true
                emit "result" ["complete", box ok; "detail", box detail; "phase", box phase; "route", box route]
                if world.TimeAdvancing then World.setTimeAdvancing false world
                World.exit world
            let snap (world : World) =
                let g = Simulants.Gameplay.GetGameplay world
                [ "callbacks", box callbacks; "updates", box updates; "timeAdvances", box timeAdvances
                  "advancing", box world.TimeAdvancing; "imperative", box world.Imperative
                  "pasts", box (Gaia.researchPastsCount ()); "futures", box (Gaia.researchFuturesCount ())
                  "pastsHead", box (Gaia.researchPastsHeadKind ()); "messageBox", box (Option.toObj (Gaia.researchMessageBox ()))
                  "gameplayTime", box g.GameplayTime; "model", box (modelData g) ]
            let callback (world : World) =
                let entryTick = Stopwatch.GetTimestamp ()
                let entryUtc = utcMs ()
                if not done_ then
                    try
                        callbacks <- callbacks + 1
                        require "callback watchdog (1200)" (callbacks <= 1200)
                        require "wrong mode" (world.Imperative = imperative && world.Accompanied)
                        let g = Simulants.Gameplay.GetGameplay world
                        let pasts = Gaia.researchPastsCount ()
                        match phase with
                        | "initialize" ->
                            require "initial world advancing" world.TimeHalted
                            require "Gameplay not selected/idling" (World.getSelectedScreen world = Simulants.Gameplay && World.getSelectedScreenIdling world)
                            require "initial Gameplay contract" (g.Score = 0 && g.Bricks.Count = 30 && g.GameplayState = Playing && g.GameplayTime = 0L)
                            World.subscribe (fun _ w ->
                                updates <- updates + 1
                                if phase = "continue" && updates - continuationStart = ContinuationUpdates then World.setTimeAdvancing false w
                                Cascade) Simulants.Gameplay.UpdateEvent Game world |> ignore
                            World.subscribe (fun _ _ -> timeAdvances <- timeAdvances + 1; Cascade) Simulants.Gameplay.TimeAdvanceEvent Game world |> ignore
                            s0Model <- json (modelData g)
                            s0Projection <- toNode (projection world)
                            emit "settled-S0" (snap world @ ["projection", box (projection world)])
                            if route = "C2" then
                                let groupsBefore = World.getGroups Simulants.Gameplay world |> Seq.map (fun gr -> gr.Name) |> Seq.toArray
                                let t0 = Stopwatch.GetTimestamp ()
                                World.destroyGroupsImmediate (World.getGroups Simulants.Gameplay world) world
                                let screen = World.readScreenFromFile checkpointFile None world
                                World.notifyScreenModelChange screen world
                                let t1 = Stopwatch.GetTimestamp ()
                                require "imported wrong screen" (screen = Simulants.Gameplay)
                                expectedModel <- File.ReadAllText (Path.Combine (transfer, "checkpoint-model.json"))
                                expectedProjection <- JsonNode.Parse (File.ReadAllText (Path.Combine (transfer, "checkpoint-projection.json")))
                                for KeyValue (k, v) in JsonSerializer.Deserialize<Dictionary<string, string>> (File.ReadAllText (Path.Combine (transfer, "models-by-clock.json"))) do
                                    modelsByClock[int64 k] <- v
                                emit "import" ["importMs", box (tickMs t0 t1); "destroyedGroups", box groupsBefore]
                                phase <- "settle"
                            else
                                Gaia.researchToggleAdvancing world
                                maxPasts <- Gaia.researchPastsCount ()
                                emit "advance" (snap world)
                                require "Advance did not push a snapshot" (Gaia.researchPastsHeadKind () = "Advance")
                                expectedModel <- s0Model
                                expectedProjection <- s0Projection
                                phase <- "run"
                        | "run" ->
                            if pasts > maxPasts then maxPasts <- pasts
                            if pasts < maxPasts then
                                // the outer handler rewound (H, F): first hook after recovery
                                emit "recovery-immediate"
                                    (snap world @ [ "gapFromLastHookMs", box (tickMs lastHookTick entryTick)
                                                    "gapFromLastHookUtcMs", box (entryUtc - lastHookUtc)
                                                    "lastHookClock", box (Seq.max modelsByClock.Keys) ])
                                phase <- "settle"
                                settle <- 0
                            elif world.TimeAdvancing then
                                modelsByClock[g.GameplayTime] <- json (modelData g)
                                lastHookTick <- entryTick
                                lastHookUtc <- entryUtc
                                if g.GameplayTime = CheckpointClock && route = "F" then
                                    let t0 = Stopwatch.GetTimestamp ()
                                    Gaia.researchCreateRestorePoint world
                                    let t1 = Stopwatch.GetTimestamp ()
                                    expectedModel <- json (modelData (Simulants.Gameplay.GetGameplay world))
                                    expectedProjection <- toNode (projection world)
                                    maxPasts <- Gaia.researchPastsCount ()
                                    emit "checkpoint" (snap world @ ["kind", box "F7 restore point"; "checkpointMs", box (tickMs t0 t1)])
                                elif g.GameplayTime = CheckpointClock && route = "C1" then
                                    let t0 = Stopwatch.GetTimestamp ()
                                    World.writeScreenToFile checkpointFile Simulants.Gameplay world
                                    let t1 = Stopwatch.GetTimestamp ()
                                    File.WriteAllText (Path.Combine (transfer, "checkpoint-model.json"), json (modelData g))
                                    File.WriteAllText (Path.Combine (transfer, "checkpoint-projection.json"), json (projection world))
                                    emit "checkpoint" (snap world @ ["kind", box "screen file"; "checkpointMs", box (tickMs t0 t1); "fileBytes", box (FileInfo(checkpointFile).Length)])
                                require "fault not reached by clock 60 (invalid)" (g.GameplayTime <= 60L)
                        | "settle" ->
                            require "advancing during settle" world.TimeHalted
                            settle <- settle + 1
                            if settle = 1 then
                                recoveredClock <- g.GameplayTime
                                emit "recovered-first-hook"
                                    (snap world @ [ "modelEqualsExpected", box (json (modelData g) = expectedModel)
                                                    "projectionEqualsExpected", box (sameTree (toNode (projection world)) expectedProjection) ])
                            if settle >= 10 then
                                emit "recovered-settled"
                                    (snap world @ [ "modelEqualsExpected", box (json (modelData g) = expectedModel)
                                                    "projectionEqualsExpected", box (sameTree (toNode (projection world)) expectedProjection)
                                                    "projectionErrors", box (projectionErrors g world) ])
                                continuationStart <- updates
                                Gaia.researchToggleAdvancing world
                                phase <- "continue"
                        | "continue" when world.TimeHalted && updates - continuationStart >= ContinuationUpdates ->
                            let reference = match modelsByClock.TryGetValue g.GameplayTime with | (true, m) -> m | _ -> ""
                            emit "continuation"
                                (snap world @ [ "recoveredClock", box recoveredClock
                                                "continuationUpdates", box (updates - continuationStart)
                                                "referenceFound", box (reference <> "")
                                                "modelEqualsOriginalRunAtSameClock", box (reference <> "" && json (modelData g) = reference) ])
                            finish true "Recovered, settled and continued." world
                        | _ -> ()
                    with ex ->
                        emit "probe-exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace; "phase", box phase]
                        finish false ex.Message world
            try
                Directory.SetCurrentDirectory AppContext.BaseDirectory
                let state = { GaiaState.defaultState with ProjectDllPath = dll; ProjectEditModeOpt = Some "Gameplay"; ProjectFreshlyLoaded = true; ProjectImperativeExecution = imperative }
                let (actualState, targetDir, plugin) = Nu.initPlus (fun () ->
                    File.WriteAllText (Path.Combine (AppContext.BaseDirectory, Constants.Gaia.StateFilePath), scstring state)
                    Gaia.selectNuPlugin (GaiaPlugin ()))
                Constants.GameTime.DesiredFrameRate <- StaticFrameRate 60L
                emit "configuration" ["route", box route; "imperative", box actualState.ProjectImperativeExecution; "nuAssembly", box typeof<World>.Assembly.FullName]
                require "wrong plugin" (plugin.GetType().FullName = typeof<BreakoutPlugin>.FullName)
                Gaia.setResearchPostProcess callback
                let exitCode = Gaia.run actualState targetDir plugin
                if route = "C1" then
                    let d = Dictionary<string, string> ()
                    for KeyValue (k, v) in modelsByClock do d[string k] <- v
                    File.WriteAllText (Path.Combine (transfer, "models-by-clock.json"), JsonSerializer.Serialize d)
                emit "engine-exit" ["exitCode", box exitCode; "probeFinished", box done_; "complete", box complete
                                    "lastHookClock", box (if modelsByClock.Count > 0 then Seq.max modelsByClock.Keys else -1L); "lastHookUtcMs", box lastHookUtc]
                exitCode
            with ex ->
                emit "launch-exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace]
                3
