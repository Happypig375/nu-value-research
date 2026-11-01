namespace R12MaterialIntent

open System
open System.Buffers
open System.Collections.Generic
open System.Globalization
open System.Security.Cryptography
open System.Text
open System.Text.Json

[<StructuralEquality; StructuralComparison>]
type Rgba =
    { R : single
      G : single
      B : single
      A : single }

[<StructuralEquality; StructuralComparison>]
type MaterialFields =
    { AlbedoOpt : Rgba option
      RoughnessOpt : single option }

[<StructuralEquality; StructuralComparison>]
type IntentMode =
    | Inherit
    | Pin

[<StructuralEquality; StructuralComparison>]
type FieldModes =
    { AlbedoMode : IntentMode
      RoughnessMode : IntentMode }

[<StructuralEquality; StructuralComparison>]
type IntentError =
    { Code : string
      Message : string }

type Policy private
    (sequence : string,
     generation : int64,
     sceneSha256 : string,
     source : string,
     members : Map<string, FieldModes>,
     extensionJson : Map<string, string>,
     memberExtensionJson : Map<string, Map<string, string>>) =

    member _.Sequence = sequence
    member _.Generation = generation
    member _.SceneSha256 = sceneSha256
    member _.Source = source
    member _.Members = members
    member _.ExtensionJson = extensionJson
    member _.MemberExtensionJson = memberExtensionJson

    static member internal Create (sequence, generation, sceneSha256, source, members, extensionJson, memberExtensionJson) =
        Policy (sequence, generation, sceneSha256, source, members, extensionJson, memberExtensionJson)

type Draft private (policy : Policy, materials : Map<string, MaterialFields>, members : Map<string, FieldModes>) =
    member _.Policy = policy
    member _.Materials = materials
    member _.Members = members

    static member internal Create (policy, materials, members) = Draft (policy, materials, members)

type BoundPolicy =
    { Policy : Policy
      Materials : Map<string, MaterialFields>
      CompanionUtf8 : byte array }

type Operation =
    | ReviseAlbedo of Rgba option
    | ReviseRoughness of single option
    | PinAlbedo of target : string * value : Rgba option
    | PinRoughness of target : string * value : single option
    | InheritAlbedo of target : string
    | InheritRoughness of target : string

[<RequireQualifiedAccess>]
module MaterialIntent =

    [<Literal>]
    let Schema = "r12-material-intent/v1"

    let private requiredRootKeys =
        set ["schema"; "sequence"; "generation"; "scene_sha256"; "source"; "members"]

    let private error (code : string) (message : string) : Result<'a, IntentError> = Error { Code = code; Message = message }

    let private isFiniteSingle (value : single) = Single.IsFinite value

    let private validateAlbedo (value : Rgba option) =
        match value with
        | None -> Ok ()
        | Some value when
            isFiniteSingle value.R && isFiniteSingle value.G &&
            isFiniteSingle value.B && isFiniteSingle value.A -> Ok ()
        | Some _ -> error "nonfinite_material" "Albedo contains a nonfinite component."

    let private validateRoughness (value : single option) =
        match value with
        | None -> Ok ()
        | Some value when isFiniteSingle value -> Ok ()
        | Some _ -> error "nonfinite_material" "Roughness is nonfinite."

    let private validateMaterial (material : MaterialFields) =
        match validateAlbedo material.AlbedoOpt with
        | Error error -> Error error
        | Ok () -> validateRoughness material.RoughnessOpt

    let private validateFamily (source : string) (family : string seq) =
        if String.IsNullOrWhiteSpace source then error "invalid_source" "Source must be nonempty."
        elif isNull (box family) then error "invalid_family" "Family must be supplied."
        else
            let values = Seq.toArray family
            if values.Length = 0 then error "invalid_family" "Family must be nonempty."
            elif Array.exists String.IsNullOrWhiteSpace values then error "invalid_family" "Family addresses must be nonempty."
            elif (Set.ofArray values).Count <> values.Length then error "invalid_family" "Family addresses must be unique."
            elif Array.sumBy (fun value -> if String.Equals (value, source, StringComparison.Ordinal) then 1 else 0) values <> 1 then
                error "invalid_family" "Source must occur exactly once in the family."
            else Ok (Set.ofArray values)

    let private validateMaterials (family : Set<string>) (materials : Map<string, MaterialFields>) =
        if isNull (box materials) then error "invalid_material_roster" "Material map must be supplied."
        elif (materials |> Map.toSeq |> Seq.map fst |> Set.ofSeq) <> family then
            error "invalid_material_roster" "Material map keys must exactly equal the family."
        else
            materials
            |> Map.toSeq
            |> Seq.tryPick (fun (address, material) ->
                match validateMaterial material with
                | Ok () -> None
                | Error detail -> Some { detail with Message = address + ": " + detail.Message })
            |> function
                | Some detail -> Error detail
                | None -> Ok ()

    let private sha256 (bytes : byte array) =
        SHA256.HashData bytes |> Convert.ToHexString |> fun value -> value.ToLowerInvariant ()

    let private validateSceneBytes (sceneBytes : byte array) =
        if isNull sceneBytes then error "invalid_scene_bytes" "Exact scene bytes must be supplied."
        else Ok (sha256 sceneBytes)

    let private validateNoDuplicateKeys (jsonUtf8 : byte array) =
        if isNull jsonUtf8 then error "invalid_json" "Companion JSON bytes must be supplied."
        else
            try
                let options = JsonReaderOptions (AllowTrailingCommas = false, CommentHandling = JsonCommentHandling.Disallow)
                let mutable reader = Utf8JsonReader (ReadOnlySpan<byte> jsonUtf8, options)
                let stack = ResizeArray<HashSet<string> option> ()
                let mutable duplicate : string option = None
                while duplicate.IsNone && reader.Read () do
                    match reader.TokenType with
                    | JsonTokenType.StartObject -> stack.Add (Some (HashSet<string> StringComparer.Ordinal))
                    | JsonTokenType.StartArray -> stack.Add None
                    | JsonTokenType.EndObject
                    | JsonTokenType.EndArray ->
                        if stack.Count > 0 then stack.RemoveAt (stack.Count - 1)
                    | JsonTokenType.PropertyName ->
                        if stack.Count = 0 then duplicate <- Some "Property outside an object."
                        else
                            match stack[stack.Count - 1] with
                            | Some names ->
                                let name = reader.GetString ()
                                if not (names.Add name) then duplicate <- Some ("Duplicate JSON key '" + name + "'.")
                            | None -> duplicate <- Some "Property inside an array."
                    | _ -> ()
                match duplicate with
                | Some message -> error "duplicate_json_key" message
                | None -> Ok ()
            with
            | :? JsonException as ex -> error "invalid_json" ex.Message
            | :? ArgumentException as ex -> error "invalid_json" ex.Message

    let private tryRequiredProperty (name : string) (root : JsonElement) =
        match root.TryGetProperty name with
        | true, value -> Ok value
        | false, _ -> error "missing_metadata" ("Missing required JSON key '" + name + "'.")

    let private readRequiredString (name : string) (root : JsonElement) =
        match tryRequiredProperty name root with
        | Error detail -> Error detail
        | Ok value when value.ValueKind = JsonValueKind.String ->
            let text = value.GetString ()
            if isNull text then error "wrong_metadata_type" (name + " must be a string.") else Ok text
        | Ok _ -> error "wrong_metadata_type" (name + " must be a string.")

    let private parseMode (address : string) (fieldName : string) (value : JsonElement) =
        if value.ValueKind <> JsonValueKind.String then
            error "wrong_metadata_type" (address + ": " + fieldName + " mode must be a string.")
        else
            match value.GetString () with
            | "inherit" -> Ok Inherit
            | "pin" -> Ok Pin
            | mode -> error "unsupported_mode" (address + ": unsupported " + fieldName + " mode '" + string mode + "'.")

    let private parseMembers (targets : Set<string>) (root : JsonElement) =
        match tryRequiredProperty "members" root with
        | Error detail -> Error detail
        | Ok members when members.ValueKind <> JsonValueKind.Object ->
            error "wrong_metadata_type" "members must be an object."
        | Ok members ->
            let suppliedTargets = members.EnumerateObject () |> Seq.map (fun property -> property.Name) |> Set.ofSeq
            if suppliedTargets <> targets then error "invalid_target_roster" "Member keys must exactly equal family minus source."
            else
                let mutable failure : IntentError option = None
                let mutable parsed : Map<string, FieldModes> = Map.empty
                let mutable extensions : Map<string, Map<string, string>> = Map.empty
                for memberProperty in members.EnumerateObject () do
                    if failure.IsNone then
                        if memberProperty.Value.ValueKind <> JsonValueKind.Object then
                            failure <- Some { Code = "wrong_metadata_type"; Message = memberProperty.Name + ": member value must be an object." }
                        else
                            let fields = memberProperty.Value.EnumerateObject () |> Seq.map (fun property -> property.Name) |> Set.ofSeq
                            if not (fields.Contains "AlbedoOpt" && fields.Contains "RoughnessOpt") then
                                failure <- Some { Code = "invalid_material_keys"; Message = memberProperty.Name + ": both managed mode keys are required." }
                            else
                                let albedo = memberProperty.Value.GetProperty "AlbedoOpt" |> parseMode memberProperty.Name "AlbedoOpt"
                                let roughness = memberProperty.Value.GetProperty "RoughnessOpt" |> parseMode memberProperty.Name "RoughnessOpt"
                                match albedo, roughness with
                                | Ok albedo, Ok roughness ->
                                    parsed <- Map.add memberProperty.Name { AlbedoMode = albedo; RoughnessMode = roughness } parsed
                                    let memberExtensions =
                                        memberProperty.Value.EnumerateObject ()
                                        |> Seq.filter (fun property -> property.Name <> "AlbedoOpt" && property.Name <> "RoughnessOpt")
                                        |> Seq.map (fun property -> property.Name, property.Value.GetRawText ())
                                        |> Map.ofSeq
                                    extensions <- Map.add memberProperty.Name memberExtensions extensions
                                | Error detail, _
                                | _, Error detail -> failure <- Some detail
                match failure with
                | Some detail -> Error detail
                | None -> Ok (parsed, extensions)

    let private parseDocument (expectedSequence : string) (expectedGeneration : int64) (expectedSource : string) (family : Set<string>) (sceneSha : string) (jsonUtf8 : byte array) =
        match validateNoDuplicateKeys jsonUtf8 with
        | Error detail -> Error detail
        | Ok () ->
            try
                use document = JsonDocument.Parse (ReadOnlyMemory<byte> jsonUtf8)
                let root = document.RootElement
                if root.ValueKind <> JsonValueKind.Object then error "wrong_metadata_type" "Companion root must be an object."
                else
                    let schema = readRequiredString "schema" root
                    let sequence = readRequiredString "sequence" root
                    let hash = readRequiredString "scene_sha256" root
                    let source = readRequiredString "source" root
                    let generation =
                        match tryRequiredProperty "generation" root with
                        | Error detail -> Error detail
                        | Ok value when value.ValueKind = JsonValueKind.Number ->
                            match value.TryGetInt64 () with
                            | true, number when number >= 0L -> Ok number
                            | true, _ -> error "invalid_generation" "generation must be nonnegative."
                            | false, _ -> error "invalid_generation" "generation must be an integral Int64 value."
                        | Ok _ -> error "wrong_metadata_type" "generation must be a number."
                    match schema, sequence, generation, hash, source with
                    | Ok schema, Ok sequence, Ok generation, Ok hash, Ok source ->
                        if schema <> Schema then error "unsupported_schema" "Unsupported companion schema."
                        elif String.IsNullOrWhiteSpace sequence then error "invalid_sequence" "Sequence identity must be nonempty."
                        elif sequence <> expectedSequence then error "sequence_mismatch" "Companion sequence does not match the expected sequence."
                        elif generation <> expectedGeneration then error "generation_mismatch" "Companion generation does not match the expected generation."
                        elif source <> expectedSource then error "source_mismatch" "Companion source does not match the expected source."
                        elif hash.Length <> 64 || (hash |> Seq.exists (fun c -> not ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f')))) then
                            error "invalid_scene_hash" "scene_sha256 must be 64 lower-case hexadecimal characters."
                        elif hash <> sceneSha then error "scene_hash_mismatch" "Companion is not bound to the supplied exact scene bytes."
                        else
                            let targets = Set.remove expectedSource family
                            match parseMembers targets root with
                            | Error detail -> Error detail
                            | Ok (members, memberExtensions) ->
                                let extensions =
                                    root.EnumerateObject ()
                                    |> Seq.filter (fun property -> not (requiredRootKeys.Contains property.Name))
                                    |> Seq.map (fun property -> property.Name, property.Value.GetRawText ())
                                    |> Map.ofSeq
                                Ok (Policy.Create (sequence, generation, hash, source, members, extensions, memberExtensions))
                    | Error detail, _, _, _, _
                    | _, Error detail, _, _, _
                    | _, _, Error detail, _, _
                    | _, _, _, Error detail, _
                    | _, _, _, _, Error detail -> Error detail
            with
            | :? JsonException as ex -> error "invalid_json" ex.Message
            | :? InvalidOperationException as ex -> error "invalid_json" ex.Message

    let private writeMode (writer : Utf8JsonWriter) (name : string) (mode : IntentMode) =
        writer.WriteString (name, match mode with Inherit -> "inherit" | Pin -> "pin")

    let serializeUtf8 (policy : Policy) : byte array =
        let buffer = ArrayBufferWriter<byte> ()
        use writer = new Utf8JsonWriter (buffer, JsonWriterOptions (Indented = true))
        writer.WriteStartObject ()
        writer.WriteString ("schema", Schema)
        writer.WriteString ("sequence", policy.Sequence)
        writer.WriteNumber ("generation", policy.Generation)
        writer.WriteString ("scene_sha256", policy.SceneSha256)
        writer.WriteString ("source", policy.Source)
        writer.WritePropertyName "members"
        writer.WriteStartObject ()
        for KeyValue (address, modes) in policy.Members do
            writer.WritePropertyName address
            writer.WriteStartObject ()
            writeMode writer "AlbedoOpt" modes.AlbedoMode
            writeMode writer "RoughnessOpt" modes.RoughnessMode
            match Map.tryFind address policy.MemberExtensionJson with
            | Some extensions ->
                for KeyValue (name, rawJson) in extensions do
                    writer.WritePropertyName name
                    writer.WriteRawValue (rawJson, false)
            | None -> ()
            writer.WriteEndObject ()
        writer.WriteEndObject ()
        for KeyValue (name, rawJson) in policy.ExtensionJson do
            writer.WritePropertyName name
            writer.WriteRawValue (rawJson, false)
        writer.WriteEndObject ()
        writer.Flush ()
        buffer.WrittenSpan.ToArray ()

    let initialize (sequence : string) (source : string) (family : string seq) (sceneBytes : byte array) (materials : Map<string, MaterialFields>) =
        if String.IsNullOrWhiteSpace sequence then error "invalid_sequence" "Sequence identity must be nonempty."
        else
            match validateFamily source family with
            | Error detail -> Error detail
            | Ok family ->
                match validateMaterials family materials, validateSceneBytes sceneBytes with
                | Ok (), Ok sceneSha ->
                    let inherited = { AlbedoMode = Inherit; RoughnessMode = Inherit }
                    let members = family |> Set.remove source |> Seq.map (fun address -> address, inherited) |> Map.ofSeq
                    let memberExtensions = members |> Map.map (fun _ _ -> Map.empty)
                    Ok (Policy.Create (sequence, 0L, sceneSha, source, members, Map.empty, memberExtensions))
                | Error detail, _
                | _, Error detail -> Error detail

    let load (expectedSequence : string) (expectedGeneration : int64) (expectedSource : string) (family : string seq) (sceneBytes : byte array) (materials : Map<string, MaterialFields>) (jsonUtf8 : byte array) =
        if String.IsNullOrWhiteSpace expectedSequence then error "invalid_sequence" "Expected sequence must be nonempty."
        elif expectedGeneration < 0L then error "invalid_generation" "Expected generation must be nonnegative."
        else
            match validateFamily expectedSource family with
            | Error detail -> Error detail
            | Ok family ->
                match validateMaterials family materials, validateSceneBytes sceneBytes with
                | Ok (), Ok sceneSha -> parseDocument expectedSequence expectedGeneration expectedSource family sceneSha jsonUtf8
                | Error detail, _
                | _, Error detail -> Error detail

    let prepare (policy : Policy) (materials : Map<string, MaterialFields>) =
        let family = policy.Members |> Map.toSeq |> Seq.map fst |> Set.ofSeq |> Set.add policy.Source
        match validateMaterials family materials with
        | Error detail -> Error detail
        | Ok () -> Ok (Draft.Create (policy, materials, policy.Members))

    let private validateTarget (target : string) (draft : Draft) =
        if String.Equals (target, draft.Policy.Source, StringComparison.Ordinal) then
            error "invalid_target" "Pin and inherit operations cannot target the source."
        elif not (draft.Members.ContainsKey target) then error "invalid_target" "Unknown target."
        else Ok ()

    let private setAlbedo (address : string) (value : Rgba option) (materials : Map<string, MaterialFields>) =
        let material = Map.find address materials
        Map.add address { material with AlbedoOpt = value } materials

    let private setRoughness (address : string) (value : single option) (materials : Map<string, MaterialFields>) =
        let material = Map.find address materials
        Map.add address { material with RoughnessOpt = value } materials

    let apply (operation : Operation) (draft : Draft) =
        match operation with
        | ReviseAlbedo value ->
            match validateAlbedo value with
            | Error detail -> Error detail
            | Ok () ->
                let materials = setAlbedo draft.Policy.Source value draft.Materials
                let materials =
                    draft.Members
                    |> Map.fold (fun state address modes -> if modes.AlbedoMode = Inherit then setAlbedo address value state else state) materials
                Ok (Draft.Create (draft.Policy, materials, draft.Members))
        | ReviseRoughness value ->
            match validateRoughness value with
            | Error detail -> Error detail
            | Ok () ->
                let materials = setRoughness draft.Policy.Source value draft.Materials
                let materials =
                    draft.Members
                    |> Map.fold (fun state address modes -> if modes.RoughnessMode = Inherit then setRoughness address value state else state) materials
                Ok (Draft.Create (draft.Policy, materials, draft.Members))
        | PinAlbedo (target, value) ->
            match validateTarget target draft, validateAlbedo value with
            | Ok (), Ok () ->
                let mode = Map.find target draft.Members
                let members = Map.add target { mode with AlbedoMode = Pin } draft.Members
                Ok (Draft.Create (draft.Policy, setAlbedo target value draft.Materials, members))
            | Error detail, _
            | _, Error detail -> Error detail
        | PinRoughness (target, value) ->
            match validateTarget target draft, validateRoughness value with
            | Ok (), Ok () ->
                let mode = Map.find target draft.Members
                let members = Map.add target { mode with RoughnessMode = Pin } draft.Members
                Ok (Draft.Create (draft.Policy, setRoughness target value draft.Materials, members))
            | Error detail, _
            | _, Error detail -> Error detail
        | InheritAlbedo target ->
            match validateTarget target draft with
            | Error detail -> Error detail
            | Ok () ->
                let source = Map.find draft.Policy.Source draft.Materials
                let mode = Map.find target draft.Members
                let members = Map.add target { mode with AlbedoMode = Inherit } draft.Members
                Ok (Draft.Create (draft.Policy, setAlbedo target source.AlbedoOpt draft.Materials, members))
        | InheritRoughness target ->
            match validateTarget target draft with
            | Error detail -> Error detail
            | Ok () ->
                let source = Map.find draft.Policy.Source draft.Materials
                let mode = Map.find target draft.Members
                let members = Map.add target { mode with RoughnessMode = Inherit } draft.Members
                Ok (Draft.Create (draft.Policy, setRoughness target source.RoughnessOpt draft.Materials, members))

    let applyMany (operations : Operation seq) (draft : Draft) =
        (Ok draft, operations)
        ||> Seq.fold (fun state operation ->
            match state with
            | Error detail -> Error detail
            | Ok draft -> apply operation draft)

    let bind (savedSceneBytes : byte array) (draft : Draft) =
        if draft.Policy.Generation = Int64.MaxValue then error "generation_overflow" "Generation cannot advance beyond Int64.MaxValue."
        else
            match validateSceneBytes savedSceneBytes with
            | Error detail -> Error detail
            | Ok sceneSha ->
                let policy =
                    Policy.Create
                        (draft.Policy.Sequence,
                         draft.Policy.Generation + 1L,
                         sceneSha,
                         draft.Policy.Source,
                         draft.Members,
                         draft.Policy.ExtensionJson,
                         draft.Policy.MemberExtensionJson)
                Ok { Policy = policy; Materials = draft.Materials; CompanionUtf8 = serializeUtf8 policy }
