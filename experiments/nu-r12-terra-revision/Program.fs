namespace TerraFirma

open System
open System.IO
open System.Diagnostics
open System.Globalization
open System.Numerics
open System.Reflection
open System.Runtime
open System.Runtime.InteropServices
open System.Security.Cryptography
open System.Text.Json
open System.Text.RegularExpressions
open SDL
open Prime
open Nu

module SceneRevisionProbe =

    let expectedNuSha = "e96cd61d188c689f7e39e2670b4d8582e26b9ea2dc95e1a15056891b7c99cd68"
    let expectedSceneSha = "1dff90c5679233f6b282e03bcb2f2fd7524a6e6e93a7df814a72f5260d3a421a"
    let expectedProtocolSha = "e6576d9ae1d825c8b9f3cb029ec3f57c22fb01f5cac12057cc3ae0b8db91fc49"
    let sourceAddress = "Game/Gameplay/Scene/Villa/Palm"
    let localAddress = "Game/Gameplay/Scene/Villa-0002/Palm-0009"
    let palmNames = [|"Palm"; "Palm-0009"; "Palm-0010"; "Palm-0011"; "Palm-0012"; "Palm-0013"; "Palm-0014"; "Palm-0016"|]
    let family =
        [| for villa in [|"Villa"; "Villa-0002"; "Villa-0003"; "Villa-0004"|] do
               for palm in palmNames do yield "Game/Gameplay/Scene/" + villa + "/" + palm |]
        |> Array.sortWith (fun a b -> StringComparer.Ordinal.Compare (a, b))
    let entityAt (address : string) = Nu.Entity (address.Split '/')
    let transforms = Set.ofList ["Position"; "PositionLocal"; "Rotation"; "RotationLocal"; "Scale"; "ScaleLocal"]
    let selectedProperties =
        ["Position"; "PositionLocal"; "Rotation"; "RotationLocal"; "Scale"; "ScaleLocal";
         "Size"; "Offset"; "MountOpt"; "Static"; "Clipped"; "BodyShape"; "StaticModel";
         "MaterialProperties"; "PropagationSourceOpt"; "PropagatedDescriptorOpt"]

    type PropertyObservation =
        { Name : string; Found : bool; TypeName : string; Value : string
          ExpectedPresent : bool; ExpectedSymbol : string; ExpectedCanonical : string; Error : string }

    type EntityObservation =
        { Address : string; Parent : string; Name : string; Dispatcher : string
          Id : string; Persistent : bool; Protection : string; Children : string array
          Original : bool; Properties : PropertyObservation array }

    type LifeObservation =
        { Ordinal : int64; Callback : int; Phase : string; ElapsedSeconds : float
          Kind : string; Address : string; Entity : bool; Exists : bool; Id : string; Error : string }

    type Boundary = { Name : string; Callback : int; Counter : int64; ElapsedSeconds : float }

    type Check = { Name : string; Passed : bool }

    let sameProperty name (a : string) (b : string) =
        if transforms.Contains name then
            let tokens (text : string) = Regex.Split (text, @"[\s\[\]]+") |> Array.filter (String.IsNullOrEmpty >> not)
            let left, right = tokens a, tokens b
            left.Length = right.Length && left.Length > 0 &&
            Array.forall2 (fun (x : string) (y : string) ->
                match Double.TryParse (x, NumberStyles.Float, CultureInfo.InvariantCulture), Double.TryParse (y, NumberStyles.Float, CultureInfo.InvariantCulture) with
                | (true, u), (true, v) -> Double.IsFinite u && Double.IsFinite v && abs (u - v) <= 0.0001
                | _ -> false) left right
        else a = b

    let shaFile path =
        use stream = File.OpenRead path
        use hash = SHA256.Create ()
        hash.ComputeHash stream |> Convert.ToHexString |> fun text -> text.ToLowerInvariant ()

    let saveJson path (value : obj) =
        let options = JsonSerializerOptions (WriteIndented = true)
        File.WriteAllText (path, JsonSerializer.Serialize (value, value.GetType (), options))

    let identities () =
        AppDomain.CurrentDomain.GetAssemblies ()
        |> Array.filter (fun assembly -> not assembly.IsDynamic && not (String.IsNullOrWhiteSpace assembly.Location))
        |> Array.map (fun assembly ->
            {| Name = assembly.GetName().Name; Version = string (assembly.GetName().Version)
               Path = assembly.Location; Sha256 = shaFile assembly.Location |})
        |> Array.sortBy (fun item -> item.Name)

    let rec originals parent (descriptors : EntityDescriptor list) =
        seq {
            for descriptor in descriptors do
                let name = EntityDescriptor.getNameOpt descriptor |> Option.defaultWith (fun () -> failwith "Unnamed original node.")
                let address = parent + "/" + name
                yield address, descriptor
                yield! originals address descriptor.EntityDescriptors }

    let observeProperty (expected : Map<string, Symbol>) (entity : Entity) world name =
        let original = Map.tryFind name expected
        let initial =
            { Name = name; Found = false; TypeName = ""; Value = ""
              ExpectedPresent = Option.isSome original
              ExpectedSymbol = original |> Option.map Symbol.toString |> Option.defaultValue ""
              ExpectedCanonical = ""; Error = "" }
        try
            match entity.TryGetProperty name world with
            | None -> initial
            | Some property ->
                let converter = SymbolicConverter (false, None, property.PropertyType)
                let stringify value = Symbol.toString (converter.ConvertTo (value, typeof<Symbol>) :?> Symbol)
                let actual = stringify property.PropertyValue
                let canonical = original |> Option.map (fun symbol -> stringify (converter.ConvertFrom symbol)) |> Option.defaultValue ""
                { initial with Found = true; TypeName = property.PropertyType.FullName; Value = actual; ExpectedCanonical = canonical }
        with error -> { initial with Error = error.ToString () }

    let rec observeEntities parent (expected : Map<string, EntityDescriptor>) (entities : Entity seq) world =
        seq {
            for entity in entities |> Seq.sortBy (fun entity -> entity.Name) do
                let address = parent + "/" + entity.Name
                let original = Map.tryFind address expected
                let properties = original |> Option.map (fun node -> node.EntityProperties) |> Option.defaultValue Map.empty
                let names = Set.union (properties |> Map.keys |> Set.ofSeq) (Set.ofList selectedProperties)
                let children = entity.GetChildren world |> Seq.sortBy (fun child -> child.Name) |> Seq.toArray
                yield
                    { Address = address; Parent = parent; Name = entity.Name
                      Dispatcher = (entity.GetDispatcher world).GetType().Name
                      Id = string (entity.GetId world); Persistent = entity.GetPersistent world
                      Protection = string (entity.GetProtection world)
                      Children = children |> Array.map (fun child -> child.Name)
                      Original = Option.isSome original
                      Properties = names |> Seq.map (observeProperty properties entity world) |> Seq.toArray }
                yield! observeEntities address expected children world }

    let [<EntryPoint; STAThread>] main args =
        let mutable output = ""
        let mutable callbacks = 0
        let mutable captures = 0
        let mutable doneRunning = false
        let mutable savedMatches = false
        let mutable engineExit : int option = None
        let mutable lifecycleCounter = 0L
        let mutable phase = "startup"
        let mutable caseName = ""
        let mutable assignmentSha = ""
        let mutable setupWrites = 0
        let mutable operatorWrites = 0
        let mutable propagationCalls = 0
        let timer = Stopwatch.StartNew ()
        let boundaries = ResizeArray<Boundary> ()
        let labels = ResizeArray<string> ()
        try
            if args.Length <> 2 || not (List.contains args[0] ["L0"; "L1"]) then failwith "Expected arm and output directory."
            output <- Path.GetFullPath args[1]
            if not (Directory.Exists output) then failwith "Observation directory must already exist."
            let assignmentPath = Path.Combine (Directory.GetParent(output).FullName, "assignment.json")
            assignmentSha <- shaFile assignmentPath
            use assignment = JsonDocument.Parse (File.ReadAllText assignmentPath)
            let field (name : string) = assignment.RootElement.GetProperty(name).GetString ()
            caseName <- field "Case"
            let operator = field "Operator"
            let condition = field "Condition"
            let revise = args[0] = "L0"
            let cases = [|"P-shared"; "B-shared"; "P-local"; "B-local"|]
            if not (Array.contains caseName cases) || caseName <> operator + "-" + condition ||
               field "Arm" <> args[0] || field "Role" <> (if revise then "revise" else "reopen") ||
               field "ProtocolSha256" <> expectedProtocolSha ||
               assignment.RootElement.GetProperty("CaseOrdinal").GetInt32 () <> Array.findIndex ((=) caseName) cases + 1 then
                failwith "Invalid experiment assignment."
            Directory.SetCurrentDirectory AppContext.BaseDirectory
            if shaFile (Path.Combine (AppContext.BaseDirectory, "original-Scene.nugroup")) <> expectedSceneSha then
                failwith "Wrong fixed original scene."
            if shaFile typeof<World>.Assembly.Location <> expectedNuSha then failwith "Wrong loaded Nu.dll."
            Nu.init ()
            let original : GroupDescriptor = scvalue (File.ReadAllText "original-Scene.nugroup")
            let expected = originals "Game/Gameplay/Scene" original.EntityDescriptors |> Map.ofSeq
            if expected.Count <> 197 || original.EntityDescriptors.Length <> 19 then failwith "Wrong original descriptor structure."
            if family |> Array.exists (fun address -> not (expected.ContainsKey address)) then failwith "Wrong original palm family."
            let originalRows =
                expected |> Map.toArray |> Array.map (fun (address, node) ->
                    {| Address = address; Dispatcher = node.EntityDispatcherName
                       Children = node.EntityDescriptors |> List.map (EntityDescriptor.getNameOpt >> Option.get) |> List.toArray
                       Properties = node.EntityProperties |> Map.toArray |> Array.map (fun (name, value) -> {| Name = name; Symbol = Symbol.toString value |}) |})
            saveJson (Path.Combine (output, "original-expectations.json")) originalRows
            let windowConfig =
                { SdlWindowConfig.defaultConfig with
                    WindowTitle = "R12 Terra Firma material revision"
                    WindowFlags = SdlWindowConfig.defaultConfig.WindowFlags ||| SDL_WindowFlags.SDL_WINDOW_HIDDEN }
            let config =
                { WorldConfig.defaultConfig with
                    Imperative = false; Accompanied = true; Advancing = false
                    SdlConfig = { SdlConfig.defaultConfig with WindowConfig = windowConfig } }
            let windowSize = Nu.Constants.Render.DisplayVirtualResolution * Globals.Render.DisplayScalar
            let windowViewport = Viewport.makeWindow1 windowSize
            let geometryViewport = Viewport.makeGeometry windowViewport.Bounds.Size
            saveJson (Path.Combine (output, "startup.json"))
                {| Arm = args[0]; Case = caseName; AssignmentSha256 = assignmentSha
                   Runtime = RuntimeInformation.FrameworkDescription
                   OS = RuntimeInformation.OSDescription; ServerGC = GCSettings.IsServerGC
                   RequestedImperative = false; RequestedAccompanied = true; RequestedAdvancing = false
                   RequestedWindowFlags = string windowConfig.WindowFlags
                   DisplayScalar = Globals.Render.DisplayScalar
                   InputSceneSha256 = shaFile "Assets/Gameplay/Scene.nugroup"
                   OriginalSceneSha256 = expectedSceneSha; LoadedAssemblies = identities () |}
            use eventWriter = new StreamWriter (Path.Combine (output, "lifecycle.jsonl"), false)
            eventWriter.AutoFlush <- true
            let mark name =
                phase <- name
                boundaries.Add { Name = name; Callback = callbacks; Counter = lifecycleCounter; ElapsedSeconds = timer.Elapsed.TotalSeconds }
                saveJson (Path.Combine (output, "boundaries.json")) (boundaries.ToArray ())
            let record (data : LifeCycleEventData) (world : World) =
                // Increment independently before classification or observation, including other kinds.
                lifecycleCounter <- lifecycleCounter + 1L
                let kind, simulant =
                    match data with
                    | RegisterData simulant -> "register", simulant
                    | UnregisteringData simulant -> "unregister", simulant
                    | MountOptChangeData (_, _, entity) -> "mount", entity :> Simulant
                let mutable exists = false
                let mutable id = ""
                let mutable error = ""
                let isEntity = simulant :? Entity
                if isEntity then
                    try
                        let entity = simulant :?> Entity
                        exists <- entity.GetExists world
                        if exists then id <- string (entity.GetId world)
                    with failure -> error <- failure.ToString ()
                let row =
                    { Ordinal = lifecycleCounter; Callback = callbacks; Phase = phase; ElapsedSeconds = timer.Elapsed.TotalSeconds
                      Kind = kind; Address = string simulant; Entity = isEntity; Exists = exists; Id = id; Error = error }
                eventWriter.WriteLine (JsonSerializer.Serialize row)
                Cascade
            let pre world =
                callbacks <- callbacks + 1
                if callbacks = 1 then
                    mark "load"
                    World.subscribePlus<LifeCycleEventData, Game> 120018UL
                        (fun evt world -> record evt.Data world) (Game.LifeCycleEvent (nameof Entity)) Game world |> ignore
                    Game.SetGameState Gameplay world
            let capture label (world : World) =
                let entities = observeEntities "Game/Gameplay/Scene" expected (World.getEntitiesSovereign Simulants.GameplayScene world) world |> Seq.toArray
                let descriptor = World.writeGroup GroupDescriptor.empty Simulants.GameplayScene world
                File.WriteAllText (Path.Combine (output, label + ".nugroup"), scstring descriptor)
                // Exact current serialization for the two allowed advancing source histories.
                for address, suffix in [sourceAddress, "palm"; "Game/Gameplay/Scene/Villa", "villa"] do
                    let entity = entityAt address
                    if entity.GetExists world then
                        let current = World.writeEntity true true EntityDescriptor.empty entity world
                        File.WriteAllText (Path.Combine (output, label + "-" + suffix + ".nuentity"), scstring current)
                saveJson (Path.Combine (output, label + ".json"))
                    {| Label = label; Case = caseName; Callback = callbacks; Counter = lifecycleCounter
                       ElapsedSeconds = timer.Elapsed.TotalSeconds; Imperative = world.Imperative
                       Accompanied = world.Accompanied; Advancing = world.Advancing; Halted = world.Halted
                       UpdateTime = string world.UpdateTime; GameState = string (Game.GetGameState world)
                       GameplaySelected = Simulants.Gameplay.GetSelected world
                       WindowFlags = string (World.tryGetWindowFlags world)
                       WindowSize = string (World.getWindowSize world)
                       WindowViewport = string (World.getWindowViewport world)
                       GeometryViewport = string (World.getGeometryViewport world)
                       Entities = entities; LoadedAssemblies = identities () |}
                captures <- captures + 1
                labels.Add label
                entities, descriptor
            let checks = ResizeArray<Check> ()
            let check name passed = checks.Add { Name = name; Passed = passed }
            let requireChecks label =
                saveJson (Path.Combine (output, label + "-checks.json")) (checks.ToArray ())
                if checks |> Seq.exists (fun item -> not item.Passed) then failwith (label + " setup precondition failed; no assigned operation follows.")
            let stable name (before : EntityObservation array) (after : EntityObservation array) allowedMaterial =
                let old = before |> Array.map (fun row -> row.Address, row) |> Map.ofArray
                let current = after |> Array.map (fun row -> row.Address, row) |> Map.ofArray
                check (name + ":unique_nodes") (old.Count = before.Length && current.Count = after.Length)
                check (name + ":same_all_observed_addresses") (Set.ofSeq old.Keys = Set.ofSeq current.Keys)
                for KeyValue (address, first) in old do
                    match Map.tryFind address current with
                    | None -> ()
                    | Some next ->
                        check (name + ":" + address + ":metadata")
                            (first.Id = next.Id && first.Name = next.Name && first.Parent = next.Parent && first.Dispatcher = next.Dispatcher &&
                             first.Persistent = next.Persistent && first.Protection = next.Protection && first.Children = next.Children)
                        let props = next.Properties |> Array.map (fun prop -> prop.Name, prop) |> Map.ofArray
                        check (name + ":" + address + ":property_names") (Set.ofArray (first.Properties |> Array.map (fun prop -> prop.Name)) = Set.ofSeq props.Keys)
                        for prop in first.Properties do
                            match Map.tryFind prop.Name props with
                            | None -> ()
                            | Some actual ->
                                if not (prop.Name = "MaterialProperties" && address = allowedMaterial) then
                                    check (name + ":" + address + ":" + prop.Name)
                                        (prop.Error = "" && actual.Error = "" && prop.Found = actual.Found &&
                                         (not prop.Found || sameProperty prop.Name prop.Value actual.Value))
            let verifyReady (loaded : EntityObservation array) (ready : EntityObservation array) (world : World) =
                checks.Clear ()
                check "ready:mode" (not world.Imperative && world.Accompanied && not world.Advancing && world.Halted &&
                    string world.UpdateTime = "0" && Game.GetGameState world = Gameplay && Simulants.Gameplay.GetSelected world)
                let rows = ready |> Array.map (fun row -> row.Address, row) |> Map.ofArray
                check "ready:original_set" ((ready |> Array.filter (fun row -> row.Original) |> Array.map (fun row -> row.Address) |> Set.ofArray) = Set.ofSeq expected.Keys)
                for KeyValue (address, node) in expected do
                    match Map.tryFind address rows with
                    | None -> check ("ready:" + address + ":exists") false
                    | Some row ->
                        let currentChildren = row.Children |> Array.filter (fun name -> expected.ContainsKey (address + "/" + name)) |> Set.ofArray
                        let originalChildren = node.EntityDescriptors |> Seq.map (EntityDescriptor.getNameOpt >> Option.get) |> Set.ofSeq
                        check ("ready:" + address + ":correspondence")
                            (row.Parent = address.Substring(0, address.LastIndexOf '/') && row.Name = address.Substring(address.LastIndexOf '/' + 1) &&
                             row.Dispatcher = node.EntityDispatcherName && currentChildren = originalChildren)
                        for prop in row.Properties do
                            check ("ready:" + address + ":" + prop.Name + ":conversion") (prop.Error = "")
                            if prop.ExpectedPresent then
                                check ("ready:" + address + ":" + prop.Name + ":original")
                                    (prop.Found && sameProperty prop.Name prop.ExpectedSymbol prop.Value)
                            elif prop.Name = "PropagationSourceOpt" || prop.Name = "PropagatedDescriptorOpt" then
                                check ("ready:" + address + ":" + prop.Name + ":absent_original") (prop.Found && prop.Value = "None")
                stable "loaded_to_ready" loaded ready ""
                let source = entityAt sourceAddress
                let selection = Seq.append [source] (source.GetPropagationTargets world) |> Seq.map string |> Seq.toArray |> Array.sortWith (fun a b -> StringComparer.Ordinal.Compare (a, b))
                check "ready:public_family_selector" (selection = family)
                for address in family do
                    let entity = entityAt address
                    check ("ready:" + address + ":all_none_material") (entity.GetExists world && entity.GetMaterialProperties world = MaterialProperties.empty)
                saveJson (Path.Combine (output, "family-selection.json")) selection
                requireChecks "Ready"
                selection
            let mutable loadedRows : EntityObservation array = [||]
            let saveAndExit descriptor world =
                mark "save"
                let savedPath = Path.Combine (output, "saved-Scene.nugroup")
                World.writeGroupToFile savedPath Simulants.GameplayScene world
                let parsed : GroupDescriptor = scvalue (File.ReadAllText savedPath)
                File.WriteAllText (Path.Combine (output, "saved-canonical.nugroup"), scstring parsed)
                savedMatches <- scstring descriptor = scstring parsed
                doneRunning <- true
                mark "cleanup"
                World.exit world
            let post (world : World) =
                saveJson (Path.Combine (output, sprintf "phase-%03i.json" callbacks))
                    {| Callback = callbacks; SceneExists = Simulants.GameplayScene.GetExists world
                       GameplayExists = Simulants.Gameplay.GetExists world
                       GameState = string (Game.GetGameState world) |}
                if captures = 0 && Simulants.GameplayScene.GetExists world then
                    loadedRows <- capture (if revise then "Loaded" else "ReopenA") world |> fst
                    mark (if revise then "ready_wait" else "reopen_wait")
                elif captures = 1 && not revise then
                    let _, descriptor = capture "ReopenB" world
                    saveAndExit descriptor world
                elif captures = 1 then
                    let ready, _ = capture "Ready" world
                    let selection = verifyReady loadedRows ready world
                    mark "preparation"
                    if condition = "local" then
                        let target = entityAt localAddress
                        let material = target.GetMaterialProperties world
                        setupWrites <- setupWrites + 1
                        target.SetMaterialProperties { material with RoughnessOpt = ValueSome 0.75f } world
                    let prepared, _ = capture "Prepared" world
                    checks.Clear ()
                    stable "ready_to_prepared" ready prepared (if condition = "local" then localAddress else "")
                    for address in family do
                        let expectedMaterial =
                            if condition = "local" && address = localAddress then { MaterialProperties.empty with RoughnessOpt = ValueSome 0.75f }
                            else MaterialProperties.empty
                        check ("prepared:" + address + ":exact_material") ((entityAt address).GetMaterialProperties world = expectedMaterial)
                    requireChecks "Prepared"
                    mark "operator"
                    let tint (entity : Entity) =
                        let current = entity.GetMaterialProperties world
                        operatorWrites <- operatorWrites + 1
                        entity.SetMaterialProperties { current with AlbedoOpt = ValueSome (Color (0.25f, 0.5f, 0.75f, 1.0f)) } world
                    if operator = "P" then
                        let source = entityAt sourceAddress
                        tint source
                        propagationCalls <- propagationCalls + 1
                        World.propagateEntityStructure source world
                    else
                        for address in selection do tint (entityAt address)
                    mark "applied"
                    capture "Applied" world |> ignore
                    mark "settling"
                elif captures = 4 && revise then
                    let _, descriptor = capture "Settled" world
                    saveAndExit descriptor world
            let exitCode =
                World.runPlus (fun () -> None) (fun _ -> callbacks < 120 && not doneRunning)
                    pre ignore post ignore ignore config windowViewport.Outer.Size geometryViewport windowViewport (TerraFirmaPlugin ())
            engineExit <- Some exitCode
            mark "returned"
            eventWriter.Flush ()
            let complete = exitCode = 0 && captures = (if revise then 5 else 2) && doneRunning
            saveJson (Path.Combine (output, "summary.json"))
                {| Arm = args[0]; Case = caseName; AssignmentSha256 = assignmentSha
                   Complete = complete; CallbackCount = callbacks; CaptureCount = captures; Labels = labels.ToArray ()
                   EngineExitCode = exitCode; SavedDescriptorMatchesEndpoint = savedMatches
                   FinalLifecycleCounter = lifecycleCounter; SetupWrites = setupWrites; OperatorWrites = operatorWrites
                   PropagationCalls = propagationCalls; ElapsedSeconds = timer.Elapsed.TotalSeconds
                   LoadedAssemblies = identities (); ServerGC = GCSettings.IsServerGC |}
            if complete then 0 else 2
        with error ->
            if output <> "" && Directory.Exists output then
                saveJson (Path.Combine (output, "exception.json"))
                    {| Error = error.ToString (); CallbackCount = callbacks; CaptureCount = captures
                       EngineExit = string engineExit; Case = caseName; AssignmentSha256 = assignmentSha
                       Phase = phase; FinalLifecycleCounter = lifecycleCounter; SetupWrites = setupWrites
                       OperatorWrites = operatorWrites; PropagationCalls = propagationCalls |}
            Console.Error.WriteLine (error.ToString ())
            2
