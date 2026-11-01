# S180 independent correlation reconstruction, 2026-10-26

**Status: bounded calculation and AI maintainer review completed.** One
execution of the unchanged, previously declared check produced 150 cell
statuses: 146 computable correlations and four uncomputable cells. This is a
bounded independent arithmetic reconstruction, not execution of the authors'
software or reproduction of their complete published analysis. The exact
publication-producing invocation remains unknown.

## Question and declared boundary

The [artifact audit](S180-practitioner-beliefs-artifact.md) identified two
conditional discrepancies: significance-to-zero reporting, and broader total-like
`ActMin` in place of the paper's declared coding-time denominator. The check asks
how those choices affect the retained data's correlation summaries. Its plan and
script were written before either earlier failed setup attempt, preserved on C:,
and copied unchanged into the fresh calculation folder. No outcomes informed
new filters, exclusions, thresholds or alternative statistical tests.

The input is the official [Zenodo v1.0.0 archive](https://zenodo.org/records/4553435),
SHA-256 `ffd1d09150dd3eede84bcb1dd5f4b3e7dc1656d7f38369b72f33deace23fdfb1`.
The selected member is `snaraya7-SE_Beliefs-e911647/data/filtered_data.csv`,
SHA-256 `395555d171218db7cf99dde48e886d8bbb198776e462bdb538c40f4da6571cb7`.
It contains 13,560 rows, 1,356 developers and ten distinct developer-task rows
per developer. Every task has the same five language-group sizes shown below.
Those are repeated training observations, not 13,560 independent people. The
new script checks the task-language cell counts; it does not independently
recheck stable developer-language identity. The developer-language counts come
from the earlier accepted static audit of the same verified CSV bytes.

## Calculation

For each of five languages and tasks 1A through 10A, calculate two-sided Spearman
correlation for:

1. `ActDefInjDsgn + ActDefInjCode` versus `ActDefRemTest` (B3).
2. `60 * ActLOC / ActMin` versus `ActDefInjCode` (B4 archived metric).
3. `60 * ActLOC / ActMinCode` versus `ActDefInjCode` (B4 coding-time sensitivity).

Retain raw rho and p, then separately apply the archived reporting rule: retain
rho if p < .01, otherwise report zero. The numerical environment is Python
3.12.2, SciPy 1.14.1 and NumPy 2.2.6. This pins the new calculation, not the
historical environment. A second implementation in the same script calculates
average ranks directly and checks each rho against their Pearson correlation
at absolute tolerance 1e-12; this was not manual or human calculation. The fresh
preflight checked negative monotonic data, a tied example with explicit expected
ranks, and SciPy's documented two-sided worked example.

The independent expression `60 * ActLOC / time` is algebraically equivalent to
the archive's `ActLOC / (ActMin / 60)`, but binary floating-point operation order
need not produce identical low-order values or exact ties. Possible effects on
ranks and p-values were not quantified; no post-outcome arithmetic sensitivity
or replacement run was performed. These are results of the unchanged declared
calculation, not bitwise execution of the archived program.

The p-values are the library's asymptotic approximations. SciPy cautions that
they are reliable only with large samples and suggests permutation tests for
smaller samples; four of the five language groups have fewer than 500
observations. No permutation test or multiplicity adjustment was substituted:
the purpose here is to reconstruct the declared reporting operation, not to
validate population inference. [SciPy 1.14.1 method documentation](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats.spearmanr.html).

The plan marks a whole cell uncomputable when an input is missing/nonfinite,
a time denominator is nonpositive or a vector is constant. It never silently
removes the affected row. A language-condition median is reported only when
all ten prescribed task cells are computable. Medians below summarize the ten
task coefficients; they are neither pooled developer-level coefficients nor
effects from independent task cohorts.

## Results

| Condition | Language | n per task | Computable tasks / 10 | Raw median rho | Median after rule | Coefficients set to zero |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| B3: injected design + code defects / test removals | C | 509 | 10/10 | 0.611995 | 0.611995 | 0/10 |
| B3: injected design + code defects / test removals | C++ | 327 | 10/10 | 0.573364 | 0.573364 | 0/10 |
| B3: injected design + code defects / test removals | C# | 201 | 10/10 | 0.625269 | 0.625269 | 0/10 |
| B3: injected design + code defects / test removals | Java | 163 | 10/10 | 0.497060 | 0.497060 | 0/10 |
| B3: injected design + code defects / test removals | VB | 156 | 10/10 | 0.659929 | 0.659929 | 0/10 |
| B4: LOC per ActMin hour / coding defects | C | 509 | 10/10 | -0.111298 | -0.062056 | 5/10 |
| B4: LOC per ActMin hour / coding defects | C++ | 327 | 10/10 | 0.006356 | 0.000000 | 6/10 |
| B4: LOC per ActMin hour / coding defects | C# | 201 | 10/10 | -0.102162 | 0.000000 | 8/10 |
| B4: LOC per ActMin hour / coding defects | Java | 163 | 10/10 | -0.150640 | 0.000000 | 7/10 |
| B4: LOC per ActMin hour / coding defects | VB | 156 | 10/10 | -0.134722 | 0.000000 | 9/10 |
| B4: LOC per coding hour / coding defects | C | 509 | 9/10 | not computed | not computed | no complete-group summary |
| B4: LOC per coding hour / coding defects | C++ | 327 | 8/10 | not computed | not computed | no complete-group summary |
| B4: LOC per coding hour / coding defects | C# | 201 | 10/10 | -0.080117 | 0.000000 | 9/10 |
| B4: LOC per coding hour / coding defects | Java | 163 | 10/10 | -0.076798 | 0.000000 | 9/10 |
| B4: LOC per coding hour / coding defects | VB | 156 | 9/10 | not computed | not computed | no complete-group summary |

B3 has no coefficients replaced by the p-value rule. Its positive associations
remain visible. The C++ median is about .573, below .6; this agrees with the
previous reading's qualitative Figure 6 discrepancy with the prose, but does
not authenticate the historical plot-producing run. Association between two
retrospective defect counts still does not identify an effect of early quality
assurance on rework.

For B4 using `ActMin`, the rule replaces 35 of 50 coefficients with zero. Four
of five language medians become exactly zero, including groups with negative
raw medians. C's median changes from about -.111 to -.062; C++'s raw median
is already close to zero. The rule's exact zeros are therefore not evidence
of exact zero association or practical equivalence. These summaries also do
not establish the inverse causal claim that productivity causes defects.

The coding-time sensitivity preserves four uncomputable cells: C/4A (n=509),
C++/3A (n=327), C++/5A (n=327), and VB/6A (n=156), each because a denominator
is nonpositive. No row was dropped and no ten-task median was supplied for
C, C++ or VB. C# and Java have all ten cells; their raw medians and significance
screens differ from the broader-time metric as shown. The calculation does not
replace the paper's unknown actual metric with either reconstructed result.

The data-definition checks repeat the earlier static findings: `ActMin` differs
from `ActMinCode` in all 13,560 rows, equals the sum of the eight named PSP phase
columns in 12,881 rows, and is nonpositive in zero rows; `ActMinCode` is
nonpositive in four. These explain why choosing a time denominator is a
substantive measurement choice, not a harmless relabeling.

## Attempts, integrity and retained outputs

The two prior attempts failed before data access: first missing SciPy, then
null bytes in the installed A: dependency. They remain failed attempts. The
[storage return](../../workspace-integrity-return-2026-10-26.md) is unchanged:
A: remains stopped and no native experiment was resumed.

For this distinct calculation, C: reported Healthy/OK with 23,255,916,544 free
bytes. The plan, script and archive were copied to
`C:/Users/hadri/nu-value-calculations/20261026-s180-correlation-01/`; two source
reads and each destination agreed. The script SHA-256 remains
`5cb57791daa874464aa3ff1e591656fcb402bb2379bc16967cbb28a8c9555b2a`, and the plan
SHA-256 remains `f1519dcca01413cd3ccc20aee81c69dc1e6989b08148fee703179accfe01429c`.
No preserved source or earlier failed dependency was overwritten.

The launch wrappers did not all specify a working directory and therefore
inherited the conversation's A: directory. The numerical child used isolated
import mode and explicit C: script, package, input and output paths. This record
establishes their correspondence; it does not claim a process-wide filesystem
trace or that the wrappers' working directory was C:. No A: dataset, application
or failed package was supplied to the calculation.

Fresh Windows CPython 3.12 wheels came from official PyPI release records and
matched their published hashes:

- [NumPy 2.2.6 metadata](https://pypi.org/pypi/numpy/2.2.6/json): wheel SHA-256
  `c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2`.
- [SciPy 1.14.1 metadata](https://pypi.org/pypi/scipy/1.14.1/json): wheel SHA-256
  `2ff38e22128e6c03ff73b6bb0f85f897d2362f8c052e3b8ad00532198fbdae3f`.

All 2,393 unchanged wheel members matched their installed bytes. The hashed
entries listed in the two installer-rewritten RECORD files were checked
separately; each RECORD file's own entry remains unhashed. The first RECORD
validation exited 1 because two generated command-launcher paths resolved
outside the new target under the installer's relative layout. It read no
outside file and found no hash mismatch. An explicit mapping to the two observed
`packages/bin` locations then verified their recorded hashes; all 2,401 hashed
installed RECORD entries were accounted for. This validation failure and its
correction are retained. The 1,288 unhashed entries are those two RECORD files
and 1,286 installer-generated bytecode files. That bytecode was bypassed through
a fresh cache prefix with bytecode writing disabled.

The fresh preflight and the one unchanged analysis invocation both exited 0;
the analysis ran from 2026-10-25 17:30:10.998976 to 17:30:17.331173 UTC
(October 26 HKT). No archived script, batch file or notebook was executed.
The complete 150-cell JSON, raw p-values, computed/invalid dispositions,
commands, environment manifests and logs remain in the calculation folder.
Result SHA-256:
`46a6a3ec9ffb6724713be71d446381c5407a0715930567e94b5b8c65b368ad0b`.
This digest was verified after execution and by the reviewer; the original
process receipt records exit status and script identity but does not itself
seal the result digest. Output/receipt correspondence is additionally checked
against the retained stdout summaries, without rerunning correlations.

A separate Sol High AI maintainer reviewed the plan, formulas, all 150 stored
cells, all 15 summary objects, hashes and attempt records, and selected archived
method source. The parent applied its wording/provenance corrections and owns
acceptance. That review neither reran the correlations nor constituted a human
review or a new full-paper reading. Exact coverage and the original review are
retained under the calculation folder's `review/` directory.

## Consequence and limits

The significance-to-zero concern is now numerically demonstrated for the
specified data and new environment, instead of resting only on code inspection.
The denominator sensitivity is partly computable under the prespecified rule;
its invalid cells remain visible. This strengthens the [S180 reading](S180-practitioner-beliefs.md)
and R14's requirement to bind the measured variable and reporting operation
before treating a null summary as practice guidance.

It does not complete Scott-Knott, verify the journal version, recover the
publication's actual software/commands, or reproduce the published analysis
end to end. No Nu comparison, task prevalence, causal language effect, agent
maintenance benefit or steering result follows. The reading count is unchanged;
no new paper, participant cohort or independent primary study is credited.

The once-only source segment `s180_correlation_reconstruction_20261026` records
the exact archive, versioned method documentation and two package-release
identities: four included sources, no excluded/skipped entries or missing
reasons, an untruncated report and retrieval_unlinked=false. Retrieved count is
null. These are provenance units, not four papers; unchanged earlier source
decisions were not resubmitted as a new reading screen.
