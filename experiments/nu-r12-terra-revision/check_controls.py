"""Synthetic oracle falsifiers, based on retained prerequisite bytes; never a native experiment."""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import re
import shutil

import compare
from oracle import (Findings, HISTORY, LOCAL, MATERIAL, SCENE, SOURCE, TINT, fixed_originals,
                    lifecycle, material, nodes, pairs, properties, symbol, tree)
from run import BASE_SHA, CASES, PACKAGE, PROTOCOL_SHA

read, save, sha, manifest = compare.read, compare.save, compare.sha, compare.manifest


def text(value):
    if isinstance(value, list):
        return '[' + ' '.join(text(x) for x in value) + ']'
    return value if value and re.fullmatch(r'[^\s\[\]"\\]+', value) else json.dumps(value)


def set_prop(data, address, name, value):
    prop = properties(nodes(data)[address])[name]
    prop.update(Found=True, Value=text(value), Error='')


def set_material(data, address, field, value):
    prop = properties(nodes(data)[address])['MaterialProperties']
    fields = material(symbol(prop['Value']))
    fields[field] = value
    prop['Value'] = text([[name, fields[name]] for name in MATERIAL])


def seal(root):
    receipt = read(root / 'receipt.json')
    receipt['summary'] = read(root / 'observations/summary.json')
    assignment = read(root / 'assignment.json')
    receipt.update(assignment=assignment, assignment_sha256=sha(root / 'assignment.json'))
    for name in ('startup.json', 'summary.json'):
        path = root / 'observations' / name
        data = read(path)
        data['AssignmentSha256'] = receipt['assignment_sha256']
        save(path, data)
    receipt['summary'] = read(root / 'observations/summary.json')
    receipt['saved_scene_sha256'] = sha(root / 'observations/saved-Scene.nugroup')
    save(root / 'observations-manifest.json', manifest(root / 'observations'))
    receipt['observations_manifest_sha256'] = sha(root / 'observations-manifest.json')
    save(root / 'receipt.json', receipt)


def relocate_assembly_observations(root):
    for path in (root / 'observations').glob('*.json'):
        data = read(path)
        if isinstance(data, dict) and 'LoadedAssemblies' in data:
            for assembly in data['LoadedAssemblies']:
                old = Path(assembly['Path'])
                if old.parent.name == 'application':
                    assembly['Path'] = str(root / 'application' / old.name)
            save(path, data)


def make_pair(path, reference, case):
    """Invent a visibly synthetic expected-output fixture, retaining every fixture byte."""
    original_path = reference / 'application/original-Scene.nugroup'
    original_group = symbol(original_path.read_text(encoding='utf-8'))
    original, palms = fixed_originals(original_group)
    baseline = read(reference / 'observations/B.json')
    canonical_group = symbol((reference / 'observations/B.nugroup').read_text(encoding='utf-8'))
    operator, condition = case.split('-')
    loaded = deepcopy(baseline)
    ready = deepcopy(baseline)
    prepared = deepcopy(baseline)
    if condition == 'local':
        set_material(prepared, LOCAL, 'RoughnessOpt', ['Some', '0.75'])
    applied = deepcopy(prepared)
    for address in palms:
        if case != 'P-local' or address != LOCAL:
            set_material(applied, address, 'AlbedoOpt', TINT)

    def descriptor(data):
        group = deepcopy(canonical_group)
        raw = tree(group)
        for address in palms:
            value = symbol(properties(nodes(data)[address])['MaterialProperties']['Value'])
            fields = pairs(raw[address]['Raw'][1])
            fields['MaterialProperties'] = value
            raw[address]['Raw'][1] = [[k, v] for k, v in fields.items()]
        return group

    if operator == 'P':
        group = descriptor(applied)
        for address in (SOURCE, SCENE + '/Villa'):
            raw = tree(group)[address]['Raw']
            history = [raw[0], [p for p in deepcopy(raw[1]) if p[0] != HISTORY], deepcopy(raw[2])]
            fields = pairs(raw[1])
            fields[HISTORY] = ['Some', history]
            raw[1] = [[k, v] for k, v in fields.items()]
            set_prop(applied, address, HISTORY, ['Some', history])
        final_group = group
    else:
        final_group = descriptor(applied)
    settled = deepcopy(applied)
    for arm in ('L0', 'L1'):
        root = path / arm
        obs = root / 'observations'
        obs.mkdir(parents=True)
        (root / 'application').mkdir()
        shutil.copy2(original_path, root / 'application/original-Scene.nugroup')
        shutil.copytree(PACKAGE, root / 'package-inputs', ignore=shutil.ignore_patterns('__pycache__'))
        inputs = manifest(root / 'package-inputs')
        save(root / 'package-inputs.json', inputs)
        authority = root / 'authorities'
        authority.mkdir()
        save(authority / 'package-inputs.json', inputs)
        save(authority / 'receipt.json', {'synthetic': True, 'purpose': 'oracle control; no compiled binary'})
        save(authority / 'source-binary-seal.json', {'synthetic': True, 'purpose': 'not a native source proof'})
        save(authority / 'native-acceptance.json', dict(synthetic=True, decision='accepted_for_native_execution',
             build_receipt_sha256=sha(authority / 'receipt.json'), source_binary_seal_sha256=sha(authority / 'source-binary-seal.json'),
             protocol_sha256=PROTOCOL_SHA))
        (root / 'shared-inputs').mkdir()
        shutil.copy2(PACKAGE.parent / 'nu-r12-terra-firma/run.py', root / 'shared-inputs/terra-run.py')
        predecessor = path / 'L0' if arm == 'L1' else None
        assignment = dict(Case=case, CaseOrdinal=CASES.index(case) + 1, Operator=operator, Condition=condition,
                          Role='revise' if arm == 'L0' else 'reopen', Arm=arm, ProtocolSha256=PROTOCOL_SHA,
                          PredecessorReceiptSha256=sha(predecessor / 'receipt.json') if predecessor else None)
        save(root / 'assignment.json', assignment)
        startup = read(reference / 'observations/startup.json')
        startup.update(Case=case, Arm=arm, AssignmentSha256=sha(root / 'assignment.json'),
                       InputSceneSha256=sha(predecessor / 'observations/saved-Scene.nugroup') if predecessor else compare.base.SCENE_SHA)
        save(obs / 'startup.json', startup)
        shutil.copy2(reference / 'application-before.json', root / 'application-before.json')
        shutil.copy2(reference / 'observations/original-expectations.json', obs / 'original-expectations.json')
        labels = ['Loaded', 'Ready', 'Prepared', 'Applied', 'Settled'] if arm == 'L0' else ['ReopenA', 'ReopenB']
        datasets = [loaded, ready, prepared, applied, settled] if arm == 'L0' else [settled, settled]
        callback = [2, 3, 3, 3, 4] if arm == 'L0' else [2, 3]
        count = len(baseline['Entities'])
        for label, initial, cb in zip(labels, datasets, callback):
            data = deepcopy(initial)
            data.update(Label=label, Case=case, Callback=cb, Counter=count, ElapsedSeconds=float(cb))
            save(obs / (label + '.json'), data)
            group = final_group if label in ('Applied', 'Settled', 'ReopenA', 'ReopenB') else descriptor(data)
            (obs / (label + '.nugroup')).write_text(text(group), encoding='utf-8')
            for address, suffix in ((SOURCE, 'palm'), (SCENE + '/Villa', 'villa')):
                (obs / (label + '-' + suffix + '.nuentity')).write_text(text(tree(group)[address]['Raw']), encoding='utf-8')
        for i in range(1, callback[-1] + 1):
            save(obs / f'phase-{i:03d}.json', dict(Callback=i, SceneExists=i >= 2, GameplayExists=True, GameState='Gameplay'))
        if arm == 'L0':
            for label in ('Ready', 'Prepared'):
                save(obs / (label + '-checks.json'), [dict(Name='synthetic_precondition_receipt', Passed=True)])
            save(obs / 'family-selection.json', sorted(palms))
        boundary_names = ['load', 'ready_wait', 'preparation', 'operator', 'applied', 'settling', 'save', 'cleanup', 'returned'] if arm == 'L0' else ['load', 'reopen_wait', 'save', 'cleanup', 'returned']
        boundaries = [dict(Name=name, Callback=(1 if name == 'load' else 2 if name in ('ready_wait', 'reopen_wait')
                                               else callback[-1] if name in ('save', 'cleanup', 'returned') else 3),
                           Counter=0 if name == 'load' else 2 * count if name == 'returned' else count, ElapsedSeconds=0.0)
                      for name in boundary_names]
        save(obs / 'boundaries.json', boundaries)
        events = []
        for kind, phase, cb in (('register', 'load', 1), ('unregister', 'cleanup', callback[-1])):
            for row in baseline['Entities']:
                events.append(dict(Ordinal=len(events) + 1, Callback=cb, Phase=phase, ElapsedSeconds=0.0,
                                   Kind=kind, Address=row['Address'], Entity=True, Exists=True, Id=row['Id'], Error=''))
        (obs / 'lifecycle.jsonl').write_text('\n'.join(json.dumps(e) for e in events) + '\n', encoding='utf-8')
        for name in ('saved-Scene.nugroup', 'saved-canonical.nugroup'):
            (obs / name).write_text(text(final_group), encoding='utf-8')
        summary = dict(Arm=arm, Case=case, AssignmentSha256=sha(root / 'assignment.json'), Complete=True,
                       CallbackCount=callback[-1], CaptureCount=len(labels), Labels=labels, EngineExitCode=0,
                       SavedDescriptorMatchesEndpoint=True, FinalLifecycleCounter=len(events), ServerGC=True,
                       SetupWrites=int(condition == 'local') if arm == 'L0' else 0,
                       OperatorWrites=(1 if operator == 'P' else 32) if arm == 'L0' else 0,
                       PropagationCalls=int(operator == 'P') if arm == 'L0' else 0,
                       LoadedAssemblies=baseline['LoadedAssemblies'], ElapsedSeconds=5.0)
        save(obs / 'summary.json', summary)
        process = dict(synthetic=True, exit_code=0, timed_out=False, deadline_seconds=180, elapsed_seconds=5.0)
        save(root / 'process.json', process)
        receipt = dict(synthetic=True, stage='run', case=case, arm=arm, assignment=assignment, assignment_unchanged=True,
                       assignment_observed_and_bound=True, shared_runner_sha256=BASE_SHA, shared_runner_unchanged=True,
                       build_receipt_sha256=sha(authority / 'receipt.json'), native_acceptance_sha256=sha(authority / 'native-acceptance.json'),
                       process=process, protected_application_files_unchanged=True, changed_or_removed_application_files=[],
                       runtime_selection_recorded=True, complete_observation_and_save=True,
                       predecessor={'sha256': sha(predecessor / 'receipt.json')} if predecessor else None)
        save(root / 'receipt.json', receipt)
        relocate_assembly_observations(root)
        seal(root)
    save(path / 'SYNTHETIC.json', {'synthetic': True, 'case': case, 'prerequisite': str(reference),
                                 'source_observation_sha256': sha(reference / 'observations/B.json'),
                                 'warning': 'Invented outcomes and receipts test scoring only; no build or engine ran.'})


def edit_json(path, operation):
    data = read(path)
    operation(data)
    save(path, data)


def safe_evaluate(l0, l1=None):
    try:
        return compare.evaluate(l0, l1)
    except Exception as error:
        return dict(disposition='invalid_or_incomplete', reopen_eligible=False, comparison_error=str(error))


def trace_fixture():
    address = SOURCE
    original = {address: {'Properties': {}}}
    rows = [dict(Ordinal=i + 1, Kind=kind, Address=address, Id=identity, Entity=True, Exists=True,
                 Error='', Phase=phase, Callback=1, ElapsedSeconds=0.0)
            for i, (kind, identity, phase) in enumerate([
                ('register', 'A', 'load'), ('unregister', 'A', 'operator'), ('register', 'B', 'operator'),
                ('unregister', 'B', 'operator'), ('register', 'C', 'operator'), ('unregister', 'C', 'cleanup')])]
    captures = [dict(Label='Prepared', Counter=1, Entities=[dict(Address=address, Id='A')]),
                dict(Label='Applied', Counter=5, Entities=[dict(Address=address, Id='C')])]
    boundaries = [dict(Name=phase, Counter=count) for phase, count in [('load', 0), ('operator', 1), ('cleanup', 5), ('returned', 6)]]
    return rows, captures, boundaries, original


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    source_hashes = {p.name: sha(p) for p in PACKAGE.iterdir() if p.is_file()}
    save(output / 'source-hashes.json', source_hashes)
    shutil.copytree(PACKAGE, output / 'package-inputs', ignore=shutil.ignore_patterns('__pycache__'))
    results = []
    for case in CASES:
        path = output / ('reference-' + case)
        make_pair(path, args.reference.resolve(), case)
        result = safe_evaluate(path / 'L0', path / 'L1')
        expected = 'adverse' if case == 'P-local' else 'passed_declared_configuration'
        passed = result['disposition'] == expected and result['reopen_eligible']
        save(path / 'comparison.json', result)
        results.append(dict(name=case + ':synthetic_pair', passed=passed, actual=result['disposition'], expected=expected))
    base_pair = output / 'reference-B-local'

    def trial(name, mutate, expected='adverse', pair=False, reseal=True, source=base_pair):
        target = output / name
        shutil.copytree(source, target)
        for arm in ('L0', 'L1'):
            relocate_assembly_observations(target / arm)
            if arm == 'L1':
                previous_sha = sha(target / 'L0/receipt.json')
                edit_json(target / 'L1/assignment.json', lambda d: d.update(PredecessorReceiptSha256=previous_sha))
                edit_json(target / 'L1/receipt.json', lambda d: d.update(predecessor={'sha256': previous_sha}))
            seal(target / arm)
        mutate(target)
        if reseal:
            seal(target / 'L0')
            if pair:
                seal(target / 'L1')
        result = safe_evaluate(target / 'L0', target / 'L1' if pair else None)
        save(target / 'control-comparison.json', result)
        passed = result['disposition'] == expected
        if expected == 'adverse':
            passed &= result['reopen_eligible']
        results.append(dict(name=name, passed=passed, expected=expected, actual=result['disposition']))

    def capture_mutation(fn):
        return lambda target: edit_json(target / 'L0/observations/Applied.json', fn)

    for name, address, field, value in [('missed-tint-local', SOURCE, 'AlbedoOpt', 'None'),
                                         ('lost-roughness', LOCAL, 'RoughnessOpt', 'None')]:
        trial(name, capture_mutation(lambda d, a=address, k=field, v=value: set_material(d, a, k, v)))
    trial('missed-tint-shared', capture_mutation(lambda d: set_material(d, SOURCE, 'AlbedoOpt', 'None')),
          source=output / 'reference-B-shared')
    for field in ('Size', 'Offset'):
        def perturb(d, name=field):
            p = properties(nodes(d)[SOURCE])[name]
            value = symbol(p['Value'])
            value[0] = str(float(value[0]) + 0.00001)
            p['Value'] = text(value)
        trial('strict-' + field, capture_mutation(perturb))
    def transform(d):
        p = properties(nodes(d)[SOURCE])['Position']
        value = symbol(p['Value'])
        value[0] = str(float(value[0]) + 0.00001)
        p['Value'] = text(value)
    trial('declared-transform-tolerance', capture_mutation(transform), 'passed_declared_configuration')
    trial('unrelated-history', capture_mutation(lambda d: set_prop(d, SCENE + '/Villa/Barrel', HISTORY, 'None')))
    trial('missing-original', capture_mutation(lambda d: d['Entities'].__setitem__(slice(None), [r for r in d['Entities'] if r['Address'] != LOCAL])))
    def extra_saved(target):
        path = target / 'L0/observations/saved-Scene.nugroup'
        raw = symbol(path.read_text())
        raw[2].append(['EntityDispatcher', [['Name', 'UnassignedExtra']], []])
        path.write_text(text(raw))
    trial('extra-saved-entity', extra_saved)
    trial('wrong-input', lambda t: edit_json(t / 'L0/observations/startup.json', lambda d: d.update(InputSceneSha256='0' * 64)), 'invalid_or_incomplete')
    trial('wrong-phase', capture_mutation(lambda d: d.update(Callback=d['Callback'] + 1)), 'invalid_or_incomplete')
    trial('filtered-first-capture', lambda t: edit_json(t / 'L0/observations/phase-001.json', lambda d: d.update(SceneExists=True)), 'invalid_or_incomplete')
    trial('wrong-loaded-host', capture_mutation(lambda d: next(a for a in d['LoadedAssemblies'] if a['Name'] == 'Nu').update(Sha256='0' * 64)), 'invalid_or_incomplete')
    trial('correct-hash-wrong-Nu-path', capture_mutation(lambda d: next(a for a in d['LoadedAssemblies'] if a['Name'] == 'Nu').update(Path=str(output / 'outside-application/Nu.dll'))), 'invalid_or_incomplete')
    trial('changed-sealed-observation', capture_mutation(lambda d: d.update(Callback=99)), 'invalid_or_incomplete', reseal=False)
    trial('wrong-predecessor', lambda t: edit_json(t / 'L1/receipt.json', lambda d: d.update(predecessor={'sha256': '0' * 64})), 'invalid_or_incomplete', pair=True)
    trial('changed-sealed-source', lambda t: (t / 'L0/package-inputs/Program.fs').write_text('// changed source'), 'invalid_or_incomplete')
    for name in ('valid-different-multiplicity', 'lost-balanced-intermediate', 'duplicate-record', 'trailing-loss',
                 'unbalanced-transition', 'cross-address-live-ID-collision', 'duplicate-capture-IDs', 'empty-capture-ID'):
        events, captures, boundaries, original = trace_fixture()
        if name == 'lost-balanced-intermediate':
            events = [e for e in events if e['Ordinal'] not in (3, 4)]
        elif name == 'duplicate-record':
            events.insert(3, deepcopy(events[2]))
        elif name == 'trailing-loss':
            events.pop()
        elif name == 'unbalanced-transition':
            events[1]['Id'] = 'wrong-old-ID'
        elif name == 'cross-address-live-ID-collision':
            for capture in captures:
                capture['Entities'].append(dict(Address=SCENE + '/StillLive', Id='B'))
        elif name == 'duplicate-capture-IDs':
            for capture in captures:
                capture['Entities'].append(dict(Address=SCENE + '/Duplicated', Id=capture['Entities'][0]['Id']))
        elif name == 'empty-capture-ID':
            captures[0]['Entities'][0]['Id'] = ''
        f = Findings()
        result = lifecycle(events, 6, captures, boundaries, original, 'B', f, name)
        passed = (result['measure_established'] and bool(result['prediction_divergence'])) if name == 'valid-different-multiplicity' else not result['measure_established']
        save(output / (name + '.json'), dict(synthetic=True, events=events, final_counter=6, captures=captures,
                                           boundaries=boundaries, result=result, findings=f.rows))
        results.append(dict(name=name, passed=passed, actual=result['measure_established']))
    unchanged = all(sha(PACKAGE / name) == value for name, value in source_hashes.items())
    receipt = dict(synthetic_only=True, native_execution=False, controls=results, source_hashes=source_hashes,
                   source_unchanged=unchanged, passed=unchanged and all(r['passed'] for r in results))
    save(output / 'receipt.json', receipt)
    print(json.dumps(dict(passed=receipt['passed'], count=len(results), failed=[r for r in results if not r['passed']]), indent=2))
    return 0 if receipt['passed'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
