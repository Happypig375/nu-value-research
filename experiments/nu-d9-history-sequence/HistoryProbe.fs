namespace TerraFirma
open System
open System.IO
open System.Numerics
open System.Text
open Prime
open Nu

// D9 direction 3 supplement probe (research only): replaces Terra Firma's Program.fs. Plain NuPlugin from this assembly;
// reuses the engine-made Gameplay screen; loads a scene group; runs a two-step revision sequence (PP, HP, HH or N) and
// snapshots every entity before and after each step, including Order and propagation history; saves after each step.
// Everything happens in one frame callback. Environment: PROBE_MODE op|reopen, PROBE_SEQ PP|HP|HH|N, PROBE_IN, PROBE_OUT,
// PROBE_TAG (reopen file name stem). Protocol: docs/nu-d9-history-sequence-2026-11-11.md.
type ResearchPlugin () =
    inherit NuPlugin ()

module Program =

    let private inv = Globalization.CultureInfo.InvariantCulture
    let private env name = Environment.GetEnvironmentVariable name
    let SourceAddress = "Game/Gameplay/Scene/Villa/Palm"
    let Tint = color 0.25f 0.5f 0.75f 1.0f
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

    let private entities (group : Group) world = World.getEntitiesDepthFirst group world |> Seq.toList

    let private propsJson (props : Map<string, Symbol>) =
        props |> Seq.map (fun (KeyValue (n, s)) -> "\"" + esc n + "\":\"" + esc (scstring s) + "\"") |> String.concat ","

    let private snapshot (group : Group) world =
        let parts =
            [for e in entities group world do
                let core = World.writeEntity false false EntityDescriptor.empty e world
                let full = World.writeEntity true true EntityDescriptor.empty e world
                let pick name = match Map.tryFind name full.EntityProperties with Some s -> "\"" + esc (scstring s) + "\"" | None -> "null"
                let source = match e.GetPropagationSourceOpt world with Some s -> "\"" + esc (string s.EntityAddress) + "\"" | None -> "null"
                yield "\"" + esc (string e.EntityAddress) + "\":{\"dispatcher\":\"" + esc core.EntityDispatcherName + "\",\"source\":" + source +
                      ",\"material\":" + defaultArg (materialJson e world) "null" +
                      ",\"order\":" + pick "Order" + ",\"history\":" + pick "PropagatedDescriptorOpt" +
                      ",\"props\":{" + propsJson core.EntityProperties + "}}"]
        "{" + String.concat "," parts + "}"

    let private setAlbedo (e : Entity) world =
        let mp = e.GetMaterialProperties world
        e.SetMaterialProperties { mp with AlbedoOpt = ValueSome Tint } world

    let private setRoughness (e : Entity) world =
        let mp = e.GetMaterialProperties world
        e.SetMaterialProperties { mp with RoughnessOpt = ValueSome Roughness } world

    let mutable private frame = 0
    let mutable private exitCode = 0

    let private run world =
        let mode, seq, input, out = env "PROBE_MODE", env "PROBE_SEQ", env "PROBE_IN", env "PROBE_OUT"
        let write (name : string) (text : string) = File.WriteAllText (Path.Combine (out, name), text)
        let existing = Game / "Gameplay"
        let screen = if existing.GetExists world then existing else World.createScreen<ScreenDispatcher> (Some "Gameplay") world
        if (screen / "Scene").GetExists world then World.destroyGroupImmediate (screen / "Scene") world
        let w = Diagnostics.Stopwatch.StartNew ()
        let group = World.readGroupFromFile input (Some "Scene") screen world
        let loadMs = w.Elapsed.TotalMilliseconds
        let all = entities group world
        let family =
            all
            |> List.filter (fun e -> string e.EntityAddress = SourceAddress ||
                                     (match e.GetPropagationSourceOpt world with Some s -> string s.EntityAddress = SourceAddress | None -> false))
            |> List.sortBy (fun e -> string e.EntityAddress)
        let familyJson = family |> List.map (fun e -> "\"" + esc (string e.EntityAddress) + "\"") |> String.concat ","
        if mode = "reopen" then
            write (env "PROBE_TAG" + ".json") (snapshot group world)
            write (env "PROBE_TAG" + "-probe.json") (String.Format (inv, "{{\"load_ms\":{0:R},\"entities\":{1},\"family\":[{2}]}}", loadMs, List.length all, familyJson))
        else
            write "before.json" (snapshot group world)
            let source = family |> List.find (fun e -> string e.EntityAddress = SourceAddress)
            let step useHelper setter =
                let w = Diagnostics.Stopwatch.StartNew ()
                if useHelper then for e in family do setter e world
                else
                    setter source world
                    World.propagateEntityStructure source world
                w.Elapsed.TotalMilliseconds
            let save name =
                let w = Diagnostics.Stopwatch.StartNew ()
                World.writeGroupToFile (Path.Combine (out, name)) group world
                w.Elapsed.TotalMilliseconds
            let mutable s1, s2, v1, v2 = 0.0, 0.0, 0.0, 0.0
            if seq <> "N" then
                s1 <- step (seq = "HP" || seq = "HH") setAlbedo
                write "after1.json" (snapshot group world)
                v1 <- save "saved1.nugroup"
                s2 <- step (seq = "HH") setRoughness
            write "after2.json" (snapshot group world)
            v2 <- save "saved2.nugroup"
            write "probe.json" (String.Format (inv, "{{\"seq\":\"{0}\",\"load_ms\":{1:R},\"step1_ms\":{2:R},\"step2_ms\":{3:R},\"save1_ms\":{4:R},\"save2_ms\":{5:R},\"entities\":{6},\"family\":[{7}]}}",
                                               seq, loadMs, s1, s2, v1, v2, List.length all, familyJson))

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
