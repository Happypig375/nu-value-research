namespace NuVulkanRecoveryCostResearch

// R06 one-checkpoint recovery component costs, ported to Nu master 47ef39e (Vulkan) for the reference re-run.
// Source: experiments/nu-r06-recovery-cost/RecoveryCost.fs and the B0 helpers in experiments/nu-history-b0/Probe.fs.
// Port changes (declared in docs/nu-vulkan-timing-reference-2026-11-03.md, part 1):
//   - master names: TimeAdvancing / TimeHalted / setTimeAdvancing, TimeAdvanceEvent (was TimeUpdateEvent);
//   - master's Breakout scene no longer has the rotating StaticModel cube or the Light3d entity, so the projection
//     has no cube rotation, and the recorded B0 projection is compared with those two names and the rotation removed;
//   - projections are compared as JSON trees (JsonNode.DeepEquals) instead of exact strings.
// Everything else (seed, content clear, 10-step drift, routes, timers, readiness boundary, oracle) is unchanged.

open System
open System.Diagnostics
open System.IO
open System.Numerics
open System.Text
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

    /// The recorded 064f7ae B0 projection, adapted to master's scene: drop the cube rotation and the two removed names.
    let adaptRecordedProjection (text : string) =
        let node = JsonNode.Parse text :?> JsonObject
        node.Remove "rotation" |> ignore
        let names = node["names"] :?> JsonArray
        let kept = [| for n in names do
                        let s = n.GetValue<string> ()
                        if s <> "StaticModel" && s <> "Light3d" then yield s |]
        node["names"] <- JsonArray ([| for s in kept -> JsonValue.Create s :> JsonNode |])
        node :> JsonNode

    let sameTree (a : JsonNode) (b : JsonNode) = JsonNode.DeepEquals (a, b)
    let toNode value = JsonNode.Parse (json value)

    let require message condition = if not condition then invalidOp message

    let expectedAt (target : Gameplay) step =
        // The same bounded source prediction accepted for R03 B1 (unchanged Gameplay.update on master).
        let mutable x = target.Ball.Position.X
        let mutable y = target.Ball.Position.Y
        for index in 1 .. step do
            let directionX = if index <= 5 then target.Ball.Direction.X else -target.Ball.Direction.X
            x <- x + target.Ball.Speed * directionX
            y <- y + target.Ball.Speed * target.Ball.Direction.Y
        let direction =
            if step >= 5 then Vector3 (-target.Ball.Direction.X, target.Ball.Direction.Y, target.Ball.Direction.Z)
            else target.Ball.Direction
        { target with
            GameplayTime = target.GameplayTime + int64 step
            Ball = { target.Ball with Position = Vector3 (x, y, target.Ball.Position.Z); Direction = direction } }

    let projectionForModel names paddleColor ballColor (g : Gameplay) =
        let sprite name position size color =
            fields
                [ "name", box name; "exists", box true
                  "position", box (vector position); "size", box (vector size)
                  "color", box (colorBits color) ]
        fields
            [ "names", box names
              "paddle", box (sprite "Paddle" g.Paddle.Position g.Paddle.Size paddleColor)
              "ball", box (sprite "Ball" g.Ball.Position g.Ball.Size ballColor)
              "bricks", box [| for KeyValue (name, brick) in g.Bricks ->
                                   sprite name brick.Position brick.Size brick.Color |]
              "scoreText", box ("Score: " + string g.Score)
              "messageText", box (if g.Lives <= 0 then "Game over!" elif g.Bricks.Count = 0 then "You win!" else "") ]

    [<EntryPoint; STAThread>]
    let main args =
        if args.Length <> 6 || not (List.contains args[0] ["H"; "R"]) ||
           not (List.contains args[1] ["feasibility"; "measured"]) then
            eprintfn "Usage: RecoveryCost <H|R> <feasibility|measured> <attempt-id> <Breakout DLL> <checkpoint directory> <new receipt directory>"
            2
        else
            let route, attemptKind, attemptId = args[0], args[1], args[2]
            let dll, checkpoint, output = Path.GetFullPath args[3], Path.GetFullPath args[4], Path.GetFullPath args[5]
            require "Receipt directory must be new" (not (Directory.Exists output))
            Directory.CreateDirectory output |> ignore
            let tracePath = Path.Combine (output, "trace.jsonl")
            let proc = Process.GetCurrentProcess ()
            let frequency = Stopwatch.Frequency
            let probeStartTick = Stopwatch.GetTimestamp ()
            let mutable traceWorkTicks = 0L
            let emit label values =
                let start = Stopwatch.GetTimestamp ()
                let record = fields (("event", box label) :: values)
                File.AppendAllText (tracePath, json record + Environment.NewLine)
                traceWorkTicks <- traceWorkTicks + Stopwatch.GetTimestamp () - start
            let sample label =
                proc.Refresh ()
                fields
                    [ "label", box label; "timestamp", box (Stopwatch.GetTimestamp ())
                      "allocatedBytesApproximate", box (GC.GetTotalAllocatedBytes false)
                      "gen0Collections", box (GC.CollectionCount 0)
                      "gen1Collections", box (GC.CollectionCount 1)
                      "gen2Collections", box (GC.CollectionCount 2)
                      "managedHeapBytesSecondary", box (GC.GetTotalMemory false)
                      "workingSetBytesSecondary", box proc.WorkingSet64
                      "privateBytesSecondary", box proc.PrivateMemorySize64 ]
            let samples = ResizeArray<Dictionary<string, obj>> ()
            let storeSample label = samples.Add (sample label)
            let mutable updates, timeUpdates, callbacks = 0, 0, 0
            let mutable leftInputs, rightInputs = 0, 0
            let mutable phase = "initialize"
            let mutable driftStartUpdates, driftStartTimeUpdates = 0, 0
            let mutable recoveryCounts = (0, 0)
            let order = ResizeArray<string> ()
            let updateDeltas = ResizeArray<int64> ()
            let timeUpdateDeltas = ResizeArray<int64> ()
            let mutable targetModelOracle = ""
            let mutable targetProjectionOracle : JsonNode = null
            let mutable driftModelOracle = ""
            let mutable driftProjectionOracle : JsonNode = null
            let mutable clearedModelOracle = ""
            let mutable clearRequestCallback = 0
            let mutable recoveryPayloadOpt : string option = None
            let mutable acquisitionStart, acquisitionStop = 0L, 0L
            let mutable recoveryStart, recoveryDirectStop, readinessStop = 0L, 0L, 0L
            let mutable oracleWorkStart, oracleWorkStop = 0L, 0L
            let mutable clockPair1Start, clockPair1Stop, clockPair2Start, clockPair2Stop = 0L, 0L, 0L, 0L
            let mutable passed, done_ = false, false
            let safeCapture name (capture : unit -> obj) =
                try [name, capture ()]
                with error ->
                    [ name + "CaptureErrorType", box (error.GetType().FullName)
                      name + "CaptureErrorMessage", box error.Message ]
            let observe label (world : World) =
                let g = Simulants.Gameplay.GetGameplay world
                emit label
                    [ "phase", box phase; "updates", box updates; "timeUpdates", box timeUpdates
                      "callbacks", box callbacks; "functional", box (not world.Imperative)
                      "accompanied", box world.Accompanied; "advancing", box world.TimeAdvancing
                      "selectedGameplay", box (World.getSelectedScreen world = Simulants.Gameplay)
                      "selectedIdling", box (World.getSelectedScreenIdling world)
                      "model", box (modelData g); "projection", box (projection world)
                      "projectionErrors", box (projectionErrors g world) ]
            let observeFailure (world : World) =
                let captures =
                    safeCapture "functional" (fun () -> box (not world.Imperative)) @
                    safeCapture "accompanied" (fun () -> box world.Accompanied) @
                    safeCapture "advancing" (fun () -> box world.TimeAdvancing) @
                    safeCapture "halted" (fun () -> box world.TimeHalted) @
                    safeCapture "selectedGameplay" (fun () -> box (World.getSelectedScreen world = Simulants.Gameplay)) @
                    safeCapture "selectedIdling" (fun () -> box (World.getSelectedScreenIdling world)) @
                    safeCapture "model" (fun () -> box (modelData (Simulants.Gameplay.GetGameplay world))) @
                    safeCapture "projection" (fun () -> box (projection world)) @
                    safeCapture "projectionErrors" (fun () ->
                        let g = Simulants.Gameplay.GetGameplay world
                        box (projectionErrors g world))
                emit "failure-state"
                    ([ "phase", box phase; "updates", box updates; "timeUpdates", box timeUpdates
                       "callbacks", box callbacks; "leftInputUpdates", box leftInputs
                       "rightInputUpdates", box rightInputs ] @ captures)
            let finish success detail (world : World) =
                passed <- success
                done_ <- true
                emit "result"
                    [ "pass", box success; "detail", box detail; "phase", box phase
                      "route", box route; "attemptKind", box attemptKind; "attemptId", box attemptId
                      "updates", box updates; "timeUpdates", box timeUpdates; "callbacks", box callbacks
                      "leftInputUpdates", box leftInputs; "rightInputUpdates", box rightInputs
                      "stopwatchFrequency", box frequency
                      "acquisitionTicks", box (if acquisitionStop > 0L then acquisitionStop - acquisitionStart else -1L)
                      "recoveryDirectTicks", box (if recoveryDirectStop > 0L then recoveryDirectStop - recoveryStart else -1L)
                      "requestToReadyTicks", box (if readinessStop > 0L then readinessStop - recoveryStart else -1L)
                      "oracleWorkTicks", box (if oracleWorkStop > 0L then oracleWorkStop - oracleWorkStart else -1L)
                      "traceWorkTicksBeforeResult", box traceWorkTicks
                      "clockPairs", box [|
                          fields ["ticks", box (clockPair1Stop - clockPair1Start)]
                          fields ["ticks", box (clockPair2Stop - clockPair2Start)] |]
                      "gcAndMemorySamples", box (samples.ToArray ()) ]
                World.setTimeAdvancing false world
                World.exit world
            let beginDrift (world : World) =
                driftStartUpdates <- updates
                driftStartTimeUpdates <- timeUpdates
                order.Clear ()
                updateDeltas.Clear ()
                timeUpdateDeltas.Clear ()
                phase <- "drift"
                World.setTimeAdvancing true world
            let callback (world : World) =
                let callbackEntry = Stopwatch.GetTimestamp ()
                // The unconditional timestamp capture above is deliberately the first callback operation.
                if phase = "await-ready" && readinessStop = 0L then
                    readinessStop <- callbackEntry
                if not done_ then
                    try
                        callbacks <- callbacks + 1
                        require "callback watchdog" (callbacks <= 1200)
                        require "wrong execution mode" (not world.Imperative && world.Accompanied)
                        require "wrong static clock" (Constants.GameTime.DesiredFrameRate = StaticFrameRate 60L)
                        require "screen selection changed"
                            (World.getSelectedScreen world = Simulants.Gameplay && World.getSelectedScreenIdling world)
                        let g = Simulants.Gameplay.GetGameplay world
                        match phase with
                        | "initialize" ->
                            require "initial world not halted" world.TimeHalted
                            require "initial gameplay contract"
                                (g.GameplayState = Playing && g.Score = 0 && g.Bricks.Count = 30)
                            World.subscribe (fun _ w ->
                                updates <- updates + 1
                                if World.isKeyboardKeyDown KeyboardKey.Left w then leftInputs <- leftInputs + 1
                                if World.isKeyboardKeyDown KeyboardKey.Right w then rightInputs <- rightInputs + 1
                                if phase = "drift" then
                                    order.Add "Update"
                                    updateDeltas.Add w.GameDelta.Updates
                                    if updates - driftStartUpdates = 10 then World.setTimeAdvancing false w
                                Cascade) Simulants.Gameplay.UpdateEvent Game world |> ignore
                            World.subscribe (fun _ w ->
                                timeUpdates <- timeUpdates + 1
                                if phase = "drift" then
                                    order.Add "TimeAdvance"
                                    timeUpdateDeltas.Add w.GameDelta.Updates
                                Cascade) Simulants.Gameplay.TimeAdvanceEvent Game world |> ignore
                            observe "fresh-initial" world
                            let target = scvalue<Gameplay> (File.ReadAllText (Path.Combine (checkpoint, "gameplay.symbol")))
                            require "fixed target summary differs"
                                (target.GameplayTime = 149L && target.Score = 100 && target.Bricks.Count = 29 && target.Lives = 5)
                            targetModelOracle <- json (modelData target)
                            targetProjectionOracle <- adaptRecordedProjection (File.ReadAllText (Path.Combine (checkpoint, "projection.json")))
                            require "initial negative control failed" (json (modelData g) <> targetModelOracle)
                            let cleared = { g with GameplayState = Quit }
                            clearedModelOracle <- json (modelData cleared)
                            clearRequestCallback <- callbacks
                            phase <- "await-content-clear"
                            Simulants.Gameplay.SetGameplay cleared world
                        | "await-content-clear" ->
                            require "content clear callback boundary differs" (callbacks = clearRequestCallback + 1)
                            require "content clear advanced" (updates = 0 && timeUpdates = 0 && world.TimeHalted)
                            require "Gameplay scene survived content clear" (not (scene.GetExists world))
                            require "content clear model mismatch" (json (modelData g) = clearedModelOracle)
                            emit "content-cleared"
                                [ "phase", box phase; "callbacks", box callbacks; "clearRequestCallback", box clearRequestCallback
                                  "sceneExists", box (scene.GetExists world); "model", box (modelData g) ]
                            let target = scvalue<Gameplay> (File.ReadAllText (Path.Combine (checkpoint, "gameplay.symbol")))
                            require "reloaded fixed target differs" (json (modelData target) = targetModelOracle)
                            Simulants.Gameplay.SetGameplay target world
                            phase <- "seed-ready"
                        | "seed-ready" ->
                            require "seed callback boundary differs" (callbacks = clearRequestCallback + 2)
                            require "seed reconstruction advanced" (updates = 0 && timeUpdates = 0 && world.TimeHalted)
                            require "seed model mismatch" (json (modelData g) = targetModelOracle)
                            require "seed projection mismatch" (sameTree (toNode (projection world)) targetProjectionOracle)
                            require "seed projection values mismatch" ((projectionErrors g world).Length = 0)
                            let names =
                                World.getEntities scene world
                                |> Seq.map (fun entity -> entity.Name)
                                |> Seq.sort
                                |> Seq.toArray
                            let paddleColor = (scene / "Paddle").GetColor world
                            let ballColor = (scene / "Ball").GetColor world
                            let driftExpected = expectedAt g 10
                            driftModelOracle <- json (modelData driftExpected)
                            driftProjectionOracle <- toNode (projectionForModel names paddleColor ballColor driftExpected)
                            observe "seeded-B0" world
                            clockPair1Start <- Stopwatch.GetTimestamp ()
                            clockPair1Stop <- Stopwatch.GetTimestamp ()
                            clockPair2Start <- Stopwatch.GetTimestamp ()
                            clockPair2Stop <- Stopwatch.GetTimestamp ()
                            storeSample "pre-acquisition"
                            acquisitionStart <- Stopwatch.GetTimestamp ()
                            if route = "H" then Gaia.researchSnapshot world
                            else recoveryPayloadOpt <- Some (scstring (Simulants.Gameplay.GetGameplay world))
                            acquisitionStop <- Stopwatch.GetTimestamp ()
                            storeSample "post-acquisition"
                            emit "acquisition"
                                [ "route", box route; "ticks", box (acquisitionStop - acquisitionStart)
                                  "payloadUtf8Bytes", box (match recoveryPayloadOpt with Some payload -> Encoding.UTF8.GetByteCount payload | None -> 0) ]
                            beginDrift world
                        | "drift" when updates - driftStartUpdates >= 10 && world.TimeHalted ->
                            require "drift Update count differs" (updates - driftStartUpdates = 10)
                            require "drift TimeAdvance count differs" (timeUpdates - driftStartTimeUpdates = 10)
                            let actualOrder = order.ToArray ()
                            emit "drift-schedule"
                                [ "order", box actualOrder; "updateDeltas", box (updateDeltas.ToArray ())
                                  "timeUpdateDeltas", box (timeUpdateDeltas.ToArray ()) ]
                            let expectedOrder = [| for _ in 1 .. 10 do yield "TimeAdvance"; yield "Update" |]
                            require "drift event order differs" (actualOrder = expectedOrder)
                            require "Update GameDelta.Updates differs" (updateDeltas.Count = 10 && updateDeltas |> Seq.forall ((=) 1L))
                            require "TimeAdvance GameDelta.Updates differs" (timeUpdateDeltas.Count = 10 && timeUpdateDeltas |> Seq.forall ((=) 1L))
                            require "host input observed" (leftInputs = 0 && rightInputs = 0)
                            require "complete drift model differs" (json (modelData g) = driftModelOracle)
                            require "complete drift projection differs" (sameTree (toNode (projection world)) driftProjectionOracle)
                            require "drift projected values mismatch" ((projectionErrors g world).Length = 0)
                            observe "drift-ready" world
                            storeSample "pre-recovery"
                            recoveryCounts <- updates, timeUpdates
                            recoveryStart <- Stopwatch.GetTimestamp ()
                            try
                                if route = "H" then
                                    require "Gaia undo returned false" (Gaia.researchUndo world)
                                else
                                    let payload = Option.get recoveryPayloadOpt
                                    let target = scvalue<Gameplay> payload
                                    Simulants.Gameplay.SetGameplay target world
                                recoveryDirectStop <- Stopwatch.GetTimestamp ()
                                phase <- "await-ready"
                            with error ->
                                recoveryDirectStop <- Stopwatch.GetTimestamp ()
                                raise error
                        | "await-ready" ->
                            storeSample "ready-entry"
                            require "missing readiness timestamp" (readinessStop > 0L)
                            require "event during recovery/readiness" ((updates, timeUpdates) = recoveryCounts)
                            require "ready world not halted" world.TimeHalted
                            oracleWorkStart <- Stopwatch.GetTimestamp ()
                            let actualModel = json (modelData g)
                            let projectionMatches = sameTree (toNode (projection world)) targetProjectionOracle
                            let projectionErrors = projectionErrors g world
                            let modelMatches = actualModel = targetModelOracle
                            let projectedValuesMatch = projectionErrors.Length = 0
                            oracleWorkStop <- Stopwatch.GetTimestamp ()
                            observe "ready-B0" world
                            require "ready model mismatch" modelMatches
                            require "ready projection mismatch" projectionMatches
                            require "ready projected values mismatch" projectedValuesMatch
                            phase <- "complete"
                            finish true "Declared B0 output reached at the next halted callback." world
                        | _ -> ()
                    with error ->
                        if recoveryStart > 0L && recoveryDirectStop = 0L then recoveryDirectStop <- Stopwatch.GetTimestamp ()
                        try observeFailure world with _ -> ()
                        finish false (error.GetType().FullName + ": " + error.Message) world
            try
                Directory.SetCurrentDirectory AppContext.BaseDirectory
                let state =
                    { GaiaState.defaultState with
                        ProjectDllPath = dll
                        ProjectEditModeOpt = Some "Gameplay"
                        ProjectFreshlyLoaded = true
                        ProjectImperativeExecution = false }
                let (actualState, targetDir, plugin) = Nu.initPlus (fun () ->
                    File.WriteAllText (Path.Combine (AppContext.BaseDirectory, Constants.Gaia.StateFilePath), scstring state)
                    Gaia.selectNuPlugin (GaiaPlugin ()))
                Constants.GameTime.DesiredFrameRate <- StaticFrameRate 60L
                emit "configuration"
                    [ "route", box route; "attemptKind", box attemptKind; "attemptId", box attemptId
                      "projectDll", box dll; "checkpoint", box checkpoint; "targetDirectory", box targetDir
                      "functional", box (not actualState.ProjectImperativeExecution)
                      "plugin", box (plugin.GetType().FullName); "runtime", box (Environment.Version.ToString ())
                      "nuAssembly", box typeof<World>.Assembly.FullName; "stopwatchFrequency", box frequency
                      "probeStartTick", box probeStartTick ]
                require "wrong plugin" (plugin.GetType().FullName = typeof<BreakoutPlugin>.FullName)
                Gaia.setResearchPostProcess callback
                let exitCode = Gaia.run actualState targetDir plugin
                emit "engine-exit" [ "exitCode", box exitCode; "probeFinished", box done_; "probePassed", box passed ]
                let compact =
                    fields
                        [ "attemptId", box attemptId; "attemptKind", box attemptKind; "route", box route
                          "pass", box passed; "exitCode", box exitCode; "stopwatchFrequency", box frequency
                          "acquisitionTicks", box (if acquisitionStop > 0L then acquisitionStop - acquisitionStart else -1L)
                          "recoveryDirectTicks", box (if recoveryDirectStop > 0L then recoveryDirectStop - recoveryStart else -1L)
                          "requestToReadyTicks", box (if readinessStop > 0L then readinessStop - recoveryStart else -1L)
                          "oracleWorkTicks", box (if oracleWorkStop > 0L then oracleWorkStop - oracleWorkStart else -1L)
                          "updates", box updates; "timeUpdates", box timeUpdates; "callbacks", box callbacks ]
                File.WriteAllText (Path.Combine (output, "result.json"), json compact + Environment.NewLine)
                if passed && done_ && exitCode = 0 then 0 else 1
            with error ->
                emit "launch-exception"
                    [ "type", box (error.GetType().FullName); "message", box error.Message; "stack", box error.StackTrace ]
                File.WriteAllText (Path.Combine (output, "result.json"),
                                   json (fields ["attemptId", box attemptId; "route", box route; "pass", box false; "error", box error.Message]) + Environment.NewLine)
                1
