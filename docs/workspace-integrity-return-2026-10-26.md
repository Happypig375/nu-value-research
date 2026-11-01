# Workspace integrity return and literature preservation, 2026-10-26

A: writes and calculations stopped after a new installed-source integrity
failure during S180's independent arithmetic preparation. Windows subsequently
reported A: **Warning / Full Repair Needed**, with 721,323,339,776 free bytes.
C: reported **Healthy / OK**, with 20,030,230,528 free bytes. These are observed
volume states; no hardware cause is established. At the original return, no
repair, dismount, reset, package reinstall or native experiment followed the failure.

## Observed failure

The declared S180 calculation had two failed setup invocations and no result.
The first failed to import absent SciPy. An isolated installation of SciPy
1.14.1 and NumPy 2.2.6 under the private S180 directory reported success. The
second invocation failed during import with a null-byte syntax error, before
opening the study archive or CSV.

For `numerics/scipy/special/__init__.py`, size 34,183 bytes, the package RECORD
expects `sha256=FKi05OxjItayyrlMUYgPlzMFAcJQzc2bMa9luxLC0C0`.
The observed file has 621 null bytes and SHA-256
`d7b5450cfc1e2ad17b7ee6753a5970cc6851b9d96c7c1f25f62226b05f3d35b9`,
unchanged on a repeated read and different from that RECORD. A bounded scan of
the installed package also encountered other null-containing Python sources
and file-read errors. It is not a whole-volume integrity assessment.
Those attempts produced no calculation result; do not count either as a completed
reproduction or silently replace the failed setup.

## Verified preservation and current documentation location

A new private destination was created:

`C:/Users/hadri/nu-value-recovery/20261025-s180-integrity-stop-01`

It preserves 89 files, 15,575,735 bytes: the unfinished literature notes and
revision history, PDF/archive, text/renders/coverage, declared calculation,
existing handoff/authority documents and two uncommitted documentation edits.
Every destination matches two source reads; all seven available earlier
expected hashes match, including the selected PDF, official archive, corrected
notes and acquisition record. Copied text passed strict UTF-8 and null checks.
There were zero failed copies. This is a bounded preservation result, not a
claim that all A: content is intact. The damaged installed dependency was not
copied or executed from C:.

`preservation-manifest.json` and
`parent-acceptance-and-integrity-return.json` retain the exact paths, hashes,
checks and failures. Private source material remains outside Git. The two
restricted branch packets and native experiment inputs remain at their earlier
A: paths and were not reviewed or copied in this operation.

Documentation integration uses a fresh, sparse clone from the GitHub remote at
`346133b942c627d5ca9eb25d956f69b7ca109e0b`, independently of A:'s Git objects:

`C:/Users/hadri/nu-value-recovery/20261025-s180-integrity-stop-01/publication-review`

Only the two verified documentation drafts were reapplied, followed by the
new literature and handoff documentation. The original A: publication tree,
original A: workspace and earlier C: recovery remain untouched. Do not pull,
reset, clean or resume writes/execution on A: under an ordinary continuation.
Later use needs a recorded healthy-storage decision and verification of the
exact inputs; a healthy label alone does not prove file correspondence.

## Research disposition

[S180](literature/full-reading/S180-practitioner-beliefs.md) has complete
selected-edition text/visual reading and an accepted bounded
[static artifact audit](literature/full-reading/S180-practitioner-beliefs-artifact.md).
At the original integrity return, its independent arithmetic check was
**unfinished, with no result**. The separate C: continuation below supersedes
that calculation status only.
[R04](nu-research-study-designs-2026-10-08.md) and
[R14](nu-practice-and-task-provenance-2026-10-11.md) receive documentation-only
method/provenance reconciliation. No new Nu capability or comparative benefit
is inferred from this work.

Both [Daybreak-only branches](unfinished-daybreak-only-work-2026-10-25.md)
remain unfinished and inaccessible to non-Daybreak models, including through
delegation. No verified Daybreak identity is recorded. R03 native-001 remains
terminal; the R02/R10/R12 returns and candidate/participant/paid/H allocation
limits are unchanged. All subagents have completed. The broad research goal
was observed active at this continuation; neither the storage return nor this
handoff declares the research complete.

## Subsequent bounded C: arithmetic continuation

On 2026-10-26 HKT, C: reported Healthy/OK with 23,255,916,544 free bytes. A
separate calculation directory was created at
`C:/Users/hadri/nu-value-calculations/20261026-s180-correlation-01`.
The previously declared plan, independent script and official archive were
copied from the verified C: preservation, matching two source reads and every
destination hash. No A: source, installed dependency or native input was used.
The earlier 89-file preservation was not changed.

After official wheel/member and installed-record verification, a preflight and
one unchanged analysis invocation completed. The
[calculation record](literature/full-reading/S180-correlation-reconstruction.md)
retains 146 correlations and four uncomputable cells, both prior pre-data
failures, and a corrected generated-launcher path-verification failure. This is
a new identified calculation environment, not silent replacement of the failed
installation or certification of all C: data. The source copy and numerical
environment checks do not reopen A:, a Nu runtime, any returned gate, candidate
allocation or either Daybreak-only branch. The documentation checkout remains
for documentation/source synthesis.
