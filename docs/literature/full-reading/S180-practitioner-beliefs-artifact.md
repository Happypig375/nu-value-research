# S180 replication-artifact audit

Status: accepted bounded static availability/correspondence audit, 2026-10-26,
with a later [independent correlation reconstruction](S180-correlation-reconstruction.md).
The complete published analysis has not been reproduced end to end.

Date inspected: 2026-10-25

## Scope and non-execution boundary

The original static phase checked whether the data and analysis materials named
by S180 were publicly available and whether their contents clarified the method.
It did not execute supplied Python, batch files, bytecode or notebooks. Its
computations were archive hashing/inventory and descriptive row/key/column
checks. Two later setup attempts failed before data access. The separately
recorded C: continuation then completed the unchanged independent correlation
check, still without executing supplied analysis code. Its scope and results
are distinct from the original static audit and the unknown publication run.

## Official record and retained archive

The paper's footnote identifies `10.5281/zenodo.4553435`. Direct browser opens of the DOI resolver and Zenodo HTML record both failed in this environment and yielded no evidence. A direct read of the official Zenodo API record succeeded with HTTP 200 on 2026-10-25. That record reports:

- title: *Assessing Practitioner Beliefs about Software Engineering*;
- resource type: software, version `v1.0.0`, publication date 2021-02-20, CC0;
- a supplement relation to `https://github.com/snaraya7/SE_Beliefs/tree/v1.0.0`;
- one file, `snaraya7/SE_Beliefs-v1.0.0.zip`, 5,006,908 bytes, with recorded MD5 `dbd6897197b955ff6a7ea784ab4295de`.

The archive was downloaded through the Zenodo API into this private reading directory. Its observed MD5 matches the official record. Its SHA-256 is `ffd1d09150dd3eede84bcb1dd5f4b3e7dc1656d7f38369b72f33deace23fdfb1`.

The archive has 58 entries. It contains a README, Python and Windows batch analysis scripts, Scott-Knott implementation, precomputed result files, and three CSV files. No supplied program was run.

## Data availability and denominator check

Static CSV inspection establishes that `data/filtered_data.csv` contains 13,560 rows and 115 columns, with:

- 1,356 distinct `PSPStuDataID` values;
- exactly ten rows per developer;
- exactly one row per developer-task pair and 1,356 rows for each of tasks 1A through 10A;
- no missing value in the identifier, task, language, years-experience, actual LOC, coding-minutes, code-defect, design-defect, or test-removal fields used in the reported analyses;
- 509 C, 327 C++, 201 C#, 163 Java, and 156 VB developers;
- 891 developers below three years of experience and 465 at or above three years.

The archive therefore resolves the article's ambiguous introduction sentence about "5,424 completed tasks": 5,424 is the count for the four level-2 tasks only (1,356 x 4), whereas the selected five-language analysis file has 13,560 task records (1,356 x 10). It does not resolve why Table 2's domain counts total 1,787 while the surrounding text describes a broader 3,832-person training corpus and the analytic subset contains 1,356 developers; there is no domain column in the inspected analysis CSVs.

The other two CSVs each contain 16,190 rows. The audit did not reconstruct their filtering lineage beyond file inventory because the selected-file denominator was already directly checkable.

## Static method correspondence

### Scott-Knott effect-size discrepancy

The paper says the Scott-Knott split test combines bootstrapping with Vargha-Delaney A12 (p. 14). The archived executable path does not implement that description as invoked:

- `sk.py` defaults to 1,000 bootstrap samples, `conf=0.01`, A12 threshold 0.56, and Cliff's-delta small threshold 0.147 (lines 31-32, 51-62).
- `different()` uses A12 only if `The.useA12` is truthy; otherwise it uses Cliff's delta, and both branches then use the bootstrap test (lines 969-975).
- Every archived `.bat` command invokes `sk.py` without `--useA12`.
- `rdivDemo()` passes `useA12=True` into `scottknott()` (line 1115), but that flag only selects the `different()` route; inside `different()`, the unpassed `The.useA12` remains false, so the actual effect-size screen is Cliff's delta.

If the retained batch commands were executed against the retained `sk.py`, that archived path would use bootstrap plus Cliff's delta rather than bootstrap plus A12. Static inspection does not establish that this invocation produced the publication tables, nor does it bind any unarchived run to them. Correspondence between the retained invocation and the paper-level ranks therefore remains unknown.

### Correlation censoring

`Constants.py` sets `SIG_LEVEL = 0.01`. In both `belief3.py` and `belief4.py`, `deduceCorrelation()` returns the Spearman coefficient only when its p-value is below 0.01; otherwise it substitutes numeric zero. The retained scripts include those substituted zeros in the per-language arrays from which they calculate medians and boxplots. On that archived path, a plotted zero could mean either an observed coefficient near zero or a coefficient of any magnitude that failed the p-value screen. The article does not describe this censoring operation. Static inspection does not establish that the retained scripts produced Figures 6 and 7, so correspondence to the published boxplots remains unknown.

If the retained path produced the published figure, this would matter most for belief 4: a distribution centered on zero would not be a direct distribution of all observed correlations or an equivalence test, because it would partly contain values forced to zero after significance testing.

### Production-rate denominator discrepancy

The paper defines production rate as LOC per hour of coding time (p. 12). The retained scripts use a different denominator:

- `PSPConstants.py` maps `ACTMIN_COLNAME` to `ActMin` and separately maps `ACTMINCODE_COLNAME` to `ActMinCode` (lines 37 and 47).
- `belief1.py` computes production rate as `ActLOC / (ActMin / 60)` at lines 18 and 57.
- `belief4.py` uses the same `ActMin` expression at line 71.
- `belief5.py` uses the same `ActMin` expression for its production samples and global normalization bounds at lines 50, 66-67, and 115-116.

The two columns are not interchangeable in the retained 13,560-row `filtered_data.csv`. `ActMin` is nonzero on every row; `ActMinCode` is zero on four. They are exactly equal on no row. `ActMin` exceeds `ActMinCode` on 13,559 rows, while one row has `ActMinCode` 26 minutes above `ActMin`. Their medians are 196 and 58 minutes respectively, with median difference 131 minutes. Summed coding minutes are about 30.0% of summed `ActMin`; the per-row coding/total ratio has median about 0.302 and IQR about 0.211-0.415. In 12,881 rows, `ActMin` exactly equals the sum of the eight retained PSP phase-minute columns (plan, design, design review, code, code review, compile, test, and postmortem), consistent with its broader total-like role; the remaining 679 rows have nonzero reconciliation differences.

Therefore, if the retained scripts were the publication-producing path, beliefs 1, 4, and 5 would use LOC per broader `ActMin` hour rather than the paper's declared coding-time denominator. Static inspection cannot establish that the archived scripts generated the published tables or figures, so the publication's actual denominator remains unresolved rather than silently reassigned.

### Other reporting correspondences and limits

- The paper's p. 11 filtering section says beliefs 1 and 4 use only level-2 tasks, but pp. 20-21, Figure 7, and `belief4.py` use all ten tasks for belief 4.
- The p. 12 overview assigns Scott-Knott to belief 4, while the belief-4 experiment actually uses Spearman correlation.
- The README says Python 3 generates intermediate files and Python 2 runs the batch/Scott-Knott stage. Its belief-5 instructions link to `belief1.bat` even though a `belief5.bat` is present.
- `data/pspdata.py` reads `filtered_data.csv` through an author-specific absolute Windows path (`C:/Users/ncshr/PycharmProjects/SE_Beliefs/...`), so the archived workflow cannot run from an arbitrary checkout without modification. That file identity does, however, confirm that the 13,560-row `filtered_data.csv` is the selected analysis input.
- The archived files make the data and code inspectable, but no environment lockfile, package-version manifest, random seed, or automated end-to-end command is supplied. The audit did not test whether the software still executes or reproduces the tables.

## Belief-source access check

S180 says the five propositions were selected from Albert Endres and H. Dieter Rombach's 2003 *A Handbook of Software and Systems Engineering: Empirical Observations, Laws, and Theories*, then limited to propositions compatible with the available PSP data and favored for citation prominence (pp. 2-3). One bounded exact-title query on 2026-10-25 returned 11 visible results representing nine unique durable URLs. The result inventory is recorded below. Opening the Fraunhofer publication record was denied by its access-control page; no other result page or book body was opened. This audit therefore does not independently verify the handbook's wording, qualifications, or characterization of the five propositions. Third-party full-text results were discarded without opening or use.

The original works cited for the five propositions were identified from S180's references but not newly read: Corbato [11], Dahl/Nygaard and Goldberg/Robson [12, 23], Cobb/Mills and Mills [10, 36], Sackman et al. [52], and Norman [43]. S180 itself is the only source for the exact formulations assessed here.

## New external-source audit

Only the following new external routes were considered during this assignment:

1. DOI resolver for `10.5281/zenodo.4553435`: direct browser open failed; no evidential use.
2. Zenodo HTML record `https://zenodo.org/records/4553435`: direct browser open failed; no evidential use.
3. Official Zenodo API record `https://zenodo.org/api/records/4553435`: HTTP 200; used for artifact identity, version, license, supplement relation, file size, and MD5.
4. The single archive linked by that API record: downloaded, hash-verified, inventoried, and statically inspected; supplied code was not executed.
5. One exact-title query, `Albert Endres Dieter Rombach A Handbook of Software and Systems Engineering Empirical Observations Laws and Theories 2003 Springer`, returned 11 visible results. No repeated search was made. The results and dispositions were:
   - `https://publica.fraunhofer.de/entities/publication/8824cfde-645c-48b6-873c-bf97d85f62f8` — Fraunhofer bibliographic result; identity metadata considered; body open attempted and denied.
   - `https://search.worldcat.org/title/50417309` — WorldCat bibliographic result; snippet considered; page not opened.
   - `https://ndl.ethernet.edu.et/bitstream/123456789/34262/1/39.pdf.pdf` — third-party full-text result; discarded without opening.
   - `https://s3-euw1-ap-pe-df-pch-content-store-p.s3.eu-west-1.amazonaws.com/9780429093791/60e2c84a-2b92-4094-af4f-c2c7b971a5fd/web.pdf` — the same third-party object appeared as three separate results with distinct temporary signed query strings; all three were discarded without opening. The stable object URL is recorded exactly; transient AWS credential-bearing query strings are intentionally not reproduced.
   - `https://www.iese.fraunhofer.de/en/media/books.html` — Fraunhofer IESE English books result; snippet considered for identity; page not opened.
   - `https://www.iese.fraunhofer.de/de/media/buecher.html` — Fraunhofer IESE German books result; snippet considered for identity; page not opened.
   - `https://obnb.uk/a00643189-albert-endres` — Open British National Bibliography author result; snippet considered for identity; page not opened.
   - `https://dblp.org/pid/r/HDRombach.html` — DBLP author result; snippet considered for identity; page not opened.
   - `https://obnb.uk/a00643190-h-dieter-rombach` — Open British National Bibliography author result; snippet considered for identity; page not opened.

No arXiv or journal metadata screen was repeated. No publisher version-of-record bytes were obtained, so correspondence between the selected arXiv v4 body and the journal version remains unresolved. The separate parent lookup used the exact journal DOI with limit 20, offset 0 and returned one record. It verified bibliographic identity only; no editorialNotices field was returned, so absence of a correction is not established.


## Parent arithmetic check: original return before data access

The prospective private plan specified 150 task-language cells: belief 3,
belief 4 using the archived broader-time metric, and a coding-time sensitivity.
It retained raw coefficients and the significance-to-zero rule separately,
with uncomputable cells preserved rather than silently dropping rows. This
plan was not a completed analysis at the original return. Both attempts failed during dependency
import before the CSV was read: initially missing SciPy, subsequently damaged
installed source. No correlations, p-values, sensitivity result or plot
correspondence were produced by those attempts. Do not infer anything from their absence.

The planned method referred to
[SciPy 1.14.1's spearmanr documentation](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats.spearmanr.html).
Its asymptotic p-value qualification matters for the mostly smaller groups;
a prospective arithmetic reconstruction would not itself validate inference
or recover the historical software versions. No new environment was substituted
at that integrity return. See the
[storage handoff](../../workspace-integrity-return-2026-10-26.md).

The paper, official archive, corrected notes and coverage records were copied
without changing their bytes to C: and matched their earlier recorded hashes.
Revision-01 drafts and the declared check remain private. No copyrighted body,
CSV or extraction dump is committed.

## Subsequent C: calculation

The [2026-10-26 independent reconstruction](S180-correlation-reconstruction.md)
now supplies 150 declared cell dispositions: 146 correlations and four
uncomputable coding-time cells, without dropping their invalid rows. Under the
declared `ActMin` metric, the archived significance-to-zero rule replaces 35 of
50 coefficients and makes four language medians exactly zero. B3 has no replaced
coefficients. The new environment and script are identified separately from
the publication's unknown software invocation; no full Scott-Knott or author
workflow reproduction follows. Earlier failures, source discrepancies, journal
edition gaps and the A: stop remain unchanged.

## References

Shrikanth, N. C., Nichols, W., Fahid, F. M., & Menzies, T. (2021).
*Assessing practitioner beliefs about software engineering*.
[arXiv:2006.05060v4](https://arxiv.org/abs/2006.05060v4).

*Assessing practitioner beliefs about software engineering* (Version v1.0.0)
[Software and data]. (2021).
[Zenodo record API](https://zenodo.org/api/records/4553435).

SciPy developers. (n.d.). *scipy.stats.spearmanr* (SciPy 1.14.1 documentation).
[Method documentation](https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats.spearmanr.html).
