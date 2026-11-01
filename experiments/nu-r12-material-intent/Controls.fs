namespace R12MaterialIntent

open System
open System.Text
open System.Text.Json.Nodes

module Controls =

    let private source = "Game/Gameplay/Scene/Villa/Palm"
    let private local = "Game/Gameplay/Scene/Villa-0002/Palm-0009"
    let private sequence = "terra-firma-32-palms-five-stage-v1"

    let private palmNames =
        [|"Palm"; "Palm-0009"; "Palm-0010"; "Palm-0011"; "Palm-0012"; "Palm-0013"; "Palm-0014"; "Palm-0016"|]

    let private family =
        [|for villa in [|"Villa"; "Villa-0002"; "Villa-0003"; "Villa-0004"|] do
              for palm in palmNames do yield "Game/Gameplay/Scene/" + villa + "/" + palm|]

    let private noneMaterial : MaterialFields = { AlbedoOpt = None; RoughnessOpt = None }
    let private initialMaterials : Map<string, MaterialFields> = family |> Array.map (fun address -> address, noneMaterial) |> Map.ofArray
    let private a : Rgba = { R = 0.25f; G = 0.5f; B = 0.75f; A = 1.0f }
    let private b : Rgba = { R = 0.75f; G = 0.5f; B = 0.25f; A = 1.0f }
    let private c : Rgba = { R = 0.5f; G = 0.25f; B = 0.75f; A = 1.0f }

    let mutable private positiveCount = 0
    let mutable private rejectionCount = 0

    let private fail name detail = raise (InvalidOperationException (name + ": " + detail))

    let private check name condition =
        if not condition then fail name "assertion failed"
        positiveCount <- positiveCount + 1
        printfn "PASS %s" name

    let private ok name result =
        match result with
        | Ok value -> value
        | Error detail -> fail name (detail.Code + ": " + detail.Message)

    let private rejects name expectedCode result =
        match result with
        | Error detail when expectedCode = "*" || detail.Code = expectedCode ->
            rejectionCount <- rejectionCount + 1
            printfn "EXPECTED_REJECTION PASS %s [%s]" name detail.Code
        | Error detail -> fail name ("expected " + expectedCode + ", got " + detail.Code + ": " + detail.Message)
        | Ok _ -> fail name "unexpectedly accepted"

    let private bytes (text : string) = Encoding.UTF8.GetBytes text
    let private scene (stage : int) = bytes ("synthetic scene binding stage " + string stage + "\n")

    let private transformJson (json : byte array) (transform : JsonObject -> unit) =
        let root = JsonNode.Parse(json).AsObject ()
        transform root
        bytes (root.ToJsonString ())

    let private addOpaqueExtension json =
        transformJson json (fun root ->
            root["opaque"] <-
                JsonNode.Parse
                    "{\"revision\":7,\"nested\":[true,null,{\"number\":1.25,\"names\":[\"a\",\"b\"]}],\"object\":{\"kept\":\"yes\"}}"
            let members = root["members"].AsObject ()
            let localMember = members[local].AsObject ()
            localMember["ancillary"] <-
                JsonNode.Parse "{\"nested\":[1,{\"keep\":true}],\"label\":\"local metadata\"}")

    let private extensionSemantic (policy : Policy) =
        JsonNode.Parse(policy.ExtensionJson["opaque"]).ToJsonString ()

    let private assertExtension name expected (policy : Policy) =
        check name
            (policy.ExtensionJson.Count = 1 &&
             extensionSemantic policy = expected &&
             policy.MemberExtensionJson[local].ContainsKey "ancillary" &&
             JsonNode.Parse(policy.MemberExtensionJson[local]["ancillary"]).ToJsonString () =
                 JsonNode.Parse("{\"nested\":[1,{\"keep\":true}],\"label\":\"local metadata\"}").ToJsonString ())

    let private reload (generation : int64) (sceneBytes : byte array) (materials : Map<string, MaterialFields>) (json : byte array) =
        MaterialIntent.load sequence generation source family sceneBytes materials json
        |> ok ("reload-generation-" + string generation)

    let private bindReload (generation : int64) (sceneBytes : byte array) (draft : Draft) =
        let bound = MaterialIntent.bind sceneBytes draft |> ok ("bind-generation-" + string generation)
        check ("generation-advanced-" + string generation) (bound.Policy.Generation = generation)
        let loaded = reload generation sceneBytes bound.Materials bound.CompanionUtf8
        (loaded, bound.Materials, bound.CompanionUtf8)

    let private allAlbedo (value : Rgba option) (materials : Map<string, MaterialFields>) =
        family |> Array.forall (fun address -> (Map.find address materials).AlbedoOpt = value)

    let private allRoughness (value : single option) (materials : Map<string, MaterialFields>) =
        family |> Array.forall (fun address -> (Map.find address materials).RoughnessOpt = value)

    let private nonlocalAlbedo (value : Rgba option) (materials : Map<string, MaterialFields>) =
        family |> Array.filter ((<>) local) |> Array.forall (fun address -> (Map.find address materials).AlbedoOpt = value)

    let private addUnknownRoot json = addOpaqueExtension json

    let private removeRoot (name : string) json =
        transformJson json (fun root -> root.Remove name |> ignore)

    let private setRootString (name : string) (value : string) json =
        transformJson json (fun root -> root[name] <- JsonValue.Create value)

    let private setRootNumber (name : string) (value : int64) json =
        transformJson json (fun root -> root[name] <- JsonValue.Create value)

    let private setRootNode (name : string) (value : string) json =
        transformJson json (fun root -> root[name] <- JsonNode.Parse value)

    let private alterMember (address : string) (transform : JsonObject -> unit) json =
        transformJson json (fun root ->
            let members = root["members"].AsObject ()
            let memberNode = members[address].AsObject ()
            transform memberNode)

    let private addMember (address : string) json =
        transformJson json (fun root ->
            let members = root["members"].AsObject ()
            members[address] <- JsonNode.Parse "{\"AlbedoOpt\":\"inherit\",\"RoughnessOpt\":\"inherit\"}")

    let private removeMember (address : string) json =
        transformJson json (fun root ->
            let members = root["members"].AsObject ()
            members.Remove address |> ignore)

    let private loadAt0 (sceneBytes : byte array) (materials : Map<string, MaterialFields>) (json : byte array) =
        MaterialIntent.load sequence 0L source family sceneBytes materials json

    let private runFiveStage () =
        check "fixed-roster-count" (family.Length = 32 && (Set.ofArray family).Count = 32 && Array.contains source family && Array.contains local family)

        let policy0 = MaterialIntent.initialize sequence source family (scene 0) initialMaterials |> ok "initialize"
        check "initialize-generation-zero" (policy0.Generation = 0L)
        check "initialize-all-inherit" (policy0.Members |> Map.forall (fun _ mode -> mode.AlbedoMode = Inherit && mode.RoughnessMode = Inherit))
        let json0 = MaterialIntent.serializeUtf8 policy0 |> addOpaqueExtension
        let policy0 = reload 0L (scene 0) initialMaterials json0
        let extensionExpected = extensionSemantic policy0
        assertExtension "extension-load" extensionExpected policy0

        let draft0 = MaterialIntent.prepare policy0 initialMaterials |> ok "prepare-stage-1"
        let stage1Draft = MaterialIntent.apply (ReviseAlbedo (Some a)) draft0 |> ok "apply-stage-1"
        check "stage-1-all-32-albedo-a" (allAlbedo (Some a) stage1Draft.Materials)
        check "stage-1-all-roughness-absent" (allRoughness None stage1Draft.Materials)
        check "stage-1-input-materials-unchanged" (draft0.Materials = initialMaterials)
        check "stage-1-input-modes-unchanged" (draft0.Members = policy0.Members)
        let policy1, materials1, _ = bindReload 1L (scene 1) stage1Draft
        assertExtension "extension-stage-1" extensionExpected policy1

        let stage2Base = MaterialIntent.prepare policy1 materials1 |> ok "prepare-stage-2"
        let stage2Draft =
            MaterialIntent.applyMany
                [PinAlbedo (local, Some a); PinRoughness (local, Some 0.75f)]
                stage2Base
            |> ok "apply-stage-2"
        check "stage-2-equal-value-pin-keeps-a" (allAlbedo (Some a) stage2Draft.Materials)
        check "stage-2-local-roughness-075" ((Map.find local stage2Draft.Materials).RoughnessOpt = Some 0.75f)
        check "stage-2-other-roughness-absent" (family |> Array.filter ((<>) local) |> Array.forall (fun address -> (Map.find address stage2Draft.Materials).RoughnessOpt = None))
        check "stage-2-both-local-modes-pinned" (stage2Draft.Members[local] = { AlbedoMode = Pin; RoughnessMode = Pin })
        check "stage-2-base-draft-independent" (stage2Base.Members[local] = { AlbedoMode = Inherit; RoughnessMode = Inherit })
        let policy2, materials2, json2 = bindReload 2L (scene 2) stage2Draft
        check "stage-2-equal-value-pin-survives-json" (policy2.Members[local].AlbedoMode = Pin && (Map.find local materials2).AlbedoOpt = Some a)
        assertExtension "extension-stage-2" extensionExpected policy2

        let flippedJson = alterMember local (fun memberNode -> memberNode["AlbedoOpt"] <- JsonValue.Create "inherit") json2
        let flipped = MaterialIntent.load sequence 2L source family (scene 2) materials2 flippedJson |> ok "load-flipped-mode-probe"
        check "mode-flip-detected-independent-of-equal-values" (flipped.Members[local].AlbedoMode <> policy2.Members[local].AlbedoMode && (Map.find local materials2).AlbedoOpt = Some a)

        let stage3Base = MaterialIntent.prepare policy2 materials2 |> ok "prepare-stage-3"
        let stage3Draft = MaterialIntent.apply (ReviseAlbedo (Some b)) stage3Base |> ok "apply-stage-3"
        check "stage-3-local-retains-a" ((Map.find local stage3Draft.Materials).AlbedoOpt = Some a)
        check "stage-3-other-31-take-b" (nonlocalAlbedo (Some b) stage3Draft.Materials)
        check "stage-3-local-roughness-retained" ((Map.find local stage3Draft.Materials).RoughnessOpt = Some 0.75f)
        check "stage-3-modes-retained" (stage3Draft.Members[local] = { AlbedoMode = Pin; RoughnessMode = Pin })
        let policy3, materials3, _ = bindReload 3L (scene 3) stage3Draft
        assertExtension "extension-stage-3" extensionExpected policy3

        let stage4Base = MaterialIntent.prepare policy3 materials3 |> ok "prepare-stage-4"
        let stage4Draft = MaterialIntent.apply (InheritAlbedo local) stage4Base |> ok "apply-stage-4"
        check "stage-4-release-adopts-b" ((Map.find local stage4Draft.Materials).AlbedoOpt = Some b)
        check "stage-4-only-albedo-mode-inherits" (stage4Draft.Members[local] = { AlbedoMode = Inherit; RoughnessMode = Pin })
        check "stage-4-roughness-unchanged" ((Map.find local stage4Draft.Materials).RoughnessOpt = Some 0.75f)
        let policy4, materials4, _ = bindReload 4L (scene 4) stage4Draft
        assertExtension "extension-stage-4" extensionExpected policy4

        let stage5Base = MaterialIntent.prepare policy4 materials4 |> ok "prepare-stage-5"
        let stage5Draft = MaterialIntent.apply (ReviseAlbedo (Some c)) stage5Base |> ok "apply-stage-5"
        check "stage-5-all-32-albedo-c" (allAlbedo (Some c) stage5Draft.Materials)
        check "stage-5-local-roughness-retained" ((Map.find local stage5Draft.Materials).RoughnessOpt = Some 0.75f)
        let policy5, materials5, json5 = bindReload 5L (scene 5) stage5Draft
        check "stage-5-final-modes" (policy5.Members[local] = { AlbedoMode = Inherit; RoughnessMode = Pin })
        check "stage-5-final-values" (allAlbedo (Some c) materials5 && (Map.find local materials5).RoughnessOpt = Some 0.75f)
        assertExtension "extension-stage-5" extensionExpected policy5
        let finalReload = MaterialIntent.load sequence 5L source family (scene 5) materials5 json5 |> ok "final-reload"
        check "final-reload-exact-modes" (finalReload.Members = policy5.Members)
        check "final-reload-exact-hash" (finalReload.SceneSha256 = policy5.SceneSha256)

        (policy0, json0, extensionExpected)

    let private runAbsentAndSymmetryControls policy0 extensionExpected =
        let baseDraft = MaterialIntent.prepare policy0 initialMaterials |> ok "prepare-absent-option"
        let pinnedAbsent = MaterialIntent.apply (PinAlbedo (local, None)) baseDraft |> ok "pin-absent-albedo"
        let revised = MaterialIntent.apply (ReviseAlbedo (Some b)) pinnedAbsent |> ok "revise-after-absent-pin"
        check "pinned-absent-survives-distinct-source" ((Map.find local revised.Materials).AlbedoOpt = None && revised.Members[local].AlbedoMode = Pin)
        check "inherited-absent-follows-distinct-source" (nonlocalAlbedo (Some b) revised.Materials)
        let sourceAbsent = MaterialIntent.apply (ReviseAlbedo None) revised |> ok "revise-source-back-to-absent"
        check "equal-absent-still-pinned-before-release" ((Map.find local sourceAbsent.Materials).AlbedoOpt = None && sourceAbsent.Members[local].AlbedoMode = Pin)
        let released = MaterialIntent.apply (InheritAlbedo local) sourceAbsent |> ok "release-to-absent-source"
        check "release-adopts-absent-source" ((Map.find local released.Materials).AlbedoOpt = None && released.Members[local].AlbedoMode = Inherit)

        let albedoPinned = MaterialIntent.apply (PinAlbedo (local, Some a)) baseDraft |> ok "symmetry-pin-albedo"
        let roughnessRevised = MaterialIntent.apply (ReviseRoughness (Some 0.4f)) albedoPinned |> ok "symmetry-revise-roughness"
        check "roughness-revision-does-not-change-albedo" ((Map.find local roughnessRevised.Materials).AlbedoOpt = Some a)
        check "roughness-revision-all-inherited" (allRoughness (Some 0.4f) roughnessRevised.Materials)
        let roughnessPinned = MaterialIntent.apply (PinRoughness (local, None)) roughnessRevised |> ok "symmetry-pin-roughness-absent"
        let roughnessDistinct = MaterialIntent.apply (ReviseRoughness (Some 0.9f)) roughnessPinned |> ok "symmetry-distinct-roughness"
        check "roughness-pin-survives-and-albedo-unchanged" ((Map.find local roughnessDistinct.Materials).RoughnessOpt = None && (Map.find local roughnessDistinct.Materials).AlbedoOpt = Some a)
        let roughnessReleased = MaterialIntent.apply (InheritRoughness local) roughnessDistinct |> ok "symmetry-release-roughness"
        check "roughness-release-adopts-source" ((Map.find local roughnessReleased.Materials).RoughnessOpt = Some 0.9f && roughnessReleased.Members[local].RoughnessMode = Inherit)
        let roughnessBound = MaterialIntent.bind (bytes "synthetic roughness extension binding\n") roughnessReleased |> ok "bind-roughness-extension"
        assertExtension "extension-survives-roughness-operations-and-binding" extensionExpected roughnessBound.Policy

        let sibling = family |> Array.find (fun address -> address <> source && address <> local)
        let branchA = MaterialIntent.apply (PinAlbedo (local, Some a)) baseDraft |> ok "branch-a"
        let branchB = MaterialIntent.apply (PinRoughness (sibling, Some 0.2f)) baseDraft |> ok "branch-b"
        check "successive-drafts-independent" (baseDraft.Members[local].AlbedoMode = Inherit && branchA.Members[local].AlbedoMode = Pin && branchB.Members[local].AlbedoMode = Inherit && branchB.Members[sibling].RoughnessMode = Pin)
        check "successive-drafts-share-no-extension-alias" (extensionSemantic branchA.Policy = extensionExpected && extensionSemantic branchB.Policy = extensionExpected)

    let private runNegativeControls policy0 json0 =
        let scene0 = scene 0
        let originalPolicyJson = MaterialIntent.serializeUtf8 policy0
        let originalMaterials = initialMaterials

        rejects "missing-required-metadata" "missing_metadata" (json0 |> removeRoot "schema" |> loadAt0 scene0 initialMaterials)
        rejects "wrong-scene-bytes" "scene_hash_mismatch" (MaterialIntent.load sequence 0L source family (bytes "different") initialMaterials json0)
        rejects "wrong-sequence" "sequence_mismatch" (MaterialIntent.load "wrong-sequence" 0L source family scene0 initialMaterials json0)
        rejects "wrong-generation" "generation_mismatch" (MaterialIntent.load sequence 1L source family scene0 initialMaterials json0)
        rejects "wrong-source" "source_mismatch" (json0 |> setRootString "source" "Game/Gameplay/Scene/Wrong" |> loadAt0 scene0 initialMaterials)
        rejects "unsupported-schema" "unsupported_schema" (json0 |> setRootString "schema" "r12-material-intent/v2" |> loadAt0 scene0 initialMaterials)
        rejects "empty-sequence" "invalid_sequence" (json0 |> setRootString "sequence" "" |> loadAt0 scene0 initialMaterials)
        rejects "negative-generation" "invalid_generation" (json0 |> setRootNumber "generation" -1L |> loadAt0 scene0 initialMaterials)
        rejects "nonintegral-generation" "invalid_generation" (json0 |> setRootNode "generation" "1.5" |> loadAt0 scene0 initialMaterials)
        rejects "wrong-schema-type" "wrong_metadata_type" (json0 |> setRootNode "schema" "7" |> loadAt0 scene0 initialMaterials)
        rejects "wrong-members-type" "wrong_metadata_type" (json0 |> setRootNode "members" "[]" |> loadAt0 scene0 initialMaterials)
        rejects "uppercase-scene-hash" "invalid_scene_hash" (json0 |> setRootString "scene_sha256" (policy0.SceneSha256.ToUpperInvariant ()) |> loadAt0 scene0 initialMaterials)

        let text = Encoding.UTF8.GetString json0
        let trimmed = text.TrimEnd ()
        let withoutRootClose = trimmed.Substring (0, trimmed.Length - 1)
        let duplicateRoot = bytes (withoutRootClose + ",\"schema\":\"r12-material-intent/v1\"}")
        rejects "duplicate-root-key" "duplicate_json_key" (loadAt0 scene0 initialMaterials duplicateRoot)
        let duplicateNested = bytes (withoutRootClose + ",\"extra-duplicate-probe\":{\"x\":1,\"x\":2}}")
        rejects "duplicate-nested-key" "duplicate_json_key" (loadAt0 scene0 initialMaterials duplicateNested)

        rejects "malformed-mode" "unsupported_mode" (json0 |> alterMember local (fun node -> node["AlbedoOpt"] <- JsonValue.Create "automatic") |> loadAt0 scene0 initialMaterials)
        rejects "missing-material-mode-key" "invalid_material_keys" (json0 |> alterMember local (fun node -> node.Remove "RoughnessOpt" |> ignore) |> loadAt0 scene0 initialMaterials)
        let opaqueModeStringJson = json0 |> alterMember local (fun node -> node["MetallicOpt"] <- JsonValue.Create "pin")
        let opaqueModeString = loadAt0 scene0 initialMaterials opaqueModeStringJson |> ok "opaque-member-pin-string-load"
        check "opaque-member-pin-string-preserved-not-managed" (opaqueModeString.MemberExtensionJson[local]["MetallicOpt"] = "\"pin\"" && opaqueModeString.Members[local] = policy0.Members[local])
        let opaqueModeRoundTrip = MaterialIntent.serializeUtf8 opaqueModeString |> loadAt0 scene0 initialMaterials |> ok "opaque-member-pin-string-roundtrip"
        check "opaque-member-pin-string-survives-roundtrip" (opaqueModeRoundTrip.MemberExtensionJson[local]["MetallicOpt"] = "\"pin\"")
        rejects "missing-target-key" "invalid_target_roster" (json0 |> removeMember local |> loadAt0 scene0 initialMaterials)
        rejects "extra-target-key" "invalid_target_roster" (json0 |> addMember "Game/Gameplay/Scene/Extra" |> loadAt0 scene0 initialMaterials)

        let missingMaterials = Map.remove local initialMaterials
        let extraMaterials = Map.add "Game/Gameplay/Scene/Extra" noneMaterial initialMaterials
        rejects "missing-material-map-member" "invalid_material_roster" (MaterialIntent.load sequence 0L source family scene0 missingMaterials json0)
        rejects "extra-material-map-member" "invalid_material_roster" (MaterialIntent.load sequence 0L source family scene0 extraMaterials json0)
        let nonfinite = Map.add local { noneMaterial with RoughnessOpt = Some Single.NaN } initialMaterials
        rejects "nonfinite-supplied-material" "nonfinite_material" (MaterialIntent.load sequence 0L source family scene0 nonfinite json0)

        let draft = MaterialIntent.prepare policy0 initialMaterials |> ok "negative-prepare"
        rejects "unknown-operation-target" "invalid_target" (MaterialIntent.apply (PinAlbedo ("Game/Gameplay/Scene/Unknown", Some a)) draft)
        rejects "source-operation-target" "invalid_target" (MaterialIntent.apply (PinAlbedo (source, Some a)) draft)
        rejects "nonfinite-operation-value" "nonfinite_material" (MaterialIntent.apply (PinRoughness (local, Some Single.PositiveInfinity)) draft)
        check "rejections-leave-policy-input-unchanged" (MaterialIntent.serializeUtf8 policy0 = originalPolicyJson)
        check "rejections-leave-material-input-unchanged" (initialMaterials = originalMaterials && draft.Materials = originalMaterials)

        rejects "duplicate-family-init" "invalid_family" (MaterialIntent.initialize sequence source (Array.append family [|local|]) scene0 initialMaterials)
        rejects "missing-source-family-init" "invalid_family" (MaterialIntent.initialize sequence source (family |> Array.filter ((<>) source)) scene0 (Map.remove source initialMaterials))
        rejects "empty-sequence-init" "invalid_sequence" (MaterialIntent.initialize "" source family scene0 initialMaterials)
        let explicitInitAfterFailure = MaterialIntent.initialize sequence source family scene0 initialMaterials |> ok "explicit-init-after-failed-load"
        check "initialization-is-explicit-generation-zero-not-successor" (explicitInitAfterFailure.Generation = 0L && explicitInitAfterFailure.Members |> Map.forall (fun _ value -> value.AlbedoMode = Inherit && value.RoughnessMode = Inherit))

    [<EntryPoint>]
    let main _ =
        try
            let policy0, json0, extensionExpected = runFiveStage ()
            runAbsentAndSymmetryControls policy0 extensionExpected
            runNegativeControls policy0 json0
            printfn "CONTROL_SUMMARY positive=%d expected_rejections=%d total=%d" positiveCount rejectionCount (positiveCount + rejectionCount)
            0
        with ex ->
            eprintfn "CONTROL_FAILURE %s" (ex.ToString ())
            1
