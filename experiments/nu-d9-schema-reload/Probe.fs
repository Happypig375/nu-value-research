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
        if args.Length <> 3 then
            eprintfn "Usage: Probe <Breakout DLL> <Gameplay.fs to edit> <new receipt dir>"
            2
        else
            let dll, gameplaySource, output = Path.GetFullPath args[0], Path.GetFullPath args[1], Path.GetFullPath args[2]
            if Directory.Exists output then invalidOp "Receipt directory must be new."
            Directory.CreateDirectory output |> ignore
            let trace = Path.Combine (output, "trace.jsonl")
            let emit label (values : (string * obj) list) =
                File.AppendAllText (trace, json (fields (("event", box label) :: ("utcMs", box (utcMs ())) :: values)) + Environment.NewLine)
            let mutable phase, callbacks, updates, reloadEvents, settle = "initialize", 0, 0, 0, 0
            let mutable before : (string * string) array = [||]
            let mutable done_ = false
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
                        | "initialize" ->
                            require "initial world advancing" world.TimeHalted
                            require "Gameplay not selected" (World.getSelectedScreen world = Simulants.Gameplay)
                            World.subscribe (fun _ _ -> updates <- updates + 1; Cascade) Simulants.Gameplay.UpdateEvent Game world |> ignore
                            World.subscribe (fun _ _ -> reloadEvents <- reloadEvents + 1; Cascade) Game.CodeReloadEvent Game world |> ignore
                            Gaia.researchToggleAdvancing world
                            phase <- "advance"
                        | "advance" ->
                            let g = Simulants.Gameplay.GetGameplay world
                            if world.TimeAdvancing && g.GameplayTime >= 10L then
                                World.setTimeAdvancing false world
                                phase <- "halting"
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
                                emit "post-reload"
                                    [ "modelType", box (m.GetType().FullName); "modelAssembly", box (m.GetType().Assembly.FullName)
                                      "fields", box afterMap; "oldFieldsPreserved", box oldPreserved
                                      "brickReward", box (if afterMap.ContainsKey "BrickReward" then afterMap["BrickReward"] else "(absent)")
                                      "requiredBrickReward", box "200"; "codeReloadEvents", box reloadEvents
                                      "fsiHasProjectCode", box (Gaia.researchFsiHasProjectCode ()); "halted", box world.TimeHalted ]
                                finish true "Reload observed." world
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
