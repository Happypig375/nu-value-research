# S312 — Replay-derived traces and higher reported agent-repair counts

Jiahong Xiang, Xiaoyang Xu, Xiaopan Chu, Hongliang Tian, and Yuqun Zhang,
*Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis*,
[arXiv:2604.24212v1](https://arxiv.org/abs/2604.24212v1), related published
DOI [10.1145/3797126](https://doi.org/10.1145/3797126).

## Identity and coverage

The official arXiv record identifies v1 as submitted 27 April 2026 at
09:18:42 UTC. The selected edition was registered before body reading as a
Zotero `preprint` in collection **`PKLXQNEE`**. Verified parent
**`B6V8URKN` v8273** records `repository: arXiv`,
`archiveID: arXiv:2604.24212v1`, and the related PACMSE/FSE DOI. Exact PDF
attachment **`M9CEPSUX` v8276** is 2,272,386 bytes, 22 pages, MD5
`342431f41745fbf25d6c25def23aa003`, and SHA-256
`06142ac31471ab675fcb8351751533207615b9b502560acfc83d30112394f7e1`.
The downloaded, acquisition-staged, and Zotero-stored bytes agree.

All 22 pages were read textually and visually, including Figures 1–9,
Tables 1–4, Algorithm 1, and all 62 references. Poppler reported no display
font for `Symbol`; formulas, tables, and figures were checked in page renders.
The related Zenodo v1 artifact was inspected passively, without executing its
code or reproducing the experiments. Published-version byte equivalence was
not checked.

## Method and endpoint

ADI is a Python function-level dynamic-analysis interface for autonomous
coding agents. Its Frame Lifetime Trace (FLT) records an invocation's caller,
entry arguments, return or exception, ordered statements, state changes, and
callee identifiers. High-level commands expose breakpoints, forward and
backward frame navigation, step-in and step-out, call trees, and statement
injection.

This is replay-based inspection rather than retained-process history. ADI
first records a lightweight sequence of frames; when an agent requests a
particular FLT, it re-executes the selected program and frame. Its `execute`
command also reruns the program. The evaluated agent first constructs a
reproduction script from an issue report, then chooses functions and frames,
uses the trace, edits code, and verifies its patch. The benchmark's developer
test patch is withheld from the agent and used for final scoring.

The endpoint is SWE-bench Pass@1: a generated patch must apply and pass the
held-out developer tests in the official Docker evaluation. That is a repair
endpoint, stronger than localization or a proposed edit. It does not measure
continued execution of an old interactive world, preservation of native or
external effects, or human maintenance benefit.

Lite and Verified are already curated 300/500-task subsets of SWE-bench, not
an unrestricted population of maintenance work. The artifact records
incomplete FramePilot tasks while the published rate keeps the full benchmark
denominator: 1–29 incomplete tasks across the four Lite runs and 10–29 across
the four Verified runs. The paper does not report matched incompletion or
failure-cause distributions for BaseAgent and PDBAgent. Analyses of 62 tasks
uniquely resolved by FramePilot are selected success-case analyses and must
not be generalized to all tasks.

## Comparisons and results

The paper reports a shared ReAct framework and broad workflow for FramePilot,
BaseAgent and PDBAgent, with common benchmark/model conditions, a USD 4 API
budget per task and temperature 0. BaseAgent receives ordinary file and shell
tools, PDBAgent adds low-level nonblocking PDB, and FramePilot adds ADI.

The exact deposited prompts differ materially. FramePilot gives a concise
workflow requiring FLT analysis and ADI-specific guidance. BaseAgent has a
different system/user prompt and permits skipping reproduction when the
environment is difficult; PDBAgent adds its own debugging and comprehensive-test
stages. The artifact README says four stages but enumerates five. Thus the
available evidence supports comparison of bundled configurations under
paper-reported common conditions, not a clean isolation of trace information
with all other prompt/workflow instructions held fixed.

On SWE-bench Verified, reported resolved counts for Base/PDB/FramePilot are:

| Model | Base | PDB | ADI |
| --- | ---: | ---: | ---: |
| Claude Sonnet 3.7 | 275 | 279 | 319 |
| Claude 3.5 Sonnet | 222 | 225 | 256 |
| GPT-4o | 163 | 156 | 181 |
| Qwen3 | 146 | 142 | 157 |

PDB is therefore mixed: small favorable differences for the two Claude
models and lower resolved counts than BaseAgent for GPT-4o and Qwen3. The ADI-enabled configuration has
higher reported counts than both other variants for all four models. FramePilot's Verified
Pass@1 is 63.8%, 51.2%, 36.2%, and 31.4% respectively. The paper reports that
PDB was attempted on 191 Claude 3.7 tasks, averaged 10.1 `next` operations,
and was abandoned in 53% of attempts; the released artifact contains no
trajectories with which to reconstruct this analysis.

FramePilot's 319/500 with Claude 3.7 is also compared to Claude Tools at
316/500. That is a system-level leaderboard comparator with a different,
high-investment implementation, not a matched information treatment; its
reported calculated cost of USD 3.95 cannot isolate ADI's effect.

Two host agents also have higher reported counts in ADI-enabled configurations. On
Verified, mini-SWE-agent rises from 264 to 292 resolved tasks with Claude 3.7
and from 108 to 128 with GPT-4o; AutoCodeRover rises from 231 to 248 with
Claude 3.5 and from 192 to 204 with GPT-4o. The paper's 6.2–18.5% range is the
relative increase in resolved counts, equivalent to 2.4–5.6 percentage
points on the 500-task denominator.

The cumulative FLT ablation on SWE-bench Lite with Claude 3.7 reports
130 resolved tasks for BaseAgent, 142 after adding statement traces, 145
after entry arguments, and 152 after return information. This narrows the
information contribution, but the increments are cumulative, with no
reported repeated runs, confidence intervals, or significance tests.

## Cost and adverse boundaries

The selected FramePilot run costs are higher than BaseAgent in every reported
same-model comparison: USD 1.28 versus 1.02 for Claude 3.7, 0.58 versus 0.49 for Claude
3.5, and 0.93 versus 0.87 for GPT-4o; Qwen3 cost is unreported. They are lower
than the PDBAgent values of 1.62, 0.89, and 1.09. The paper measures the
official failing tests at 0.68 seconds without ADI and 0.87 seconds while
tracing the buggy function. ADI re-executes about 5.19 times per task, for
roughly four seconds of reported execution time. These figures are API spend
and selected tracing runtime, not total wall time or acquisition, setup,
integration, container, debugging-tool development, and verification work.

The implementation traces only a selected Python frame through `sys.settrace`,
does not trace external libraries, caps call-tree depth at three, and
compresses loops by retaining their first and last iterations. Re-execution
can diverge for nondeterministic programs. The paper also identifies weaker
coverage for concurrency, memory leaks, and bugs spanning many shallow calls.
No human study or non-Python evaluation is reported.

## Artifact check

The publication artifact is
[Zenodo v1, DOI 10.5281/zenodo.19728388](https://doi.org/10.5281/zenodo.19728388):
16,260,997 bytes, MD5 `9040ebbc831090029072fe9dc5a2fdf2`, SHA-256
`cbfb41fc85f9e4ded1881a0ce44082d940fcc72ec39bd98c746e5a03e4427850`.
Its 505 files include implementation variants, benchmark data, and eight
FramePilot patch/result pairs. The released resolved counts and completed-ID
partitions match the eight FramePilot rows in the paper. The archive has no
run trajectories or execution-log data and no BaseAgent, PDBAgent, mini-SWE-agent, or
AutoCodeRover result bundles, so those comparisons and costs cannot be
independently reconstructed from this deposit.

The final patch rows also preserve a useful scoring distinction: agents
self-report success much more often than held-out evaluation resolves a task.
For example, the Verified Claude 3.7 file contains 490 positive agent reports
but 319 held-out resolved patches. Final scoring must therefore remain
separate from agent belief.

Two provenance discrepancies remain unresolved. All eight summary files have
`submitted_ids` list lengths inconsistent with their stated
`submitted_instances`, sometimes exceeding the benchmark size. More
consequentially, paper §5.3.2 states temperature 0, while the exact Zenodo v1
query modules for FramePilot, BaseAgent and PDBAgent all pass
`temperature=0.7` at line 137. The archive contains no run manifests that bind
every published row to a source revision and invocation, so neither setting
should be silently treated as the executed one. The paper/README also name a
`call-tree` command where the deposited FramePilot prompt/API uses `call-graph`;
this further limits exact source-to-run correspondence without changing the
high-level navigation method.

## Consequence for R08, R03, and R06

For R08, S312 supports a concrete ordinary-agent access condition: source and
shell access, a reproduction script, callable trace/navigation commands,
patch tools, repeated executions, and held-out tests. Ordinary-tool and
low-level-debugger configurations are credible comparator families; PDB's
mixed results remain relevant adverse evidence. The reported comparison and
nonidentical deposited prompts bundle dynamic information, tool implementation,
workflow and reruns. A future study must count those changes and either
compare the complete workflows or independently control the information
contrast; it cannot attribute the entire reported difference to history.

For R03, ADI is a repair aid when the relevant failure can be reproduced in
Python. It does not recover the retained Gaia episode's absent predecessor
root or original entity names, resume its old native world, or preserve
contacts, audio, framebuffer state, and external effects. Calling FLT
“history” would change the information condition: it is generated by rerun.
Ordinary Gaia serialization invoked through Interactive can itself create a
retained snapshot, so snapshot creation authority and observation side
effects require their own accounting. Recovery to such a checkpoint,
diagnosis, applied repair, and verified continuation remain separate stages;
S312 supports only the reproducible Python repair path.

For R06, S312 motivates recording repair outcome separately from trace access
and counting reruns, tool calls, integration, and final verification. Its API
spend and small selected runtime measurements do not replace the current Nu
component timings or establish lower total maintenance work.

## Integration review

The October 23 delegated reading supplies complete page/visual coverage.
The October 25 substantive review checked decision-relevant PDF pages 1 and
7–19, selected rendered figures/tables, the exact ZIP inventory, eight result
and patch pairs, and principal prompts/query/API modules. It verified the
numeric claims and required the prompt-comparability and temperature
corrections above. Parent inspected the three workflow prompts and all three
temperature assignments. This is AI evidence review, not another study,
full-reading increment, human sign-off or benchmark reproduction. Original
packet and review remain preserved privately; the selected edition is unchanged.

## References

Xiang, J., Xu, X., Chu, X., Tian, H., & Zhang, Y. (2026). *Empowering
autonomous debugging agents with efficient dynamic analysis* (arXiv:2604.24212v1).
arXiv. https://doi.org/10.48550/arXiv.2604.24212

Xiang, J., Xu, X., Chu, X., Tian, H., & Zhang, Y. (2026). *FSE26 artifact*.
Zenodo. https://doi.org/10.5281/zenodo.19728388
