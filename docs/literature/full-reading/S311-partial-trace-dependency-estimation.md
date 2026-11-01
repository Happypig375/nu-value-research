# S311 — partial-trace dependency estimation is a rescue method, not retained history

Yunrui Pei, Hongshu Wang, Wenjie Zhang, Yun Lin, Weiyu Kong, and Jin Song
Dong, *LLM as an Execution Estimator: Recovering Missing Dependency for
Practical Time-travelling Debugging*,
[arXiv:2508.18721v5](https://arxiv.org/abs/2508.18721v5).

## Identity and coverage

The official arXiv record says v1 was submitted 26 August 2025 and v5 was
revised 3 September 2025 at 14:34:30 UTC. The selected edition was registered before body reading as a Zotero
`preprint` in collection **`PKLXQNEE`**. Final verified parent
**`YNG9EI88` v8260** has `repository: arXiv` and
`archiveID: arXiv:2508.18721v5`. Exact official PDF attachment
**`HCLDBPF3` v8259** is 1,940,313 bytes, 15 pages, MD5
`ff36df7a1d59e6e44870aa8d879dc864`, and SHA-256
`67dc6d169c39e5b89a147e2c77ee05b7edb2f6d0c9824476b0e0811913150855`.
Downloaded and Zotero-stored bytes agree.

All 15 pages were read textually and visually, including Figures 1–10,
Tables 1–6, Algorithms 1–3, Appendix A's prompts, and all 58 references.
Poppler reported an embedded-font mismatch and a missing Symbol display font;
the formulas, diagrams, and table cells were checked in the page renders. No
author source, benchmark rows, model logs, or executable artifact was acquired
or run.

This remains a preprint. The PDF contains ACM-template debris: placeholder
conference/DOI text, 2018 Woodstock headings, “Trovato et al.” running heads,
and a received/revised/accepted line dated 2007/2009. Those lines are not
publication metadata; the official arXiv version history governs the identity.

## Method and endpoint

RecovSlicing receives a partially instrumented Java execution trace, source
code, a query step, and a query variable. It recovers an unrecorded object
path/value, infers aliases between recovered and recorded variables, and
searches backward for a defining step. It combines static checks with LLM
calls for library or external-code cases. Adaptive examples come from small
similar programs that the system synthesizes and fully instruments.

The output is an **estimated dynamic data-dependency edge**. When the actual
write occurs in uninstrumented code, the formal endpoint is the recorded call
site rather than the hidden operation. The method does not reconstruct a
missing world root, prove that an inferred predecessor state existed, edit a
program, execute a repair, or verify post-repair continuation.

The RQ4 “debugging agent” is Tregression's automatic regression localizer. It
aligns failing and working executions and follows data/control dependencies
from an observed faulty step toward a known root-cause step. Success means
generating a path to that benchmark root cause. It is not a human study, an
LLM coding-agent repair, or a total-maintenance-work measure.

## Evaluation and result

RQ1 uses 905 translated ND-Slicer items, 100 LLM-Slicer programs, and 7,365
author-generated hierarchical programs. These sum to **8,370**, while the
abstract and prose repeatedly report **8,300** dependencies. The 70-item
discrepancy is unresolved. Reported RecovSlicing precision/recall is
80.34/80.34% on the hierarchical set, 91.06/91.06% on translated ND-Slicer,
and 98.25/98.25% on LLM-Slicer. GPT-4o accuracy on the five hierarchical
levels falls from 93.89% for basic operations to 68.50% with aliasing and is
73.05/73.46% for interprocedural/inter-file cases.

RQ2 uses 570 variable-recovery and 1,032 definition-inference tasks. Reported
totals are 91.48% precision and 89.24% recall for variable recovery and
**83.24% success for definition inference**. These results supply a material
false-edge and missed-edge boundary for treating estimates as evidence.

RQ4 selects **489 of 835** Defects4J bugs because Tregression cannot collect
long traces for the remainder. Runs use at most 100,000 trace steps,
one-layer variable recording, and a 60-minute whole-session limit; timeouts
count as failures. Across 16 active projects, reported localization success
rises from **0.73 to 0.89**. The paper does not report per-project
denominators, confidence intervals or tests, repeated LLM runs/seeds, an exact
model snapshot, token/API cost, or complete acquisition/integration work.

This is primary empirical evidence that estimated missing dependencies can
improve one automatic regression-localization pipeline under the reported
bounds. It does not show that inferred history equals retained state or that
an executor can deliver and validate a repair.

## Consequence for R03/R06

S311 supports a separately named **rescue or estimator treatment** when a
practical history route omitted a needed dependency. Actual predecessor roots,
values, and operations remain observed history; RecovSlicing-style edges are
model estimates. Reaching a cause, proposing a change, applying it, and
passing a behavioral continuation remain distinct endpoints. Instrumentation,
synthesis, LLM calls, timeouts, integration, and verification belong in total
work.

This does not repair the retained R03 episode's missing original entity names
or missing predecessor root. Using an estimate there would change the
information condition and provide an unverified cause. A future authored case
could prespecify the estimator as a fallback or separate arm.

For R06, the paper shows why retention scope is a separate design variable:
a partial trace can be feasible while missing edges are inferred incorrectly
and require verification. It reports neither Nu's history costs nor a matched
acquisition/recovery comparison, so it does not change the retained R06 timing
result.

## Access boundary

Reference [4] points to `https://sites.google.com/view/recov-slicing/home` for
source, demo, tutorials, examples, and experimental details. On 23 October
2026, an ordinary public fetch redirected to Google sign-in. No account was
created and no gated content was used. The source package, benchmark rows,
exact model invocations, and result reproduction remain uninspected.
