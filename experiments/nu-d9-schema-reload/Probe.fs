namespace NuD9SchemaReload

// D9 direction 2, route L (live reload, no migration), case A (absent field; required value 200), unscored feasibility.
// Gaia functional, Gameplay edit mode, Nu master 47ef39e (Vulkan). Advance 10 updates, halt, apply the October R10
// schema edit to Gameplay.fs on disk (add BrickReward : int, initializer 200 in `empty`, used in scoring), call Gaia's
// own code reload, then read the live model by reflection. Observations only.
// Protocol: docs/nu-d9-directions-2-4-packets-2026-11-10.md, direction 2.

open System
open System.Diagnostics
open System.IO
open System.Text
open System.Text.Json
open System.Collections.Generic
open Microsoft.FSharp.Reflection
open Prime
open Nu
open Nu.Gaia
open Breakout

module Program =
    let fields (pairs : (string * obj) list) = Dictionary<string, obj> (dict pairs)
    let json value = JsonSerializer.Serialize value
    let utcMs () = DateTimeOffset.UtcNow.ToUnixTimeMilliseconds ()
    let recordFields (value : obj) =
        if isNull value || not (FSharpType.IsRecord (value.GetType (), true)) then [||]
        else
            let t = value.GetType ()
            Array.zip (FSharpType.GetRecordFields (t, true) |> Array.map (fun p -> p.Name)) (FSharpValue.GetRecordFields (value, true))
            |> Array.map (fun (n, v) -> n, sprintf "%A" v)
    let edits =
        [ "      Score : int\n      Lives : int }", "      Score : int\n      Lives : int\n      BrickReward : int }"
          "          Score = 0\n          Lives = 0 }", "          Score = 0\n          Lives = 0\n          BrickReward = 200 }"
          "                let scoring = Map.count bricksIntersected * 100", "                let scoring = Map.count bricksIntersected * gameplay.BrickReward" ]

    let applyEdit (path : string) =
        let raw = File.ReadAllBytes path
        let bom = raw.Length >= 3 && raw[0] = 0xEFuy && raw[1] = 0xBBuy && raw[2] = 0xBFuy
        let text = Encoding.UTF8.GetString (if bom then raw[3..] else raw)
        let crlf = text.Contains "\r\n"
        let mutable body = text.Replace ("\r\n", "\n")
        for (o, n) in edits do
            let count = (body.Length - body.Replace(o, "").Length) / o.Length
            if count <> 1 then invalidOp ("schema edit anchor not unique: " + o)
            body <- body.Replace (o, n)
        let body = if crlf then body.Replace ("\n", "\r\n") else body
        let out = Array.append (if bom then [| 0xEFuy; 0xBBuy; 0xBFuy |] else [||]) (Encoding.UTF8.GetBytes body)
        File.WriteAllBytes (path, out)

    [<EntryPoint; STAThread>]
    let main args =
        if args.Length <> 6 || not (List.contains args[0] ["L"; "M"; "R1"; "R2"]) || not (List.contains args[1] ["A"; "Z"; "N"]) then
            eprintfn "Usage: Probe <L|M|R1|R2> <A|Z|N> <Breakout DLL> <Gameplay.fs to edit, or transfer dir for R1/R2> <B0 seed gameplay.symbol> <new receipt dir>"
            2
        else
            let route, case = args[0], args[1]
            // Amendment 4: required new-field value per case (A absent -> declared default 200; Z deliberate zero; N nondefault 75)
            let required = match case with "A" -> 200 | "Z" -> 0 | _ -> 75
            let dll, gameplaySource, seedPath, output = Path.GetFullPath args[2], Path.GetFullPath args[3], Path.GetFullPath args[4], Path.GetFullPath args[5]
            if Directory.Exists output then invalidOp "Receipt directory must be new."
            Directory.CreateDirectory output |> ignore
            let trace = Path.Combine (output, "trace.jsonl")
            let emit label (values : (string * obj) list) =
                File.AppendAllText (trace, json (fields (("event", box label) :: ("utcMs", box (utcMs ())) :: values)) + Environment.NewLine)
            let mutable phase, callbacks, updates, reloadEvents, settle = "initialize", 0, 0, 0, 0
            let mutable before : (string * string) array = [||]
            let mutable done_ = false
            let mutable entityNamesAfterReload : string array = [||]
            let mutable hitTarget = ""
            let mutable contStartClock = -1L
            let mutable contHaltRequested = false
            let fieldOf (m : obj) name = match (dict (recordFields m)).TryGetValue name with | (true, v) -> v | _ -> "(absent)"
            let beginContinuation (world : World) =
                let m = Simulants.Gameplay.GetModelGeneric<obj> world
                contStartClock <- int64 (fieldOf m "GameplayTime" |> fun s -> s.TrimEnd 'L')
                emit "continuation-start" ["score", box (fieldOf m "Score"); "brickReward", box (fieldOf m "BrickReward"); "clock", box contStartClock]
                Gaia.researchToggleAdvancing world
                phase <- "continue"
            let require m c = if not c then invalidOp m
            let finish ok detail (world : World) =
                done_ <- true
                emit "result" ["complete", box ok; "detail", box detail; "phase", box phase]
                if world.TimeAdvancing then World.setTimeAdvancing false world
                World.exit world
            let liveModel (world : World) = Simulants.Gameplay.GetModelGeneric<obj> world
            let callback (world : World) =
                if not done_ then
                    try
                        callbacks <- callbacks + 1
                        require "callback watchdog (2400)" (callbacks <= 2400)
                        match phase with
                        | "initialize" when route = "R2" ->
                            // Amendment 3, route R process 2 (new code, fresh process): reconstruct with the new field explicit
                            let transfer = gameplaySource
                            let oldFields = JsonSerializer.Deserialize<Dictionary<string, string>> (File.ReadAllText (Path.Combine (transfer, "fields.json")))
                            let t0 = Stopwatch.GetTimestamp ()
                            let converted = scvalue<Gameplay> (File.ReadAllText (Path.Combine (transfer, "model.symbol")))
                            let t = converted.GetType ()
                            let props = FSharpType.GetRecordFields (t, true)
                            let values = FSharpValue.GetRecordFields (converted, true)
                            let convertedReward = match props |> Array.tryFindIndex (fun p -> p.Name = "BrickReward") with Some i -> sprintf "%A" values[i] | None -> "(absent)"
                            match props |> Array.tryFindIndex (fun p -> p.Name = "BrickReward") with Some i -> values[i] <- box required | None -> ()
                            let target = FSharpValue.MakeRecord (t, values, true) :?> Gameplay
                            Simulants.Gameplay.SetGameplay target world
                            let t1 = Stopwatch.GetTimestamp ()
                            emit "reconstructed" ["reconstructMs", box (float (t1 - t0) * 1000.0 / float Stopwatch.Frequency)
                                                  "brickRewardAfterSymbolConversion", box convertedReward; "oldFields", box oldFields]
                            before <- [| for KeyValue (k, v) in oldFields -> k, v |]
                            phase <- "settle-reconstructed"
                            settle <- 0
                        | "settle-reconstructed" ->
                            settle <- settle + 1
                            if settle >= 10 then
                                let m = liveModel world
                                let afterMap = dict (recordFields m)
                                let oldPreserved = before |> Array.forall (fun (n, v) -> afterMap.ContainsKey n && afterMap[n] = v)
                                emit "post-reconstruction"
                                    [ "modelType", box (m.GetType().FullName); "oldFieldsPreserved", box oldPreserved
                                      "brickReward", box (if afterMap.ContainsKey "BrickReward" then afterMap["BrickReward"] else "(absent)")
                                      "requiredBrickReward", box (string required); "halted", box world.TimeHalted
                                      "processUptimeMs", box (int64 (DateTime.Now - Process.GetCurrentProcess().StartTime).TotalMilliseconds) ]
                                beginContinuation world
                        | "initialize" ->
                            require "initial world advancing" world.TimeHalted
                            require "Gameplay not selected" (World.getSelectedScreen world = Simulants.Gameplay)
                            World.subscribe (fun _ _ -> updates <- updates + 1; Cascade) Simulants.Gameplay.UpdateEvent Game world |> ignore
                            World.subscribe (fun _ _ -> reloadEvents <- reloadEvents + 1; Cascade) Game.CodeReloadEvent Game world |> ignore
                            // Amendment 4: seed a deterministic one-brick-hit state (B0 model; ball just under a bottom-row brick, moving up)
                            let b0 = scvalue<Gameplay> (File.ReadAllText seedPath)
                            let (hitName, hitBrick) = b0.Bricks |> Map.toList |> List.filter (fun (_, b) -> b.Position.Y = 64.0f) |> List.minBy (fun (_, b) -> abs (b.Position.X + 64.0f))
                            let seeded = { b0 with Ball = { b0.Ball with Position = Numerics.Vector3 (hitBrick.Position.X, 52.0f, 0.0f); Direction = Numerics.Vector3 (0.0f, 1.0f, 0.0f) } }
                            hitTarget <- hitName
                            Simulants.Gameplay.SetGameplay seeded world
                            emit "seeded" ["hitBrick", box hitName; "score", box seeded.Score; "bricks", box seeded.Bricks.Count]
                            phase <- "halting"
                        | "advance" ->
                            let g = Simulants.Gameplay.GetGameplay world
                            if world.TimeAdvancing && g.GameplayTime >= 10L then
                                World.setTimeAdvancing false world
                                phase <- "halting"
                        | "halting" when world.TimeHalted && route = "R1" ->
                            // Amendment 3, route R process 1 (old code): save the model and its fields, then exit
                            let transfer = gameplaySource
                            Directory.CreateDirectory transfer |> ignore
                            let g = Simulants.Gameplay.GetGameplay world
                            File.WriteAllText (Path.Combine (transfer, "model.symbol"), scstring g)
                            File.WriteAllText (Path.Combine (transfer, "fields.json"), json (dict (recordFields (liveModel world))))
                            emit "saved" ["fields", box (dict (recordFields (liveModel world)))]
                            finish true "Old-code model saved." world
                        | "halting" when world.TimeHalted ->
                            before <- recordFields (liveModel world)
                            emit "pre-reload" ["modelType", box ((liveModel world).GetType().FullName); "fields", box (dict before)]
                            applyEdit gameplaySource
                            let t0 = Stopwatch.GetTimestamp ()
                            Gaia.researchReloadCode world
                            let t1 = Stopwatch.GetTimestamp ()
                            emit "reload-called" ["reloadMs", box (float (t1 - t0) * 1000.0 / float Stopwatch.Frequency)
                                                  "fsiHasProjectCode", box (Gaia.researchFsiHasProjectCode ()); "codeReloadEvents", box reloadEvents]
                            phase <- "settle"
                        | "settle" ->
                            settle <- settle + 1
                            if settle >= 10 then
                                let m = liveModel world
                                let after = recordFields m
                                let afterMap = dict after
                                let oldPreserved = before |> Array.forall (fun (n, v) -> afterMap.ContainsKey n && afterMap[n] = v)
                                let names (w : World) = World.getEntities Simulants.GameplayScene w |> Seq.map (fun e -> e.Name) |> Seq.sort |> Seq.toArray
                                entityNamesAfterReload <- names world
                                emit "post-reload"
                                    [ "modelType", box (m.GetType().FullName); "modelAssembly", box (m.GetType().Assembly.FullName)
                                      "fields", box afterMap; "oldFieldsPreserved", box oldPreserved
                                      "brickReward", box (if afterMap.ContainsKey "BrickReward" then afterMap["BrickReward"] else "(absent)")
                                      "requiredBrickReward", box (string required); "codeReloadEvents", box reloadEvents
                                      "fsiHasProjectCode", box (Gaia.researchFsiHasProjectCode ()); "halted", box world.TimeHalted ]
                                if route = "L" then beginContinuation world
                                else
                                    // Amendment 2: explicit migration, case A (required 200), via the reloaded code's own setter
                                    let t = m.GetType ()
                                    let props = FSharpType.GetRecordFields (t, true)
                                    let values = FSharpValue.GetRecordFields (m, true)
                                    let i = props |> Array.findIndex (fun p -> p.Name = "BrickReward")
                                    values[i] <- box required
                                    let migrated = FSharpValue.MakeRecord (t, values, true)
                                    let ext = t.Assembly.GetTypes () |> Array.find (fun ty -> ty.FullName.EndsWith "Breakout.GameplayExtensions")
                                    let setter = ext.GetMethods () |> Array.find (fun mi -> mi.Name = "Screen.SetGameplay")
                                    let t0 = Stopwatch.GetTimestamp ()
                                    setter.Invoke (null, [| box Simulants.Gameplay; migrated; box world |]) |> ignore
                                    let t1 = Stopwatch.GetTimestamp ()
                                    emit "migration-applied" ["migrationMs", box (float (t1 - t0) * 1000.0 / float Stopwatch.Frequency); "setter", box (ext.FullName + "." + setter.Name)]
                                    phase <- "settle-migrated"
                                    settle <- 0
                        | "settle-migrated" ->
                            settle <- settle + 1
                            if settle >= 10 then
                                let m = liveModel world
                                let afterMap = dict (recordFields m)
                                let oldPreserved = before |> Array.forall (fun (n, v) -> afterMap.ContainsKey n && afterMap[n] = v)
                                let names = World.getEntities Simulants.GameplayScene world |> Seq.map (fun e -> e.Name) |> Seq.sort |> Seq.toArray
                                emit "post-migration"
                                    [ "modelType", box (m.GetType().FullName); "oldFieldsPreserved", box oldPreserved
                                      "brickReward", box (if afterMap.ContainsKey "BrickReward" then afterMap["BrickReward"] else "(absent)")
                                      "requiredBrickReward", box (string required); "sceneNamesUnchanged", box (names = entityNamesAfterReload)
                                      "halted", box world.TimeHalted ]
                                beginContinuation world
                        | "continue" when world.TimeAdvancing ->
                            let m = liveModel world
                            let clock = int64 ((fieldOf m "GameplayTime").TrimEnd 'L')
                            if clock >= contStartClock + 1L && not contHaltRequested then
                                World.setTimeAdvancing false world
                                contHaltRequested <- true
                        | "continue" when world.TimeHalted && contHaltRequested ->
                            let m = liveModel world
                            let bricks = fieldOf m "Bricks"
                            emit "continuation"
                                [ "clock", box (fieldOf m "GameplayTime"); "score", box (fieldOf m "Score"); "brickReward", box (fieldOf m "BrickReward")
                                  "hitBrickRemoved", box (not (bricks.Contains ("\"" + hitTarget + "\""))); "requiredBrickReward", box (string required)
                                  "expectedScore", box (string (100 + required)) ]
                            finish true "Continuation observed." world
                        | _ -> ()
                    with ex ->
                        emit "probe-exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace; "phase", box phase]
                        finish false ex.Message world
            try
                Directory.SetCurrentDirectory AppContext.BaseDirectory
                let state = { GaiaState.defaultState with ProjectDllPath = dll; ProjectEditModeOpt = Some "Gameplay"; ProjectFreshlyLoaded = true; ProjectImperativeExecution = false }
                let (actualState, targetDir, plugin) = Nu.initPlus (fun () ->
                    File.WriteAllText (Path.Combine (AppContext.BaseDirectory, Constants.Gaia.StateFilePath), scstring state)
                    Gaia.selectNuPlugin (GaiaPlugin ()))
                Constants.GameTime.DesiredFrameRate <- StaticFrameRate 60L
                emit "configuration" ["targetDirectory", box targetDir; "nuAssembly", box typeof<World>.Assembly.FullName]
                Gaia.setResearchPostProcess callback
                let exitCode = Gaia.run actualState targetDir plugin
                emit "engine-exit" ["exitCode", box exitCode; "probeFinished", box done_]
                exitCode
            with ex ->
                emit "launch-exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace]
                3
