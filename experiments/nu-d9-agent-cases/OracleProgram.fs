namespace Breakout
open System
open System.IO
open System.Text
open Prime
open Nu

// D9 direction 4 behavioural oracle: replaces Breakout Mmcc's Program.fs for scoring only. It runs the game exactly
// as World.run does, plus a read-only per-frame observer (the run loop's postProcess callback) that writes one JSON
// line per frame to the file named by ORACLE_TRACE: the selected screen and, on the Gameplay screen, the Paddle,
// Ball, Message, Score and Quit entities found by name in any group, plus the count of entities and of Life+ icons.
// It never changes the world. Protocol: docs/nu-d9-agent-cases-2026-11-11.md.
module Program =

    let mutable private writer : StreamWriter = null
    let private inv = Globalization.CultureInfo.InvariantCulture

    let private esc (s : string) =
        let sb = StringBuilder ()
        for c in s do
            match c with
            | '"' -> sb.Append "\\\"" |> ignore
            | '\\' -> sb.Append "\\\\" |> ignore
            | c when c < ' ' -> sb.AppendFormat ("\\u{0:x4}", int c) |> ignore
            | c -> sb.Append c |> ignore
        sb.ToString ()

    let private observe (world : World) =
        if isNull writer then
            let path = Environment.GetEnvironmentVariable "ORACLE_TRACE"
            if not (String.IsNullOrEmpty path) then
                writer <- new StreamWriter (path, false)
                writer.AutoFlush <- true
        if not (isNull writer) then
            let sb = StringBuilder ()
            let screen = match World.getSelectedScreenOpt world with Some s -> s.Name | None -> ""
            sb.Append("{\"u\":").Append(world.UpdateTime).Append(",\"ms\":").Append(Environment.TickCount64)
              .Append(",\"screen\":\"").Append(esc screen).Append('"') |> ignore
            if Simulants.Gameplay.GetExists world then
                let entities = [for g in World.getGroups Simulants.Gameplay world do yield! World.getEntities g world]
                let find name = List.tryFind (fun (e : Entity) -> e.Name = name) entities
                let pos name =
                    match find name with
                    | Some e -> String.Format (inv, "[{0:R},{1:R}]", e.GetPosition(world).X, e.GetPosition(world).Y)
                    | None -> "null"
                let text name =
                    match find name with
                    | Some e -> (try "\"" + esc (e.GetText world) + "\"" with _ -> "\"<no text>\"")
                    | None -> "null"
                let lives = entities |> List.filter (fun e -> e.Name.StartsWith "Life+") |> List.length
                sb.Append(",\"paddle\":").Append(pos "Paddle").Append(",\"ball\":").Append(pos "Ball")
                  .Append(",\"message\":").Append(text "Message").Append(",\"score\":").Append(text "Score")
                  .Append(",\"quit\":").Append(pos "Quit").Append(",\"lives\":").Append(lives)
                  .Append(",\"entities\":").Append(List.length entities) |> ignore
            sb.Append '}' |> ignore
            writer.WriteLine (sb.ToString ())

    let [<EntryPoint; STAThread>] main _ =
        Directory.SetCurrentDirectory AppContext.BaseDirectory
        Nu.init ()
        let sdlWindowConfig = { SdlWindowConfig.defaultConfig with WindowTitle = "Breakout Mmcc" }
        let sdlConfig = { SdlConfig.defaultConfig with WindowConfig = sdlWindowConfig }
        let worldConfig = { WorldConfig.defaultConfig with SdlConfig = sdlConfig }
        // the same arguments World.run passes, with the observer as postProcess
        let windowSize = Constants.Render.DisplayVirtualResolution * Globals.Render.DisplayScalar
        let windowViewport = Viewport.makeWindow1 windowSize
        let geometryViewport = Viewport.makeGeometry windowViewport.Bounds.Size
        World.runPlus
            (constant None) tautology ignore ignore observe ignore ignore ignore
            worldConfig windowViewport.Outer.Size geometryViewport windowViewport (BreakoutPlugin ())
