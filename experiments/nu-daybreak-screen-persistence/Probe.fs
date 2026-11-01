namespace NuDaybreakScreenPersistence

open System
open System.IO
open System.Numerics
open System.Collections.Generic
open System.Security.Cryptography
open System.Text.Json
open Prime
open Nu
open Nu.Gaia
open Breakout

// Daybreak branch B probe: ordinary screen serializer export/import round-trip.
// Protocol: docs/nu-daybreak-screen-persistence-2026-11-02.md (frozen before any run).
// Observation helpers below are adapted from the reviewed reference observer
// (history B0 probe, public git 663c1b8:experiments/nu-history-b0/Probe.fs) so that
// field encodings and comparisons stay comparable with the closed history-04 process.
module Program =

    let fields (pairs : (string * obj) list) = Dictionary<string, obj> (dict pairs)
    let json value = JsonSerializer.Serialize value
    let bits (value : single) = (BitConverter.SingleToInt32Bits value).ToString "X8"
    let vector (value : Vector3) = [| bits value.X; bits value.Y; bits value.Z |]
    let quaternion (value : Quaternion) = [| bits value.X; bits value.Y; bits value.Z; bits value.W |]
    let colorBits (value : Color) = [| bits value.R; bits value.G; bits value.B; bits value.A |]
    let sha256File path = Convert.ToHexStringLower (SHA256.HashData (File.ReadAllBytes path))

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
        let expectedRotation = Quaternion.CreateFromAxisAngle ((v3 1.0f 0.75f 0.5f).Normalized, single (g.GameplayTime % 360L) |> degToRadF)
        check "model-rotation" (quaternion ((scene / "StaticModel").GetRotation world) = quaternion expectedRotation)
        failures.ToArray ()

    [<EntryPoint; STAThread>]
    let main args =
        if args.Length <> 5 || not (List.contains args[0] ["export"; "import"; "replace-nodestroy"]) then
            eprintfn "Usage: Probe <export|import|replace-nodestroy> <Breakout DLL> <reference checkpoint dir> <transfer dir> <new receipt dir>"
            2
        else
            let mode = args[0]
            let dll = Path.GetFullPath args[1]
            let referenceDir = Path.GetFullPath args[2]
            let transferDir = Path.GetFullPath args[3]
            let output = Path.GetFullPath args[4]
            let transferFile = Path.Combine (transferDir, "gameplay-screen.nuscreen")
            if Directory.Exists output then invalidOp "Receipt directory must be new."
            if mode = "export" && Directory.Exists transferDir && not (Directory.EnumerateFileSystemEntries transferDir |> Seq.isEmpty) then
                invalidOp "Export transfer directory must be new or empty."
            if mode <> "export" && not (File.Exists transferFile) then
                invalidOp "Import transfer file is missing."
            Directory.CreateDirectory output |> ignore
            Directory.CreateDirectory transferDir |> ignore
            let trace = Path.Combine (output, "trace.jsonl")
            let emit label values =
                let record = fields (("event", box label) :: values)
                File.AppendAllText (trace, json record + Environment.NewLine)
            let target = scvalue<Gameplay> (File.ReadAllText (Path.Combine (referenceDir, "gameplay.symbol")))
            let targetProjection = File.ReadAllText (Path.Combine (referenceDir, "projection.json"))
            let mutable callbacks = 0
            let mutable phase = "initialize"
            let mutable passed = false
            let mutable done_ = false
            let observe label world =
                let g = Simulants.Gameplay.GetGameplay world
                emit label ["callbacks", box callbacks
                            "functional", box (not world.Imperative); "accompanied", box world.Accompanied
                            "advancing", box world.Advancing; "model", box (modelData g)
                            "projection", box (projection world); "projectionErrors", box (projectionErrors g world)]
            let finish success detail world =
                passed <- success
                done_ <- true
                emit "result" ["pass", box success; "detail", box detail; "phase", box phase]
                World.setAdvancing false world
                World.exit world
            let require message condition = if not condition then invalidOp message
            let equalModel a b = json (modelData a) = json (modelData b)
            let verifyTarget label world =
                observe label world
                require (label + ": model mismatch") (equalModel target (Simulants.Gameplay.GetGameplay world))
                require (label + ": projected values mismatch") ((projectionErrors target world).Length = 0)
                require (label + ": projection/entity set mismatch") (json (projection world) = targetProjection)
                require (label + ": world advanced") world.Halted
                require (label + ": wrong screen") (World.getSelectedScreen world = Simulants.Gameplay)
                require (label + ": screen not idling") (World.getSelectedScreenIdling world)
            let initialize world =
                require "initial world not halted" world.Halted
                require "Gameplay is not selected/idling" (World.getSelectedScreen world = Simulants.Gameplay && World.getSelectedScreenIdling world)
                let g = Simulants.Gameplay.GetGameplay world
                require "initial Gameplay contract" (g.Score = 0 && g.Bricks.Count = 30 && g.GameplayState = Playing)
                observe "initial" world
                require "initial model negative control passed incorrectly" (not (equalModel target g))
                require "initial projection negative control passed incorrectly" (json (projection world) <> targetProjection)
                emit "negative-controls" ["modelRejected", box true; "projectionRejected", box true]
            let callback (world : World) =
                if not done_ then
                    try
                        callbacks <- callbacks + 1
                        require "callback watchdog" (callbacks <= 1200)
                        require "wrong mode" (not world.Imperative && world.Accompanied)
                        require "wrong static clock" (Constants.GameTime.DesiredFrameRate = StaticFrameRate 60L)
                        match phase with
                        | "initialize" ->
                            initialize world
                            match mode with
                            | "export" ->
                                Simulants.Gameplay.SetGameplay target world
                                phase <- "settle"
                            | "import" ->
                                let groupsBefore = World.getGroups Simulants.Gameplay world |> Seq.map (fun group -> group.Name) |> Seq.toList
                                World.destroyGroupsImmediate (World.getGroups Simulants.Gameplay world) world
                                require "groups not destroyed" (World.getGroups Simulants.Gameplay world |> Seq.isEmpty)
                                let screen = World.readScreenFromFile transferFile None world
                                require "imported wrong screen" (screen = Simulants.Gameplay)
                                World.notifyScreenModelChange screen world
                                emit "import-groups" ["destroyedGroups", box (List.toArray groupsBefore); "policy", box "destroy-groups-then-replace-state"]
                                phase <- "settle"
                            | _ -> // replace-nodestroy
                                let screen = World.readScreenFromFile transferFile None world
                                require "imported wrong screen" (screen = Simulants.Gameplay)
                                World.notifyScreenModelChange screen world
                                emit "import-groups" ["destroyedGroups", box ([||] : string array); "policy", box "replace-state-only"]
                                phase <- "settle"
                        | "settle" ->
                            match mode with
                            | "export" ->
                                verifyTarget "pre-export-B0" world
                                World.writeScreenToFile transferFile Simulants.Gameplay world
                                let descriptorStr = File.ReadAllText transferFile
                                let descriptor = scvalue<ScreenDescriptor> descriptorStr
                                let propertyNames = descriptor.ScreenProperties |> Map.toList |> List.map fst |> List.sort
                                let modelRoundTrip =
                                    match Map.tryFind "Model" descriptor.ScreenProperties with
                                    | Some modelSymbol ->
                                        try let converter = SymbolicConverter (false, None, typeof<DesignerProperty>)
                                            let dp = converter.ConvertFrom modelSymbol :?> DesignerProperty
                                            match dp.DesignerValue with
                                            | :? Gameplay as g -> equalModel target g
                                            | _ -> false
                                        with _ -> false
                                    | None -> false
                                emit "export-inspection"
                                    ["fileBytes", box (FileInfo(transferFile).Length)
                                     "fileSha256", box (sha256File transferFile)
                                     "screenDispatcherName", box descriptor.ScreenDispatcherName
                                     "propertyNames", box (List.toArray propertyNames)
                                     "groupDescriptorCount", box descriptor.GroupDescriptors.Length
                                     "screenNameOpt", box (match ScreenDescriptor.getNameOpt descriptor with Some n -> n | None -> "")
                                     "modelPropertyPresent", box (Map.containsKey "Model" descriptor.ScreenProperties)
                                     "modelRoundTripEqualsB0", box modelRoundTrip]
                                phase <- "exported"
                            | "import" ->
                                verifyTarget "post-import-B0" world
                                phase <- "verified"
                            | _ -> // replace-nodestroy
                                observe "post-import-diagnostic" world
                                require "diagnostic: model was not replaced" (equalModel target (Simulants.Gameplay.GetGameplay world))
                                require "diagnostic: world advanced" world.Halted
                                let names = World.getEntities scene world |> Seq.map (fun entity -> entity.Name) |> Seq.toList
                                let brickEntities = names |> List.filter (fun name -> name.StartsWith "@")
                                let projectionMatches = json (projection world) = targetProjection
                                emit "diagnostic"
                                    ["entityCount", box names.Length
                                     "brickEntityCount", box brickEntities.Length
                                     "expectedBrickCountFromModel", box target.Bricks.Count
                                     "projectionMatchesB0", box projectionMatches
                                     "predictionWasStaleEntitiesSurvive", box true
                                     "predictionObserved", box (not projectionMatches && brickEntities.Length = 30 + target.Bricks.Count)]
                                finish true "Diagnostic complete: model replaced; stale-content prediction recorded." world
                        | "exported" ->
                            verifyTarget "post-export-B0" world
                            finish true "Export wrote a screen file whose model round-trips to B0; world undisturbed." world
                        | "verified" ->
                            verifyTarget "post-import-next-boundary" world
                            finish true "Import reproduced the B0 model and projected content at a halted boundary." world
                        | _ -> ()
                    with ex ->
                        emit "exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace]
                        finish false ex.Message world
            try
                Directory.SetCurrentDirectory AppContext.BaseDirectory
                let state = { GaiaState.defaultState with ProjectDllPath = dll; ProjectEditModeOpt = Some "Gameplay"; ProjectFreshlyLoaded = true; ProjectImperativeExecution = false }
                let (actualState, targetDir, plugin) = Nu.initPlus (fun () ->
                    File.WriteAllText (Path.Combine (AppContext.BaseDirectory, Constants.Gaia.StateFilePath), scstring state)
                    Gaia.selectNuPlugin (GaiaPlugin ()))
                Constants.GameTime.DesiredFrameRate <- StaticFrameRate 60L
                emit "configuration" ["arm", box mode; "projectDll", box dll; "targetDirectory", box targetDir
                                      "referenceGameplaySha256", box (sha256File (Path.Combine (referenceDir, "gameplay.symbol")))
                                      "referenceProjectionSha256", box (sha256File (Path.Combine (referenceDir, "projection.json")))
                                      "transferFile", box transferFile
                                      "functional", box (not actualState.ProjectImperativeExecution)
                                      "plugin", box (plugin.GetType().FullName); "runtime", box (Environment.Version.ToString())
                                      "nuAssembly", box typeof<World>.Assembly.FullName]
                require "selected plugin is not Breakout" (plugin.GetType().FullName = typeof<BreakoutPlugin>.FullName)
                Gaia.setResearchPostProcess callback
                let exitCode = Gaia.run actualState targetDir plugin
                emit "engine-exit" ["exitCode", box exitCode; "probeFinished", box done_; "probePassed", box passed]
                if passed && done_ && exitCode = 0 then 0 else 1
            with ex ->
                emit "launch-exception" ["type", box (ex.GetType().FullName); "message", box ex.Message; "stack", box ex.StackTrace]
                1
