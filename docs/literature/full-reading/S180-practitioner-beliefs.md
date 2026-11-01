# S180 full reading: Assessing Practitioner Beliefs about Software Engineering

Status: selected-edition full reading accepted for literature integration on
2026-10-26. A later bounded independent correlation reconstruction is recorded;
the authors' complete published analysis remains unreproduced.

## Identity and edition boundary

- N. C. Shrikanth, William Nichols, Fahmid Morshed Fahid, and Tim Menzies, *Assessing Practitioner Beliefs about Software Engineering*.
- Selected body: arXiv:2006.05060v4, 24 May 2021, 32 pages; the manuscript says accepted 26 February 2021 and identifies DOI `10.1007/s10664-021-09957-5` (p. 1).
- Read file: `S180-2006.05060v4.pdf`, 2,558,111 bytes, SHA-256 `8eb1eaeca6b0a9d291920c68ded6a17b889c3e65a638494f8c03b1fe4361bc4b`.
- Zotero was verified before reading and was not changed: journal parent `Z5ADDDFA` version 4247 in `PKLXQNEE`; related preprint-PDF attachment `VLAA2F7Q` version 4237.
- The journal parent and selected preprint are distinct editions. No publisher bytes were obtained, so version-of-record body correspondence is unresolved.

## Full-coverage statement

All 32 pages were read as extracted text, and the same AI maintainer reader inspected every page from 144-dpi full-page renders at 1191 x 1684 pixels. This was a second modality used by the same reader, not an independent or human review. The pass covered title/abstract, main text, methods and equations, all six tables, all nine figures, threats, acknowledgements, all 67 references, and author biographies. The paper has no appendix; none is silently inferred. Exact artifacts and limitations are recorded in the private `coverage.json`. The parent reviewed the complete proposed reconstruction and decision-critical source, directly inspected rendered pages 2, 3, 8, 12, 14, 15, 19 and 20, and required the corrections recorded below. This is AI maintainer review, not human approval or a second full reading.

## Interpretation

S180 is most useful as a warning about construct separation, not as evidence that a particular technology or language causes better outcomes. The five "practitioner beliefs" were not elicited from the 1,356 participating developers, nor was their prevalence measured. The authors selected propositions from a 2003 handbook, restricted the set to propositions that their already-available PSP data could address, and preferred five that they described as widely cited (pp. 2-3, Table 1). They then retrospectively related those propositions to 1995-2006 training-task records.

The data can show bounded descriptive associations and rank contrasts that the authors interpret as adverse evidence against several broad formulations. It cannot establish exact size matching, a universal counterexample, that the trainees held the beliefs, that a belief caused their behavior, that a language caused the observed outcomes, or that the proposed managerial prescriptions improve projects. Static inspection of the official replication archive exposes two consequential conditional discrepancies: the retained correlation scripts would convert nonsignificant coefficients to zero before summary, and the retained Scott-Knott invocation would use Cliff's delta plus bootstrap rather than the paper's stated A12 plus bootstrap. If those paths produced the published outputs, belief 4 and the reported rank method would require further qualification. Actual publication-run correspondence is unknown. See the [artifact audit](S180-practitioner-beliefs-artifact.md).

For R14, the defensible transfer is procedural: keep a reported preference or requirement, an explicit empirical prediction, and observed history/outcome as three separate objects. For R15, the study shows why retrospective fit is not prospective guidance. It provides no evidence of Nu benefit.

## What the five beliefs actually are

Table 1 (p. 3) gives the following inherited propositions and source labels:

1. **Corbato's law (1969):** productivity and reliability depend on program-text length rather than language level.
2. **Dahl-Goldberg hypothesis (1967/1989):** object-oriented programming reduces errors and encourages reuse.
3. **Mills-Jones hypothesis (1983/1990):** software quality entails productivity.
4. **Sackman's second law (1968 in Table 1; the body calls the cited study 1966):** individual developer performance varies considerably.
5. **Apprentice's law (1993):** about 5,000 hours turns a novice into an expert.

These are literature-selected propositions. S180 says it began with Endres and Rombach's handbook, excluded beliefs that required other data, and selected five among the remainder partly for citation prominence (pp. 2-3). The exact handbook passages and original-source qualifications were not accessible in this audit. The paper's labels should therefore not be upgraded into a finding that contemporary practitioners endorse exactly these formulations.

## Population, hierarchy, tasks, and exclusions

### Population and course

The underlying PSP training corpus was collected from 1995 through 2006. The paper describes 3,832 trainees across 373 classes, with 361 classes in industry and 123 university participants (3.2%). Classes were delivered in the United States, Japan, Korea, Australia, Mexico, Sweden, Germany, the United Kingdom, the Netherlands, and India. Class size ranged from 1 to 20, with mean 10.4 and interquartile range 7-14 (p. 7).

The analytic subset contains 1,356 developers who used C, C++, C#, Java, or Visual Basic, described as 85% of developers in the relevant language distribution (pp. 8, 11; Figures 2 and 5). Fifteen languages used by fewer than 30 developers were excluded. Every selected developer used one self-chosen, familiar language and completed ten assignments in that language. Exact selected counts, confirmed by Figure 8 and the archived filtered file, are:

| Language | Novice developers | Expert developers | Total developers | Task records |
|---|---:|---:|---:|---:|
| C | 335 | 174 | 509 | 5,090 |
| C++ | 185 | 142 | 327 | 3,270 |
| C# | 140 | 61 | 201 | 2,010 |
| Java | 123 | 40 | 163 | 1,630 |
| VB | 108 | 48 | 156 | 1,560 |
| **Total** | **891** | **465** | **1,356** | **13,560** |

The ten-day PSP course had a measurement/estimation week and a review/design/quality week, normally separated by at least two weeks (p. 7). Participants used their own devices, language, and development environment. The course instructed them to use the language with which they were most comfortable (p. 10). Static analysis was prohibited until compilation, and real-time IDE syntax checking was supposed to be disabled, but actual environments and adherence were not recorded (p. 10).

### Tasks and observational units

The ten assignments were the same for every selected developer and increased across PSP levels 0, 1, and 2. They were small, generally 100-200 LOC, principally numeric/statistical programs involving size counting, linear and multiple regression, numerical integration, chi-square and Student-t calculations, and prediction intervals (pp. 7-10; Table 3). Requirements supplied formulas, algorithms, test cases, and examples. Participants could use primitive mathematical functions but not library procedures (p. 10).

Developers often implemented each assignment in three to five increments, but the analytic row is the completed developer-task. Time and defects were recorded by PSP phase. A defect was any change after a phase was declared complete, with type, injection phase, discovery phase, and repair time recorded (pp. 9-11). Figure 4 (p. 9) reports 124,521 defects in the described task corpus: 16,437 injected in design, 75,927 injected in coding, and 32,157 removed in test.

The hierarchy is therefore not 13,560 independent developers. It is ten repeated task records nested within each of 1,356 developers, developers nested within classes, and classes distributed across time, countries, organizations, and product domains. Task order also coincides with PSP instruction and increasing difficulty. S180 does not model developer, class, task, cohort, country, organization, or period as random/fixed effects.

There is a denominator inconsistency in the article. The introduction says it has 5,424 completed tasks (p. 2), while Table 3 shows 1,356 attempts for each of ten tasks, or 13,560 developer-task records (p. 8). Figure 5 identifies 5,424 specifically as the four level-2 tasks, resolving the likely intended scope (p. 11). The official filtered CSV confirms 13,560 selected rows, exactly ten per developer and 1,356 per task. Separately, Table 2's product-domain cells sum to 1,787 rather than either 3,832 or 1,356; the paper does not map that table to the analytic subset.

### Filtering and missingness

Belief 1 uses level-2 tasks 7-10 before narrowing to task 10. Beliefs 2, 3, and 5 use all ten tasks (p. 11). The filtering section says belief 4 also uses only level-2 tasks, but the belief-4 result, Figure 7, and archived script use all ten (pp. 20-21). The selected archive file has no missing value in the key identifiers and measures used here. The paper gives no attrition analysis and does not explain the transition from the 3,832-person broad corpus to the five-language subset beyond language prevalence.

## Outcomes and operationalizations

S180 defines program size as LOC, production rate as LOC per hour of coding time, and quality as a defect count (p. 12). Unless a section says otherwise, "defects" means defects injected during coding. Some analyses add design-injected defects or use defects removed in testing.

The retained code does not implement that declared production-rate denominator for beliefs 1, 4, or 5. `PSPConstants.py` distinguishes `ActMin` from `ActMinCode`, but `belief1.py`, `belief4.py`, and `belief5.py` all compute `ActLOC / (ActMin / 60)`. In the retained 13,560-row file, the columns are equal on no row; their medians are 196 total-like minutes and 58 coding minutes, and coding minutes sum to about 30.0% of `ActMin`. `ActMin` exactly equals the sum of eight PSP phase-minute columns on 12,881 rows, reinforcing that it is broader than coding time. The archived static path therefore would use a broader effort denominator. It is not bound to the actual publication-table or figure run, so the production denominator underlying the published results remains unresolved. Results below are paper-reported observations, not claims that the retained scripts necessarily produced them.

These choices impose important limits:

- Under the paper's stated definition, production rate excludes planning, design, review, compile, test, repair, and other recorded effort and is not total delivery productivity. Under the retained scripts, the broader `ActMin` denominator is used instead; neither measure is a complete end-to-end project-value measure.
- Raw defect count is defended because all participants did the same tasks, but it is still not escaped field defects, user value, reliability, or production quality.
- Belief 3's "early quality" exposure is not an intervention or review effort. It is the number of defects injected in design and code; its outcome is the number removed in test.
- Belief 5 operationalizes expert as at least three years or approximately 5,000 programming hours and novice as below three years. The data analysis uses the years threshold. This is not a direct measure of deliberate practice, task expertise, language-specific experience, or demonstrated expertise.
- Tables 4-6 display min-max-normalized values on a 0-100 presentation scale rather than raw LOC/hour or defect counts. Their medians and IQRs therefore support ordering within the fitted comparison, not an original-unit magnitude.

## Inferential methods and dependence

### Scott-Knott comparisons

For beliefs 1, 2, and 5, the paper min-max normalizes the pooled treatment values, orders treatments by median, recursively selects the split maximizing expected between-group mean difference, and accepts splits with a bootstrap plus claimed Vargha-Delaney A12 effect-size screen (pp. 12-14). The article does not state bootstrap repetitions, the A12 cutoff, or a familywise/FDR adjustment. The official code archive supplies defaults of 1,000 bootstrap samples and 0.01 confidence threshold. If the retained batch commands were executed as archived, their path would use a Cliff's-delta threshold of 0.147 rather than A12. The audit does not establish that this path produced the publication tables, so correspondence remains unknown.

Pooling ten task rows per developer for beliefs 2 and 5 treats dependent records as treatment observations without a developer cluster term. It also conflates task difficulty/order with the repeated training sequence. Scott-Knott reduces pairwise comparisons by recursive clustering, but the paper does not adjust across the five beliefs, multiple outcome constructions, task/language searches, or the later subset analyses.

### Correlations

Beliefs 3 and 4 compute a Spearman correlation separately in each task-language group, yielding 10 tasks x 5 languages = 50 coefficients per belief (pp. 18-20). Each coefficient uses one record per developer in that language: n=509 for C, 327 C++, 201 C#, 163 Java, or 156 VB. The same developers recur across the ten task-specific coefficients for their language, so the ten values summarized in each language boxplot are dependent.

The authors classify absolute rho of 0-.39 as no support, .40-.49 weak, .50-.59 support, .60-.69 strong, and .70-1.00 very strong; they acknowledge these thresholds are debatable (p. 13). They use p<.01 per coefficient but state no multiplicity adjustment, confidence intervals, or power/equivalence criterion.

Static artifact inspection adds a consequential conditional fact omitted by the article: each retained correlation script replaces any coefficient with p>=.01 by numeric zero before calculating per-language medians and plotting. On that archived path, zero is a censored value rather than necessarily an observed rho of zero, which would make the belief-4 null interpretation especially fragile. The audit does not establish that this path produced Figures 6 and 7.

### No confounder adjustment or causal identification

The authors considered structural equation modeling but abandoned it because productivity is derived, person effects are nonnormal, and interactions/confounders were difficult; they explicitly say student and other confounders are not accounted for (p. 12). The final analyses do not adjust for self-selection into language, years using that language, tool/IDE, organization, class, instructor, country, cohort/year, task order, or PSP learning. Calling language a "confounding factor" in the discussion does not turn the language comparisons into causal effects.

## Belief-by-belief evidence

### 1. Corbato: authors' adverse interpretation from a selected observational contrast

The authors search the four level-2 tasks for C and C# LOC distributions that share a Scott-Knott rank, find task 10, and then compare task-10 production and defects (pp. 14-16; Table 4). Denominators are 509 C developers and 201 C# developers, one task record each.

Table 4's normalized displays are: program size C# median/IQR 18/11 and C 17/10, both rank 1; production C# 13/10 rank 1 versus C 8/7 rank 2; defects C# 5/7 rank 1 versus C 9/9 rank 2 (p. 15). The authors treat the shared size rank followed by different outcome ranks as adverse evidence against the broad law. A shared Scott-Knott rank is neither an equivalence result nor exact length matching: the displayed size medians are 18 and 17, and the underlying distributions can still differ. Because language, developer groups, and residual size are not jointly controlled, this selected contrast does not itself prove a universal counterexample.

It is not evidence that switching from C to C# causes higher productivity or fewer defects. Language was self-selected, only one language pair and one post-screened task carry the outcome claim, and C# and C groups can differ in unmeasured experience, cohort, tooling, and class. The paper's own later explanation invokes C# libraries even though library procedures were prohibited in the tasks (pp. 10, 25-26).

### 2. Dahl-Goldberg: mixed/conditional, adverse to the simple OO category

Belief 2 pools all ten repeated task rows by language and compares design-plus-code defect counts (pp. 16-18; Table 5). Effective record counts are 5,090 C, 3,270 C++, 2,010 C#, 1,630 Java, and 1,560 VB, arising from 509, 327, 201, 163, and 156 developers respectively.

Across all tasks, normalized median/IQR and ranks are VB 5/5 rank 1, C# 5/5 rank 1, C 8/7 rank 2, Java 8/8 rank 2, and C++ 11/10 rank 3. Task 10 alone has C# 5/5 and VB 6/6 in rank 1, Java 8/11 and C 8/8 in rank 2, and C++ 11/13 in rank 3 (p. 18).

The result is positive for a conditional language difference but adverse to a simple OO-versus-non-OO rule: two languages classed as OO rank better than C, while Java does not and C++ ranks worse. It does not test reuse, and it does not identify OO design as the cause because the actual program designs and language/tool experience are uncontrolled.

### 3. Mills-Jones: positive association, causal interpretation unsupported

For each task-language group, belief 3 correlates design-plus-code defects injected with defects removed in test, producing 50 coefficients (pp. 18-19; Figure 6). The group sample sizes are the language-specific developer counts above. The prose reports median rho about +.5 for Java, above +.6 for each other language, and an overall median about +.6 (p. 19). Visual inspection of Figure 6 does not fully agree: its C++ median line is below .6, although the figure still shows a favorable positive association. No exact replacement value is inferred from the plot. By its chosen thresholds, this is the only belief the authors call supported.

The observation is a positive retrospective association between two defect counts from the same completed program. It does not observe early quality assurance effort or randomize an early-quality treatment. Programs with more total defect opportunities can have both more injected defects and more test removals, and test removals are not themselves coding time or on-time delivery. The conclusion that early quality assurance minimizes rework is therefore a causal/process interpretation that the measures do not identify. If the archived correlation path produced Figure 6, its p-value censoring would also mean the plotted coefficient distribution is not a complete distribution of observed rhos.

### 4. Sackman: null association for a rewritten question, not a test of the law

Belief 4 correlates coding-defect counts with production rate in the same 50 task-language groups (pp. 19-21; Figure 7). Figure 7 is centered at zero across languages, and the authors infer that quality is not affected by variation in developer production rate.

This is not a direct test of whether individual performance varies considerably. It asks whether two performance dimensions covary monotonically within task-language groups. Large between-person variation can exist even when speed and defects are uncorrelated. In the retained script, nonsignificant correlations would be replaced by zero; if that path produced Figure 7, a median containing censored zeros would be neither evidence of exact zero association nor an equivalence result. Even without binding the script to the figure, the paper supplies no equivalence analysis. The strongest defensible paper-level result is that this analysis did not establish a monotonic speed-defect association under its p<.01 screen.

### 5. Apprentice: aggregate null with conditional language patterns

Belief 5 compares 891 novice developers (8,910 task rows) with 465 experts (4,650 task rows), using all ten repeated tasks per person (pp. 21-23; Figure 8; Table 6). In the pooled comparison, production is expert median/IQR 6/4 and novice 5/5, both rank 1; defects are expert 6/6 and novice 5/6, both rank 1. These are null rank separations, not demonstrated equivalence.

Language-stratified production ranks are conditional: C# novice and expert are rank 1; C++ expert, Java expert, and VB novice rank 2; Java novice, C++ novice, C expert, VB expert, and C novice rank 3. The paper summarizes an expert production advantage only for Java and C++ (two of five languages). For defects, C# novice and VB novice rank 1; C# expert, C novice, and VB expert rank 2; Java expert, C expert, C++ novice, Java novice, and C++ expert rank 3 (p. 23).

These results are adverse to a universal claim that three-plus years guarantees better speed and quality in these assignments. They do not show that industrial experience has little value or that novices are generally experts. The experience split is coarse, language-specific experience is unknown, tasks are constrained and unfamiliar, language is self-selected, ten rows per person are pooled, and absence of rank separation is not an equivalence test.

## Aggregate interpretation and threats

Figure 9 (p. 24) redraws the five propositions into a causal-looking aggregate diagram, retaining belief 3 and adding language-to-defect/productivity links while marking the others unsupported. The paper calls this similar to meta-analysis, but it is not a formal meta-analysis: the five analyses reuse one data source, developers, tasks, and measures, and their results are not independent effect estimates.

The authors argue that narrow observations can make beliefs diverge and recommend regularly retesting inherited claims (pp. 23-28). That general recommendation is reasonable. Their stronger prescriptions are not established by the design: emphasizing quality early, discounting experience, and emphasizing language are causal or decision claims drawn from retrospective associations.

The paper acknowledges several threats (pp. 26-28): the PSP course itself can alter behavior; language experience and development environment are uncontrolled; data were collected for another purpose; tasks are numeric/statistical rather than production work; tests are limited; languages are older and exclude contemporary web languages; and conclusions need not generalize to all projects. Further limits are:

- the study analyzes industrial practitioners doing training assignments, not industrial project changes;
- task sequence, PSP training, and task difficulty are entangled;
- the same developers contribute repeated rows and repeated coefficients;
- belief selection was conditioned on available data, creating a compatibility/selection boundary;
- multiplicity is not handled across beliefs, tasks, languages, outcomes, and follow-up subsets;
- null results are presented without power or equivalence analysis;
- the course data predate publication by 15-26 years;
- the five beliefs were never elicited from the analytic participants.

The authors claim PSP instructor review supports fidelity and cite a prior 10-developer, 89-program manual-recording study with about 5% error (pp. 8, 26). That is relevant background, but it is not a direct error audit of this selected 13,560-row extract.

## Consequences for the Nu agenda

### R14 task/adoption provenance

S180 can change R14's evidence discipline in one concrete way. A task or adoption record should preserve at least three separate fields:

1. **Reported stance:** what a practitioner, issue author, maintainer, or source actually requested, preferred, or believed, including population and date.
2. **Empirical prediction:** the explicit, falsifiable outcome claim derived from that stance, with its scope and comparator.
3. **Observed evidence:** the historical or experimental outcome and its unit, missingness, and causal limits.

S180 shows the cost of collapsing those fields. Its "practitioner beliefs" are inherited literature propositions, while its evidence is retrospective training-task data. An issue request for easier authoring, a requirement for explicit state, or a preference for a language is not itself an empirical prediction and cannot be marked false because later history differs. Conversely, an observed project history does not establish how prevalent a preference is.

The paper supports auditing broad practice claims against multiple tasks, languages, and contexts and recording adverse/null outcomes. It does **not** establish present Nu demand, the prevalence of functional or data-oriented preferences, the representativeness of selected Nu tasks, current adoption barriers, or a language/framework causal advantage.

### R15 guidance and selection

Our R15 design inference is that these retrospective associations and inherited propositions do not by themselves validate prospective guidance. A defensible selector or architecture recommendation needs a prospective decision point, explicit alternatives, predeclared outcomes, held-out or future cases, total-work accounting, and calibration of uncertainty. S180's data-compatible proposition selection, post hoc task/language narrowing, self-selected treatment groups, and unmodeled repeated structure cannot validate such guidance.

The paper may motivate a falsifier for R15: if guidance derived from historical beliefs cannot predict outcomes on held-out tasks, languages, or projects better than a simple baseline, it should not be promoted. S180 itself does not provide or validate that predictive instrument.

### What cannot be inferred about Nu

S180 contains no Nu, F#, game-engine, interactive-software-evolution, live-editing, history, agent, or maintenance comparison. It does not compare Nu with C#, Godot, Unity, imperative architectures, or any ordinary-tool workflow. It cannot establish Nu benefit, cost, adoption, task fit, causal language effects, or agent accessibility. Any connection to Nu is a methodological transfer about evidence and construct separation, not a substantive benefit result.

## Artifact and access disposition

The official Zenodo record and archive were lawfully inspected without executing supplied code. The archive contains the selected data and analysis scripts and permits denominator checks. Static inspection shows that the retained batch invocation would select Cliff's delta where the article describes A12, but it does not bind that invocation to the actual publication-table run. It also exposes the correlation censoring described above. Full publication-run reproduction remains unresolved; the bounded independent calculation below has a separate, identified scope.

The Endres-Rombach handbook was identified bibliographically, but its body and the original five source works were not read in this assignment. Exact source formulations remain S180-reported. No version-of-record body was obtained. These are bounded lineage limitations, not reasons to treat the S180 reading itself as incomplete.


## Review, computation and preservation boundary

Parent review corrected three material overstatements before integration:
shared Scott-Knott rank is not equal size or a demonstrated universal
counterexample; the archived invocation is not established as the actual
publication run; and full visual coverage was by the same AI reader, not a
human. The Figure 6 C++ discrepancy and the coding-time versus broader-time
denominator discrepancy are retained alongside favorable associations.

A separately declared independent correlation check initially produced
no data analysis or results. Its first invocation failed because SciPy was
absent. After an isolated installation, its second invocation failed during
import, before opening the study archive. The installed source did not match
its package RECORD checksum; A: then reported Warning / Full Repair Needed.
The check stopped at that return, with no replacement calculation, supplied
analysis program execution or numerical reproduction credit from those attempts. The
[storage handoff](../../workspace-integrity-return-2026-10-26.md) preserves the
failure and verified C: copy. The completed text/visual reading and bounded
static artifact checks have distinct coverage from the calculation.

The later [independent C: reconstruction](S180-correlation-reconstruction.md)
completed the unchanged declared analysis: 146 computed correlations and four
preserved uncomputable cells among 150 planned cells. The significance-to-zero
rule replaces 35/50 B4 `ActMin` coefficients and makes four language medians
exactly zero; B3's coefficients are unchanged by that rule. The coding-time
sensitivity retains its four invalid cells without row deletion or incomplete
ten-task medians. This demonstrates the reporting/measurement consequence in
the specified new environment. It still does not identify the paper's actual
commands or historical versions, validate causal guidance, or reproduce its
Scott-Knott analyses. No new full-reading credit is added.

## References

Shrikanth, N. C., Nichols, W., Fahid, F. M., & Menzies, T. (2021).
*Assessing practitioner beliefs about software engineering*.
[arXiv:2006.05060v4](https://arxiv.org/abs/2006.05060v4).
Related journal record: *Empirical Software Engineering, 26*(4),
[DOI 10.1007/s10664-021-09957-5](https://doi.org/10.1007/s10664-021-09957-5).
These identify one work and related editions, not independent studies.

*Assessing practitioner beliefs about software engineering* (Version v1.0.0)
[Software and data]. (2021).
[Zenodo](https://doi.org/10.5281/zenodo.4553435).
