namespace NuRecoveryTriggerResearch

// Observer for the branch A recovery-trigger check (docs/nu-daybreak-recovery-trigger-2026-11-03.md, section 4).
// It records observations only; check.py applies the pass/fail conditions. The model and scene serializers are
// copied from experiments/nu-history-b0/Probe.fs.

open System
open System.IO
open System.Numerics
open System.Collections.Generic
open System.Text.Json
open Prime
open Nu
open Nu.Gaia
open Breakout

module Program =
    let fields (pairs : (string * obj) list) = Dictionary<string, obj> (dict pairs)
    let json value = JsonSerializer.Serialize value
    let bits (value : single) = (BitConverter.SingleToInt32Bits value).ToString "X8"
    let vector (value : Vector3) = [| bits value.X; bits value.Y; bits value.Z |]
    let quaternion (value : Quaternion) = [| bits value.X; bits value.Y; bits value.Z; bits value.W |]
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
              "messageText", box ((scene / "Message").GetText world)
              "rotation", box (quaternion ((scene / "StaticModel").GetRotation world)) ]

    [<EntryPoint; STAThread>]
    let main args =
        if args.Length <> 3 || not (List.contains args[0] ["a0"; "a1"; "a2"]) then
            eprintfn "Usage: Probe <a0|a1|a2> <Breakout DLL> <new receipt directory>"
            2
        else
            let arm, dll, output = args[0], Path.GetFullPath args[1], Path.GetFullPath args[2]
            let imperative = (arm = "a2")
            if Directory.Exists output then invalidOp "Receipt directory must be new."
            Directory.CreateDirectory output |> ignore
            let trace = Path.Combine (output, "trace.jsonl")
            let emit label values =
                let record = fields (("event", box label) :: values)
                File.AppendAllText (trace, json record + Environment.NewLine)
            let mutable updates = 0
            let mutable timeUpdates = 0
            let mutable callbacks = 0
            let mutable phase = "initialize"
            let mutable pass = 0
            let mutable pastsBase = -1
            let mutable s0Model = ""
            let mutable s0Projection = ""
            let mutable kState : WorldState option = None
            let mutable lastGood : (int64 * string) option = None
            let mutable lastTime = -1L
            let times = ResizeArray<int64> ()
            let mutable settleHooks = 0
            let mutable sequenceComplete = false
            let mutable done_ = false
            let require message condition = if not condition then invalidOp message
            let snapshotFields (world : World) =
                let g = Simulants.Gameplay.GetGameplay world
                let modelJson = json (modelData g)
                let projectionJson = json (projection world)
                [ "pass", box pass; "updates", box updates; "timeUpdates", box timeUpdates; "callbacks", box callbacks
                  "imperative", box world.Imperative; "advancing", box world.Advancing
                  "pasts", box (Gaia.researchPastsCount ()); "futures", box (Gaia.researchFuturesCount ())
                  "pastsHeadIsAdvance", box (Gaia.researchPastsHeadIsAdvance ())
                  "messageBox", box (Option.toObj (Gaia.researchMessageBox ()))
                  "liveStateIsK", box (match kState with Some k -> Object.ReferenceEquals (k, world.CurrentState) | None -> false)
                  "modelEqualsS0", box (modelJson = s0Model); "projectionEqualsS0", box (projectionJson = s0Projection)
                  "gameplayTime", box g.GameplayTime; "model", box (modelData g); "projection", box (projection world) ]
            let finish complete detail (world : World) =
                sequenceComplete <- complete
                done_ <- true
                emit "result" ["sequenceComplete", box complete; "detail", box detail; "phase", box phase; "pass", box pass
                               "updates", box updates; "timeUpdates", box timeUpdates; "callbacks", box callbacks]
                if world.Advancing then World.setAdvancing false world
                World.exit world
            let advance label (world : World) =
                let before = world.CurrentState
                Gaia.researchToggleAdvancing world
                kState <- Gaia.researchPastsHeadState ()
                let headIsBefore = match kState with Some k -> Object.ReferenceEquals (k, before) | None -> false
                emit label (snapshotFields world @ ["headIsPreAdvanceState", box headIsBefore])
                require (label + ": Pasts count is not base + 1") (Gaia.researchPastsCount () = pastsBase + 1)
                require (label + ": Pasts head is not an Advance snapshot") (Gaia.researchPastsHeadIsAdvance ())
                require (label + ": Pasts head is not the pre-Advance state") headIsBefore
                lastTime <- -1L
                lastGood <- None
                times.Clear ()
            let callback (world : World) =
                if not done_ then
                    try
                        callbacks <- callbacks + 1
                        require "callback watchdog (1200)" (callbacks <= 1200)
                        require "wrong mode" (world.Imperative = imperative && world.Accompanied)
                        require "wrong static clock" (Constants.GameTime.DesiredFrameRate = StaticFrameRate 60L)
                        let g = Simulants.Gameplay.GetGameplay world
                        match phase with
                        | "initialize" ->
                            require "initial world is advancing" world.Halted
                            require "Gameplay is not selected/idling" (World.getSelectedScreen world = Simulants.Gameplay && World.getSelectedScreenIdling world)
                            require "initial Gameplay contract" (g.Score = 0 && g.Bricks.Count = 30 && g.GameplayState = Playing)
                            require "initial gameplay clock is not before the trigger (invalid)" (g.GameplayTime < 30L)
                            World.subscribe (fun _ _ -> updates <- updates + 1; Cascade) Simulants.Gameplay.UpdateEvent Game world |> ignore
                            World.subscribe (fun _ _ -> timeUpdates <- timeUpdates + 1; Cascade) Simulants.Gameplay.TimeUpdateEvent Game world |> ignore
                            pastsBase <- Gaia.researchPastsCount ()
                            s0Model <- json (modelData g)
                            s0Projection <- json (projection world)
                            emit "settled-S0" (snapshotFields world @ ["P0", box pastsBase])
                            pass <- 1
                            advance "advance-1" world
                            phase <- "run"
                        | "run" ->
                            let pasts = Gaia.researchPastsCount ()
                            if pasts = pastsBase + 1 then
                                if world.Advancing then
                                    if lastTime >= 0L && g.GameplayTime <> lastTime + 1L && g.GameplayTime <> lastTime then
                                        emit "clock-irregular" ["previous", box lastTime; "current", box g.GameplayTime]
                                    times.Add g.GameplayTime
                                    lastTime <- g.GameplayTime
                                    lastGood <- Some (g.GameplayTime, json (modelData g))
                                    if arm = "a0" && g.GameplayTime >= 60L then
                                        emit "a0-60-updates" (snapshotFields world)
                                        finish true "A0 advanced 60 gameplay updates." world
                                if not done_ && updates >= 600 then
                                    emit "trigger-not-reached" (snapshotFields world)
                                    finish false "Trigger not reached within 600 Update events (invalid)." world
                            elif pasts = pastsBase then
                                emit (sprintf "recovery-%d-immediate" pass)
                                    (snapshotFields world @
                                     [ "lastGoodHookTime", box (match lastGood with Some (t, _) -> t | None -> -1L)
                                       "lastGoodHookModel", box (match lastGood with Some (_, m) -> m | None -> "")
                                       "hookTimes", box (times.ToArray ()) ])
                                settleHooks <- 0
                                phase <- "settle"
                            else
                                emit "unexpected-history" (snapshotFields world)
                                finish false "Unexpected Pasts count during run." world
                        | "settle" ->
                            if world.Advancing then
                                emit "advancing-during-settle" (snapshotFields world)
                                finish false "World advanced during the halted settle window." world
                            else
                                settleHooks <- settleHooks + 1
                                if settleHooks >= 10 then
                                    emit (sprintf "recovery-%d-settled" pass) (snapshotFields world @ ["settleHooks", box settleHooks])
                                    if pass = 1 then
                                        pass <- 2
                                        advance "advance-2" world
                                        phase <- "run"
                                    else finish true "Two fault/recovery passes observed." world
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
                emit "configuration" ["arm", box arm; "projectDll", box dll; "targetDirectory", box targetDir
                                      "imperative", box actualState.ProjectImperativeExecution
                                      "plugin", box (plugin.GetType().FullName); "runtime", box (Environment.Version.ToString())
                                      "nuAssembly", box typeof<World>.Assembly.FullName]
                require "selected plugin is not Breakout" (plugin.GetType().FullName = typeof<BreakoutPlugin>.FullName)
                require "Gaia state does not have the arm's execution mode" (actualState.ProjectImperativeExecution = imperative)
                Gaia.setResearchPostProcess callback
                let exitCode = Gaia.run actualState targetDir plugin
                emit "engine-exit" ["exitCode", box exitCode; "probeFinished", box done_; "sequenceComplete", box sequenceComplete
                                    "phase", box phase; "pass", box pass; "updates", box updates; "timeUpdates", box timeUpdates
                                    "lastGoodHookTime", box (match lastGood with Some (t, _) -> t | None -> -1L)
                                    "hookTimes", box (times.ToArray ())]
                exitCode
            with ex ->
                emit "launch-exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace]
                3
