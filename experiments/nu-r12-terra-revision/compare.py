"""Score one assigned revision and optional actual-save reopen, retaining adverse evidence."""
import argparse
import json
from pathlib import Path

from run import BASE_SHA, CASES, PROTOCOL_SHA, load_base
from oracle import (Findings, HISTORY, LOCAL, MATERIAL, SCENE, SELECTED, SOURCE, TRANSFORMS,
                    check_baseline, check_capture, check_history, check_links, compare_nodes,
                    equal, fixed_originals, lifecycle, nodes, properties, symbol, tree)

base = load_base()
sha, read, save, manifest = base.sha, base.read, base.save, base.manifest


def check_provenance(root, arm, predecessor, f):
    receipt = read(root / 'receipt.json')
    obs = root / 'observations'
    summary, startup = read(obs / 'summary.json'), read(obs / 'startup.json')
    assignment = read(root / 'assignment.json')
    case = assignment['Case']
    f.check(case in CASES, 'invalid', arm, 'declared_case')
    operator, condition = case.split('-')
    expected_assignment = dict(Case=case, CaseOrdinal=CASES.index(case) + 1, Operator=operator,
                               Condition=condition, Role='revise' if arm == 'L0' else 'reopen', Arm=arm,
                               ProtocolSha256=PROTOCOL_SHA,
                               PredecessorReceiptSha256=sha(predecessor / 'receipt.json') if predecessor else None)
    f.check(assignment == expected_assignment and receipt['assignment'] == assignment,
            'invalid', arm, 'assignment_contents_and_predecessor', expected_assignment, assignment)
    f.check(receipt['case'] == case and receipt['arm'] == arm and receipt['assignment_unchanged']
            and receipt['assignment_observed_and_bound']
            and receipt['assignment_sha256'] == sha(root / 'assignment.json')
            and all(row['Case'] == case and row['Arm'] == arm and row['AssignmentSha256'] == receipt['assignment_sha256']
                    for row in (summary, startup)), 'invalid', arm, 'observed_assignment_binding')
    f.check(receipt['shared_runner_sha256'] == BASE_SHA and receipt['shared_runner_unchanged']
            and sha(root / 'shared-inputs/terra-run.py') == BASE_SHA, 'invalid', arm, 'accepted_shared_runner')
    authority = root / 'authorities'
    acceptance = read(authority / 'native-acceptance.json')
    f.check(receipt['build_receipt_sha256'] == sha(authority / 'receipt.json')
            and receipt['native_acceptance_sha256'] == sha(authority / 'native-acceptance.json')
            and acceptance['build_receipt_sha256'] == receipt['build_receipt_sha256']
            and acceptance['source_binary_seal_sha256'] == sha(authority / 'source-binary-seal.json')
            and acceptance['decision'] == 'accepted_for_native_execution'
            and acceptance['protocol_sha256'] == PROTOCOL_SHA == sha(root / 'package-inputs/PROTOCOL.md'),
            'invalid', arm, 'accepted_compile_source_protocol_seal')
    inputs = read(authority / 'package-inputs.json')
    f.check(manifest(root / 'package-inputs') == inputs == read(root / 'package-inputs.json'),
            'invalid', arm, 'compiled_package_inputs')
    f.check(all((Path(__file__).parent / name).is_file() and sha(Path(__file__).parent / name) == item['sha256']
                for name, item in inputs.items()), 'invalid', arm, 'scoring_with_accepted_package')
    f.check(sha(root / 'observations-manifest.json') == receipt['observations_manifest_sha256']
            and manifest(obs) == read(root / 'observations-manifest.json'), 'invalid', arm, 'sealed_observations')
    process = read(root / 'process.json')
    f.check(receipt['complete_observation_and_save'] and receipt['process'] == process
            and process['exit_code'] == 0 and not process['timed_out'] and process['deadline_seconds'] == 180
            and receipt['protected_application_files_unchanged'] and not receipt['changed_or_removed_application_files']
            and receipt['runtime_selection_recorded'] and summary == receipt['summary']
            and summary['Complete'] and summary['EngineExitCode'] == 0 and summary['ServerGC'] and startup['ServerGC'],
            'invalid', arm, 'complete_process_cleanup_and_observation')
    expected_input = sha(predecessor / 'observations/saved-Scene.nugroup') if predecessor else base.SCENE_SHA
    f.check(startup['InputSceneSha256'] == expected_input and startup['OriginalSceneSha256'] == base.SCENE_SHA
            and sha(root / 'application/original-Scene.nugroup') == base.SCENE_SHA,
            'invalid', arm, 'assigned_scene_edition', expected_input, startup['InputSceneSha256'])
    f.check(receipt['saved_scene_sha256'] == sha(obs / 'saved-Scene.nugroup'), 'invalid', arm, 'actual_saved_bytes')
    if predecessor:
        prev = read(predecessor / 'receipt.json')
        f.check(prev['case'] == case and prev['arm'] == 'L0' and prev['complete_observation_and_save']
                and prev['build_receipt_sha256'] == receipt['build_receipt_sha256']
                and (receipt.get('predecessor') or {}).get('sha256') == sha(predecessor / 'receipt.json'),
                'invalid', arm, 'same_case_actual_complete_predecessor')
    return receipt, startup, summary, assignment


def check_phases(root, arm, summary, assignment, f):
    obs = root / 'observations'
    labels = ['Loaded', 'Ready', 'Prepared', 'Applied', 'Settled'] if arm == 'L0' else ['ReopenA', 'ReopenB']
    captures = [read(obs / (label + '.json')) for label in labels]
    first = captures[0]['Callback']
    wanted_callbacks = [first, first + 1, first + 1, first + 1, first + 2] if arm == 'L0' else [first, first + 1]
    f.check(summary['Labels'] == labels and summary['CaptureCount'] == len(labels)
            and summary['CallbackCount'] == wanted_callbacks[-1] <= 120
            and [c['Callback'] for c in captures] == wanted_callbacks
            and [c['Label'] for c in captures] == labels
            and all(c['Case'] == assignment['Case'] for c in captures), 'invalid', arm, 'fixed_capture_sequence')
    phases = sorted(obs.glob('phase-*.json'))
    rows = [read(path) for path in phases]
    f.check([p.name for p in phases] == [f'phase-{n:03d}.json' for n in range(1, wanted_callbacks[-1] + 1)]
            and [r['Callback'] for r in rows] == list(range(1, wanted_callbacks[-1] + 1))
            and next((r['Callback'] for r in rows if r['SceneExists']), None) == first,
            'invalid', arm, 'unfiltered_first_scene_exists_and_following_callbacks')
    boundaries = read(obs / 'boundaries.json')
    boundary_names = (['load', 'ready_wait', 'preparation', 'operator', 'applied', 'settling', 'save', 'cleanup', 'returned']
                      if arm == 'L0' else ['load', 'reopen_wait', 'save', 'cleanup', 'returned'])
    f.check([b['Name'] for b in boundaries] == boundary_names, 'invalid', arm, 'phase_boundary_roster')
    bound = {b['Name']: b for b in boundaries}
    mapping = dict(Loaded='ready_wait', Ready='preparation', Prepared='operator', Applied='applied', Settled='save') if arm == 'L0' else dict(ReopenA='reopen_wait', ReopenB='save')
    for capture in captures:
        boundary = bound[mapping[capture['Label']]]
        f.check(capture['Counter'] == boundary['Counter'] and capture['Callback'] == boundary['Callback'],
                'invalid', arm, capture['Label'] + ':capture_boundary_binding')
    f.check(bound['load']['Callback'] == 1 and bound['load']['Counter'] == 0,
            'invalid', arm, 'subscription_before_gameplay_once')
    if arm == 'L0':
        f.check(bound['applied']['Counter'] == bound['settling']['Counter'], 'invalid', arm, 'immediate_applied_interval')
        for label in ('Ready', 'Prepared'):
            checks = read(obs / (label + '-checks.json'))
            f.check(bool(checks) and all(r['Passed'] for r in checks), 'invalid', arm, label + ':runtime_preconditions')
        f.check(read(obs / 'family-selection.json') == sorted(fixed_originals(symbol((root / 'application/original-Scene.nugroup').read_text(encoding='utf-8')))[1]),
                'invalid', arm, 'public_selector_matches_independent_original_roster')
    wanted_writes = ([1 if assignment['Condition'] == 'local' else 0, 1 if assignment['Operator'] == 'P' else 32,
                      1 if assignment['Operator'] == 'P' else 0] if arm == 'L0' else [0, 0, 0])
    actual_writes = [summary[k] for k in ('SetupWrites', 'OperatorWrites', 'PropagationCalls')]
    f.check(actual_writes == wanted_writes, 'invalid', arm, 'assigned_actions_only', wanted_writes, actual_writes)
    return captures, boundaries


def evaluate(l0, l1=None):
    f = Findings()
    details = {}
    original, palms = fixed_originals(symbol((l0 / 'application/original-Scene.nugroup').read_text(encoding='utf-8')))
    prepared = settled = None
    for arm, root in (('L0', l0), ('L1', l1)):
        if root is None:
            continue
        obs = root / 'observations'
        receipt, startup, summary, assignment = check_provenance(root, arm, l0 if arm == 'L1' else None, f)
        captures, boundaries = check_phases(root, arm, summary, assignment, f)
        raw_original = read(obs / 'original-expectations.json')
        expected_rows = {a: {'Address': a, 'Dispatcher': n['Dispatcher'], 'Children': n['Children'], 'Properties': n['Properties']}
                         for a, n in original.items()}
        actual_rows = {r['Address']: {**r, 'Properties': {p['Name']: symbol(p['Symbol']) for p in r['Properties']}}
                       for r in raw_original}
        f.check(len(raw_original) == 197 and actual_rows == expected_rows, 'invalid', arm, 'independent_original_expectations')
        before_manifest = read(root / 'application-before.json')
        for data in [startup, summary] + captures:
            assemblies = data['LoadedAssemblies']
            nu = [a for a in assemblies if a['Name'] == 'Nu']
            f.check(len(nu) == 1 and Path(nu[0]['Path']).resolve() == (root / 'application/Nu.dll').resolve()
                    and nu[0]['Sha256'] == base.NU_SHA == before_manifest.get('Nu.dll', {}).get('sha256'),
                    'invalid', arm, 'loaded_Nu_identity_and_staged_path', str(root / 'application/Nu.dll'), nu)
            for assembly in assemblies:
                path = Path(assembly['Path'])
                if path.parent.resolve() == (root / 'application').resolve():
                    f.check(path.name in before_manifest and assembly['Sha256'] == before_manifest[path.name]['sha256'],
                            'invalid', arm, 'loaded_application_assembly:' + path.name)
        current = {c['Label']: check_capture(c, original, f, arm + ':' + c['Label']) for c in captures}
        if arm == 'L0':
            check_baseline(current['Ready'], original, palms, f, 'L0:Ready')
            compare_nodes(current['Loaded'], current['Ready'], original, f, 'L0:Loaded_to_Ready', 'invalid', keep_ids=True)
            compare_nodes(current['Ready'], current['Prepared'], original, f, 'L0:Prepared', 'invalid',
                          local_roughness=LOCAL if assignment['Condition'] == 'local' else None, keep_ids=True)
            prepared, settled = current['Prepared'], current['Settled']
            outcomes = ['Applied', 'Settled']
        else:
            outcomes = ['ReopenA', 'ReopenB']
            for label in outcomes:
                compare_nodes(settled, current[label], original, f, 'L1:' + label + ':actual_predecessor')
        for label in outcomes:
            phase = arm + ':' + label
            advancing = (SOURCE, SCENE + '/Villa') if assignment['Operator'] == 'P' else ()
            compare_nodes(prepared, current[label], original, f, phase, palm_albedo=palms, advancing_histories=advancing)
            check_links(current[label], original, f, phase)
            source_trees = {}
            for address, suffix in ((SOURCE, 'palm'), (SCENE + '/Villa', 'villa')):
                path = obs / (label + '-' + suffix + '.nuentity')
                if address in current[label]:
                    source_trees[address] = symbol(path.read_text(encoding='utf-8'))
            check_history(current[label], original, source_trees, assignment['Operator'], f, phase)
        endpoint = captures[-1]['Label']
        saved_text = (obs / 'saved-Scene.nugroup').read_text(encoding='utf-8')
        saved = symbol(saved_text)
        f.check(set(tree(saved)) == set(original), 'adverse', arm, 'saved_original_named_tree', sorted(original), sorted(tree(saved)))
        f.check(summary['SavedDescriptorMatchesEndpoint'] and saved == symbol((obs / (endpoint + '.nugroup')).read_text(encoding='utf-8'))
                == symbol((obs / 'saved-canonical.nugroup').read_text(encoding='utf-8')),
                'adverse', arm, 'save_matches_actual_endpoint')
        events = [json.loads(line) for line in (obs / 'lifecycle.jsonl').read_text(encoding='utf-8-sig').splitlines()]
        trace = lifecycle(events, summary['FinalLifecycleCounter'], captures, boundaries, original,
                          assignment['Operator'] if arm == 'L0' else 'B', f, arm)
        details[arm] = {'case': assignment['Case'], 'lifecycle': trace,
                        'generated_entities_by_phase': {c['Label']: [r for r in c['Entities'] if r['Address'] not in original] for c in captures},
                        'phase_times': [{'Label': c['Label'], 'ElapsedSeconds': c['ElapsedSeconds']} for c in captures],
                        'process_seconds': receipt['process']['elapsed_seconds']}
    counts = {kind: sum(r['kind'] == kind for r in f.rows) for kind in ('invalid', 'adverse', 'lifecycle')}
    disposition = 'invalid_or_incomplete' if counts['invalid'] else 'adverse' if counts['adverse'] else 'passed_declared_configuration'
    return {'disposition': disposition, 'counts': counts, 'scope': 'pair' if l1 else 'revise_only',
            'reopen_eligible': not counts['invalid'], 'findings': f.rows, 'details': details,
            'lifecycle_measure_established': counts['lifecycle'] == 0 and counts['invalid'] == 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--l0', type=Path, required=True)
    parser.add_argument('--l1', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Retain every scoring attempt; output already exists.')
    hashes = {arm: {'receipt': sha(p / 'receipt.json'), 'observations': manifest(p / 'observations')}
              for arm, p in (('L0', args.l0), ('L1', args.l1)) if p is not None}
    source_hashes = {p.name: sha(p) for p in Path(__file__).parent.iterdir() if p.is_file()}
    try:
        result = evaluate(args.l0.resolve(), args.l1.resolve() if args.l1 else None)
    except Exception as error:
        result = {'disposition': 'invalid_or_incomplete', 'reopen_eligible': False,
                  'comparison_error': str(error), 'error_type': type(error).__name__}
    unchanged = all(sha(p / 'receipt.json') == hashes[arm]['receipt'] and manifest(p / 'observations') == hashes[arm]['observations']
                    for arm, p in (('L0', args.l0), ('L1', args.l1)) if p is not None)
    unchanged = unchanged and all(sha(Path(__file__).parent / name) == value for name, value in source_hashes.items())
    if not unchanged:
        result.update(disposition='invalid_or_incomplete', reopen_eligible=False, concurrent_input_change=True)
    result['inputs'] = {'source_hashes': source_hashes, 'run_hashes': hashes, 'unchanged': unchanged}
    save(args.output, result)
    print(json.dumps({k: v for k, v in result.items() if k not in ('findings', 'details', 'inputs')}, indent=2))
    return 2 if result['disposition'] == 'invalid_or_incomplete' else 0


if __name__ == '__main__':
    raise SystemExit(main())
