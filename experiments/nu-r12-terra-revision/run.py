"""Stage one assigned R12 material revision or its actual-save fresh reopen."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
BASE_PATH = PACKAGE.parent / 'nu-r12-terra-firma/run.py'
BASE_SHA = '367e0ae4924e1a1d0b71fe408362423d4a4f1423795da67b11a68ca84e71201a'
PROTOCOL_SHA = 'e6576d9ae1d825c8b9f3cb029ec3f57c22fb01f5cac12057cc3ae0b8db91fc49'
CASES = ('P-shared', 'B-shared', 'P-local', 'B-local')


def load_base():
    if hashlib.sha256(BASE_PATH.read_bytes()).hexdigest() != BASE_SHA:
        raise ValueError('The accepted shared staging/build runner changed.')
    spec = importlib.util.spec_from_file_location('r12_accepted_terra_staging', BASE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # The accepted functions snapshot/build this package, with the same
    # original eight application units and explicitly pinned host authorities.
    module.PACKAGE = PACKAGE
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    stages = parser.add_subparsers(dest='stage', required=True)
    builder = stages.add_parser('build')
    builder.add_argument('--assets', type=Path, required=True)
    builder.add_argument('--host', type=Path, required=True)
    runner = stages.add_parser('run')
    runner.add_argument('--build', type=Path, required=True)
    runner.add_argument('--case', choices=CASES, required=True)
    runner.add_argument('--predecessor', type=Path)
    for stage in (builder, runner):
        stage.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = load_base()
    base.require(base.sha(PACKAGE / 'PROTOCOL.md') == PROTOCOL_SHA, 'Protocol differs from the accepted contract.')
    output = args.output.resolve()
    private = (ROOT / '.artifacts/r12-propagation-20261018').resolve()
    base.require(output.is_relative_to(private) and output != private, 'Use a new private R12 attempt directory.')
    output.mkdir(parents=True, exist_ok=False)
    base.snapshot(output)
    shared = output / 'shared-inputs'
    shared.mkdir()
    shutil.copy2(BASE_PATH, shared / 'terra-run.py')
    base.save(output / 'shared-inputs.json', {'runner_sha256': BASE_SHA,
              'source': BASE_PATH.relative_to(ROOT).as_posix(), 'frozen_copy': 'shared-inputs/terra-run.py'})
    assignment_sha = None
    try:
        if args.stage == 'build':
            result = base.build(args, output)
        else:
            build = args.build.resolve(strict=True)
            accepted = base.read(build / 'receipt.json')
            base.require(accepted.get('shared_runner_sha256') == BASE_SHA,
                         'The build used a different shared runner.')
            base.require(base.sha(build / 'shared-inputs/terra-run.py') == BASE_SHA,
                         'The build shared-runner snapshot changed.')
            previous_hash = None
            if args.predecessor:
                previous = args.predecessor.resolve(strict=True)
                prev = base.read(previous / 'receipt.json')
                previous_hash = base.sha(previous / 'receipt.json')
                base.require(prev.get('case') == args.case and prev.get('arm') == 'L0',
                             'Reopen must use this case\'s actual revise predecessor.')
                base.require(base.sha(previous / 'assignment.json') == prev.get('assignment_sha256'),
                             'Predecessor assignment changed.')
                base.require(prev.get('shared_runner_sha256') == BASE_SHA,
                             'Predecessor used a different shared runner.')
            operator, condition = args.case.split('-')
            assignment = {'Case': args.case, 'CaseOrdinal': CASES.index(args.case) + 1,
                          'Operator': operator, 'Condition': condition,
                          'Role': 'reopen' if args.predecessor else 'revise',
                          'Arm': 'L1' if args.predecessor else 'L0',
                          'ProtocolSha256': PROTOCOL_SHA,
                          'PredecessorReceiptSha256': previous_hash}
            base.save(output / 'assignment.json', assignment)
            assignment_sha = base.sha(output / 'assignment.json')
            result = base.run(args, output)
            result.update({'case': args.case, 'assignment': assignment,
                           'assignment_sha256': assignment_sha,
                           'assignment_unchanged': base.sha(output / 'assignment.json') == assignment_sha})
            summary = result.get('summary') or {}
            bound = (summary.get('Case') == args.case and summary.get('Arm') == assignment['Arm']
                     and summary.get('AssignmentSha256') == assignment_sha
                     and result['assignment_unchanged'])
            result['assignment_observed_and_bound'] = bound
            result['complete_observation_and_save'] &= bound
        result['shared_runner_sha256'] = BASE_SHA
        result['shared_runner_unchanged'] = (base.sha(BASE_PATH) == BASE_SHA
                                             and base.sha(shared / 'terra-run.py') == BASE_SHA)
        readiness = 'ready_for_parent_review' if args.stage == 'build' else 'complete_observation_and_save'
        result[readiness] &= result['shared_runner_unchanged']
        base.save(output / 'receipt.json', result)
    except Exception as error:
        base.save(output / 'preparation-error.json', {'type': type(error).__name__, 'error': str(error),
                  'stage': args.stage, 'assignment_sha256': assignment_sha})
        raise
    print(json.dumps({'stage': args.stage, 'output': str(output), 'ready': result[readiness],
                      'case': result.get('case'), 'arm': result.get('arm'),
                      'receipt_sha256': base.sha(output / 'receipt.json')}))
    return 0 if result[readiness] else 2


if __name__ == '__main__':
    raise SystemExit(main())
