namespace TerraFirma
open System
open System.IO
open System.Numerics
open System.Text
open Prime
open Nu

// D9 direction 3 probe (research only): replaces Terra Firma's Program.fs. It runs a plain NuPlugin from this same
// assembly (so Terra Firma's dispatchers are available, but the game's own screen flow does not run), loads a
// Terra Firma scene group, applies one revision task by one route, records every entity's saved properties before
// and after, saves the group, and exits. Everything happens inside one frame callback, so no game time passes.
// Environment: PROBE_MODE op|reopen, PROBE_TASK T1|T2|T3|NONE, PROBE_COND P|O|N, PROBE_IN (group file),
// PROBE_OUT (folder). Protocol: docs/nu-d9-content-revision-2026-11-11.md.
type ResearchPlugin () =
    inherit NuPlugin ()

module Program =

    let private inv = Globalization.CultureInfo.InvariantCulture
    let private env name = Environment.GetEnvironmentVariable name
    let SourceAddress = "Game/Gameplay/Scene/Villa/Palm"
    let Tint = color 0.25f 0.5f 0.75f 1.0f
    let LocalTint = color 1.0f 0.0f 0.0f 1.0f
    let Roughness = 0.75f

    let private esc (s : string) =
        let sb = StringBuilder ()
        for c in s do
            match c with
            | '"' -> sb.Append "\\\"" |> ignore
            | '\\' -> sb.Append "\\\\" |> ignore
            | c when c < ' ' -> sb.AppendFormat ("\\u{0:x4}", int c) |> ignore
            | c -> sb.Append c |> ignore
        sb.ToString ()

    let private colorJson (c : Color) = String.Format (inv, "[{0:R},{1:R},{2:R},{3:R}]", c.R, c.G, c.B, c.A)

    let private materialJson (entity : Entity) world =
        try
            let mp = entity.GetMaterialProperties world
            let albedo = match mp.AlbedoOpt with ValueSome c -> colorJson c | ValueNone -> "null"
            let rough = match mp.RoughnessOpt with ValueSome r -> r.ToString ("R", inv) | ValueNone -> "null"
            Some (String.Format ("{{\"albedo\":{0},\"roughness\":{1},\"record\":\"{2}\"}}", albedo, rough, esc (scstring mp)))
        with _ -> None

    let private entities (group : Group) world =
        World.getEntitiesDepthFirst group world |> Seq.toList

    /// One JSON object: address -> dispatcher, propagation source, material fields and every saved property.
    let private snapshot (group : Group) world =
        let sb = StringBuilder ()
        sb.Append '{' |> ignore
        let mutable first = true
        for e in entities group world do
            if not first then sb.Append ',' |> ignore
            first <- false
            let descriptor = World.writeEntity false false EntityDescriptor.empty e world
            let source = match e.GetPropagationSourceOpt world with Some s -> "\"" + esc (string s.EntityAddress) + "\"" | None -> "null"
            sb.Append('"').Append(esc (string e.EntityAddress)).Append("\":{\"dispatcher\":\"")
              .Append(esc descriptor.EntityDispatcherName).Append("\",\"source\":").Append(source)
              .Append(",\"material\":").Append(defaultArg (materialJson e world) "null").Append(",\"props\":{") |> ignore
            let mutable firstProp = true
            for KeyValue (name, symbol) in descriptor.EntityProperties do
                if not firstProp then sb.Append ',' |> ignore
                firstProp <- false
                sb.Append('"').Append(esc name).Append("\":\"").Append(esc (scstring symbol)).Append('"') |> ignore
            sb.Append "}}" |> ignore
        sb.Append '}' |> ignore
        sb.ToString ()

    let private setAlbedo value (e : Entity) world =
        let mp = e.GetMaterialProperties world
        e.SetMaterialProperties { mp with AlbedoOpt = ValueSome value } world

    let private setRoughness value (e : Entity) world =
        let mp = e.GetMaterialProperties world
        e.SetMaterialProperties { mp with RoughnessOpt = ValueSome value } world

    let mutable private frame = 0
    let mutable private exitCode = 0

    let private run world =
        let mode, task, cond, input, out = env "PROBE_MODE", env "PROBE_TASK", env "PROBE_COND", env "PROBE_IN", env "PROBE_OUT"
        let write (name : string) (text : string) = File.WriteAllText (Path.Combine (out, name), text)
        let screen = World.createScreen<ScreenDispatcher> (Some "Gameplay") world
        let watch = Diagnostics.Stopwatch.StartNew ()
        let group = World.readGroupFromFile input (Some "Scene") screen world
        let loadMs = watch.Elapsed.TotalMilliseconds
        let all = entities group world
        let source = all |> List.tryFind (fun e -> string e.EntityAddress = SourceAddress)
        let family =
            all
            |> List.filter (fun e -> string e.EntityAddress = SourceAddress ||
                                     (match e.GetPropagationSourceOpt world with Some s -> string s.EntityAddress = SourceAddress | None -> false))
            |> List.sortBy (fun e -> string e.EntityAddress)
        let localOpt =
            family |> List.tryFind (fun e -> (string e.EntityAddress).Contains "/Villa-0002/")
        let familyJson = family |> List.map (fun e -> "\"" + esc (string e.EntityAddress) + "\"") |> String.concat ","
        let localJson = match localOpt with Some e -> "\"" + esc (string e.EntityAddress) + "\"" | None -> "null"
        if mode = "reopen" then
            write "reopen.json" (snapshot group world)
            write "probe.json" (String.Format (inv, "{{\"mode\":\"reopen\",\"load_ms\":{0:R},\"entities\":{1},\"family\":[{2}],\"local\":{3}}}",
                                               loadMs, List.length all, familyJson, localJson))
        else
            write "before.json" (snapshot group world)
            let mutable prepMs, opMs, note = 0.0, 0.0, ""
            match source, localOpt with
            | Some source, Some local ->
                // preparation (same in both conditions): the local palm gets a local tint (T2, T3)
                let w = Diagnostics.Stopwatch.StartNew ()
                if task = "T2" || task = "T3" then setAlbedo LocalTint local world
                prepMs <- w.Elapsed.TotalMilliseconds
                write "prepared.json" (snapshot group world)
                let w = Diagnostics.Stopwatch.StartNew ()
                match cond with
                | "P" ->
                    // Nu's route: edit the source palm, then propagate its structure to the family
                    if task = "T1" || task = "T2" then setAlbedo Tint source world
                    elif task = "T3" then setRoughness Roughness source world
                    World.propagateEntityStructure source world
                | "O" ->
                    // ordinary helper: set the one field on every family member, skipping the declared local keeps
                    let keepAlbedo = if task = "T2" then Set.singleton (string local.EntityAddress) else Set.empty
                    for e in family do
                        if task = "T1" || task = "T2" then
                            if not (keepAlbedo.Contains (string e.EntityAddress)) then setAlbedo Tint e world
                        elif task = "T3" then setRoughness Roughness e world
                | _ -> ()
                opMs <- w.Elapsed.TotalMilliseconds
            | _ ->
                note <- "source or local palm not found"
                exitCode <- 3
            write "after.json" (snapshot group world)
            let w = Diagnostics.Stopwatch.StartNew ()
            World.writeGroupToFile (Path.Combine (out, "saved.nugroup")) group world
            let saveMs = w.Elapsed.TotalMilliseconds
            write "probe.json" (String.Format (inv, "{{\"mode\":\"op\",\"task\":\"{0}\",\"cond\":\"{1}\",\"load_ms\":{2:R},\"prep_ms\":{3:R},\"op_ms\":{4:R},\"save_ms\":{5:R},\"entities\":{6},\"family\":[{7}],\"local\":{8},\"note\":\"{9}\"}}",
                                               task, cond, loadMs, prepMs, opMs, saveMs, List.length all, familyJson, localJson, note))

    let private perProcess world =
        frame <- inc frame
        if frame = 3 then
            try run world
            with exn ->
                exitCode <- 4
                File.WriteAllText (Path.Combine (env "PROBE_OUT", "probe-error.txt"), string exn)
            World.exit world

    let [<EntryPoint; STAThread>] main _ =
        Directory.SetCurrentDirectory AppContext.BaseDirectory
        Nu.init ()
        let sdlWindowConfig = { SdlWindowConfig.defaultConfig with WindowTitle = "Terra Firma research probe" }
        let sdlConfig = { SdlConfig.defaultConfig with WindowConfig = sdlWindowConfig }
        let worldConfig = { WorldConfig.defaultConfig with SdlConfig = sdlConfig }
        let windowSize = Constants.Render.DisplayVirtualResolution * Globals.Render.DisplayScalar
        let windowViewport = Viewport.makeWindow1 windowSize
        let geometryViewport = Viewport.makeGeometry windowViewport.Bounds.Size
        let code =
            World.runPlus
                (constant None) tautology ignore perProcess ignore ignore ignore ignore
                worldConfig windowViewport.Outer.Size geometryViewport windowViewport (ResearchPlugin ())
        if exitCode <> 0 then exitCode else code
