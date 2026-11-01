# CI validation scope

The user requested omitting irrelevant older checks or restructuring CI on
2026-09-14. This changes engineering validation scheduling, not scientific
protocols, frozen results or execution authority.

## Why restructure

The literature-only publication `5d9ad460738112a8dfe55f2de8eaad74bef35823`
passed [CI 34774846703](https://github.com/Happypig375/interactive-software-evolution/actions/runs/34774846703),
attempt 1: Linux took 14m37s and Windows 16m21s. Both repeated .NET construction,
historical workstream checks and, on Linux, sandbox/container checks despite
only AGENTS.md, PLAN.md and a research note changing.

The older checks are not all obsolete. H preparation, E3a and historical
C3/D/E2 artifacts share helpers and source inputs. Their existing full suite
is retained; clearly unrelated pushes do not need to run it.

## Routing

[ci_scope.py](../scripts/ci_scope.py) owns the explicit path rules;
[ci.yml](../.github/workflows/ci.yml) owns the jobs. No external path-filter
action, service, dependency graph engine or new package is required.

| Change/event | Selected validation |
| --- | --- |
| Ordinary known-range branch push changing only root README.md, AGENTS.md, PLAN.md, references.md or Markdown under docs/ | Fast routing regressions, changed-Markdown UTF-8 and Git whitespace checks; no ISE install, .NET or Docker. |
| Same kind of push confined to the maintenance allowlist, optionally plus the prose above | Fast checks, then all unit tests and the trusted maintenance fixture/fault/inherited-failure audit on Linux and Windows. |
| Shared implementation, CI/configuration, other benchmark/protocol/report inputs, or any unrecognized path | Fast checks plus the unchanged full Linux/Windows validation matrix. |
| Pull request, workflow_dispatch, tag, new-branch or forced push, malformed/missing event data, unavailable base/diff | Full matrix; uncertainty never chooses a skip. |

The maintenance allowlist contains its module, CLI and test file; construction
metadata and contract; guidance and episode Markdown; cases/faults JSON; seed
files; and reference/fault patches. Other new inputs remain full-suite changes
until their isolation is established. Protocol Markdown, benchmark task prompts
and H contracts are **not** ordinary prose for this policy. Even currently
non-executable subtree READMEs and protocol amendments conservatively use the
full route. File extensions alone do not determine scope.

Maintenance uses shared `h_fixtures`, `h0` and E2 tokenizer definitions. Changes
to those helpers select full CI. If another workstream starts consuming an
allowlisted path, update the rules and tests in that same implementation change.

The workflow always starts, rather than using workflow-level path exclusions.
Job conditions select the expensive work. This retains an exact-commit CI result;
a green prose-only run means the **selected fast checks** passed, not that the
runtime or old protocols were revalidated. GitHub distinguishes job skips from
workflow path-filter skips; the latter can leave required checks pending.
[Job conditions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-jobs-with-conditions),
[workflow path filters](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onpushpull_requestpull_request_targetpathspaths-ignore).

The scope step compares the entire push's before/after commits with a local
NUL-delimited Git diff. It does not use only HEAD's parent, a truncated webhook
file list or a paginated changed-files API. Rename detection is disabled so both
the old and new paths affect the decision. Deleted paths are classified too.
Detection errors fall back to full validation; failed fast checks keep the
existing validate-linux/validate-windows jobs red through their explicit guard.
An absent or unrecognized scope output also defaults to the full matrix.
No failed job is ignored or converted into a pass.

The fast prose checks do not validate links, Markdown rendering, scientific
claims or approval. Human review and the live-execution hold remain unchanged.

## Reproduction and full validation

```text
python -m unittest discover -s tests -p test_ci_scope.py -v
python scripts/ci_scope.py --base 49caefdf0b08029e2b5eeb81b958bfde3fdab331 --head 5d9ad460738112a8dfe55f2de8eaad74bef35823
```

The second command selects `docs` for the three-file literature publication.
It checks changed Markdown in the current checkout, so use a checkout matching
the selected head when reproducing content validation, not just classification.
Regression coverage includes the explicit input boundaries, ordinary versus
conservative events, unknown bases, more than one API page of changes,
multi-commit pushes, renames, deletions and malformed UTF-8.

Use the existing Actions **Run workflow** entry point for a full model-free
validation. Leave `run_e2` false unless the optional frozen E2 baseline is
specifically wanted and within the applicable authorization. Its existing
manual-only default, prerequisites, image, network isolation and audit commands
are unchanged. No OAuth staging or model/candidate dispatch is added by CI.

## Review and evidence

The dependency mapping was extracted read-only by a Luna Max worker. The main
agent owns the classifier, workflow integration and acceptance. A separate
Sol High AI review identified an empty/unknown-output fail-open case before
publication. The full-job predicates were corrected and workflow-contract
regression coverage added. The same reviewer rechecked the correction and found
no remaining material issue in that bounded scope. All 11 focused tests and
the three-file literature-commit replay passed locally; staged whitespace is
checked before publication. No local full-suite run is claimed. This
is not human scientific approval.
The source inspected before this change is `5d9ad460738112a8dfe55f2de8eaad74bef35823`.
Local routing tests and replay checks do not establish actual GitHub execution;
verify CI on the containing implementation commit after push. Because the CI
implementation itself changed, that publication selects the full matrix.

No historical validation command or archived experiment was deleted. Skipped
checks must be described as skipped, and actual CI scope must accompany later
validation claims. This policy adds no experimental allocation or treatment.

## Windows job deadline, 2026-10-15

At `f81a7a677aae5d2472ca70bc1868adeb4ad5ac32`,
[run 38699292554](https://github.com/Happypig375/interactive-software-evolution/actions/runs/38699292554)
passed Linux validation. Windows passed every preceding check but was cancelled
at its 20-minute job deadline during the final C3 deterministic validation.
That interrupted check has no completed result. The Windows job allowance is
now 30 minutes to accommodate the existing suite; its commands, assertions,
per-process limits and scope rules are unchanged.

The containing commit `1f69fba5f446c654db7290fa9767c47d73125a14` passed
[run 38704367773](https://github.com/Happypig375/interactive-software-evolution/actions/runs/38704367773):
scope checks, full Linux validation (14m19s), and full Windows validation
(17m15s). The separate maintenance job and optional E2 baseline were skipped
under the full route. This completed run does not supply a result for the
interrupted check on the earlier commit.

The later R10/literature commit
`b596f39fb0d023155e22223f531c3a5f134b6b83` passed
[run 38711962041](https://github.com/Happypig375/interactive-software-evolution/actions/runs/38711962041):
scope checks, full Linux validation (9m29s), and full Windows validation
(15m30s). Maintenance and the optional E2 baseline were skipped under the full
route. This validates the repository checks at that head; the R10 record owns
its separate bounded runtime evidence.

## R10 schema publication, 2026-10-16

The R10 schema package at `262ec34d12a07df6dc804000c9884601e494632c` selected
the full route. [Run 38789012172](https://github.com/Happypig375/interactive-software-evolution/actions/runs/38789012172)
passed Linux on the first attempt and Windows on the unchanged failed-job retry.
The separate maintenance job and optional E2 baseline were skipped. This is
repository validation; the [R10 execution record](nu-schema-reload-feasibility-2026-10-16.md)
owns its separate native observations.

The first Windows attempt completed 548 unit tests with one error: the existing
`test_python_probe_failure_starts_no_proxy_or_artifacts` exceeded its 45-second
outer PowerShell deadline. The exact committed test and launcher passed a local
targeted reproduction without changing files, assertions or deadlines. The
failed Windows job was retried once after the workflow finished; the initial
timeout remains an unexplained failed check. No scientific trial was rerun.
Original job logs, the local test receipt and both CI attempts are retained
privately under `.artifacts/r10-schema-20261016/ci/`.

## R12 Terra Firma revision publication, 2026-10-18

The package and result publication
`aaacd5703f710748e80e00936e6355cd1b029413` selected the full route.
[Run 39130754669](https://github.com/Happypig375/interactive-software-evolution/actions/runs/39130754669)
passed scope checks, Linux validation (9m02s), and Windows validation
(15m15s), all on the first attempt. The separate maintenance job and optional
E2 baseline were skipped under that route. The unchanged historical suite's
success validates the repository checks at this head; it does not complete
the [R12 local-condition comparison](nu-terra-firma-revision-feasibility-2026-10-18.md)
or resolve the [workspace integrity return](workspace-integrity-return-2026-10-18.md).
No native experiment ran from the temporary C: publication checkout.

## Revalidated R12 continuation and S305 reconciliation, 2026-10-18

The combined publication `3f1d95b00e887c2305662b853b9828570325aff8`
selected the full route because its changes include experiment results and
the continuation receipt. [Run 39140422091](https://github.com/Happypig375/interactive-software-evolution/actions/runs/39140422091)
passed scope checks, full Linux validation (14m37s) and full Windows validation
(16m30s), all on the first attempt. The separate maintenance job and optional
E2 baseline were skipped under that route.

This validates repository checks at that commit. The
[R12 execution record](nu-terra-firma-revision-feasibility-2026-10-18.md) and
[continuation receipt](../experiments/nu-r12-terra-revision/continuation-receipt.json)
own the separate native evidence, including the retained invalid startup.
The [S305 journal reconstruction](literature/full-reading/S305-problem-centered-design-journal-reading-2026-10-18.md)
owns reading coverage and edition limits. CI neither establishes scientific
benefit nor resumes the R02/R10 returns.

## R12 material-intent component publication, 2026-10-23

The component and source-evidence publication
`ac828becb971d6be75bf148adff6613065b6aadf` selected the full route for its sixteen
changed paths. [Run 39916970418](https://github.com/Happypig375/interactive-software-evolution/actions/runs/39916970418)
passed scope checks and the full Linux and Windows jobs on the first attempt.
The new ordinary R12 material-intent control step passed on both platforms.
Maintenance and the optional E2 baseline were skipped under the full route.

Local checks passed eleven routing tests, the exact new root-invoked .NET
command, strict UTF-8, whitespace and 27 introduced local links/anchors. The
component's separate [construction record](../experiments/nu-r12-material-intent/RESULTS.md)
retains two failed builds, the failed fixture, the accepted 54 positive and
27 expected-rejection checks, and independent review. No Nu engine process,
participant, task-solving model candidate or native persistence experiment is
validated by these repository checks. R02/R10 remain stopped.

## R12 native protocol publication, 2026-10-23

The four-path protocol and agenda publication
`0ecf2414d005b2df6e67f5ccd0ca7c4f8ea611a1` selected full validation because
the [frozen protocol](../experiments/nu-r12-material-intent-native/PROTOCOL.md)
is under `experiments/`. [Run 39925993293](https://github.com/Happypig375/interactive-software-evolution/actions/runs/39925993293)
passed scope, Linux (15m06s) and Windows (16m50s) on its first attempt.
The separate maintenance job and optional E2 baseline were skipped.
Local strict UTF-8, whitespace and all 17 introduced local links/anchors passed.

The native implementation was not in this commit. Its local build, control
results, independent readiness review and any later Nu execution require their
own evidence. Full repository CI does not accept that package or establish
persistence, comparative benefit or survey completion.
