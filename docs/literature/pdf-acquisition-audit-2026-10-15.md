# PDF acquisition audit — 15 October 2026

## Scope and method

This is a bounded acquisition and attachment audit, not a substantive reading record. It checks the nine named access gaps and the three long-form records returned for completeness review by the remote Zotero inventory. All twelve parents remain in collection `PKLXQNEE`; `RFWD6G8J` also retains `IPZX66LF`.

The live native Zotero 10.0.6 API was guarded against the saved server identity. For each parent, the audit enumerated current children, resolved each stored file through Zotero, checked the actual file and `%PDF-` header, computed SHA-256, opened every PDF page with PyMuPDF and retained only bounded first/last-page identity evidence. The image-only S305 report received a separate visual cover and final-page check. The private machine-readable receipt is `.artifacts/pdf-acquisition-20261015/native-audit.json`; it contains paths and short identity prefixes, not full extracted bodies.

## Why the inventory reported zero missing

`rvl_zotero.py inventory` treats a journal or conference parent as complete when any child advertises `contentType=application/pdf`; it does not inspect stored bytes, title/edition, page count or document scope. Books and theses are the only types retained for completeness review after a PDF child is found. The reported `0 missing PDF; 3 existing-PDF completeness review` therefore meant that every journal/conference parent had some PDF child, not that all named originals or final editions were present.

The direct audit confirms that eight of the nine named paper gaps had already gained exact full-paper attachments on 12 October. The remaining S305 child is a complete 1990 technical report, not the cited 1991 journal edition.

## Named paper parents

| ID / parent | Existing PDF child and actual identity | Bytes / pages / SHA-256 | Disposition |
| --- | --- | --- | --- |
| S304 `3WWYJF9W` v6493 | `BFXMFI8D` v6728; published CHI 1991 paper, exact title/authors | 865,601; 6 pages; `2921f2d6c49443e02a4b43ec1f16c5d67ccf4e79e359d59c334da99a62432511` | Exact full conference paper; all pages parse. |
| S305 `VFB2TP7A` v6495 | `4U6YX9BT` v6708; **CU-CS-479-90, June 1990 technical report**, visually verified from its cover | 4,667,552; 60 PDF pages, ending at numbered report page 52; `c255b096392fb14c62e3e35f28863221cb57849c2fd85cd4aaa7b3cc6d93d937` | Complete image-only technical report; zero extractable text. It is not the Human–Computer Interaction 6(3–4), 319–355 final edition and does not establish edition equivalence. |
| S306 `NV7J7ACD` v6497 | `MJN2JFIC` v6718; publisher PDF, *Software—Practice and Experience* 24(1), 1–25, January 1994 | 1,820,560; 25 pages; `15e434c62edebf7f79f945dc52480a6578d1317039b0bd07c064e9682bcaf4de` | Exact full journal article; all pages parse. |
| S253 `ERL3ILFC` v5560 | `ZJMGCLNC` v6734; published conference paper, exact title/authors | 765,034; 6 pages; `8a9e413f0c6d42787da5feba9f4cc52016a523e39aacd14bd186de5c6d8666c9` | Exact full conference paper; all pages parse. Existing indexed-text child `BLZHQZJC` remains a separate derivative. |
| S254 `GQVDG772` v5569 | `UCRAGLXA` v6693; journal-layout *Information and Software Technology* paper | 4,746,029; 14 pages; `ca0c6a87f27ce065128e9436139b103e222359d4b07b1557b515c845289abf9b` | Exact full journal paper; all pages parse. Existing preprint text and replication ZIP remain separate lineage/support files. |
| S263 `VG8B7V8U` v5701 | `UHXDE9LI` v6732; published SPLC 2024 paper, pp. 113–124 | 1,399,877; 12 pages; `bc32696775592995593b7d3ee0b9e1513e64280bb61dbc0804768776818050ee` | Exact full conference paper; all pages parse. |
| S264 `9E4I7XE9` v5703 | `RTCZRCB8` v6695; journal-layout *Journal of Systems & Software* paper | 2,195,022; 16 pages; `10e3a0e3c6076774dae6d2281dc6a9298790f4655ed623aa3e1804fa6acf8000` | Exact full final journal paper; all pages parse. SSRN correspondence remains a separate lineage question. |
| S266 `7SLKDL8C` v5724 | `LIHKR9VA` v6637; SSRN preprint, explicitly marked not peer reviewed | 555,179; 33 pages; `e61da6b8da8f7f408bc1a6128583e3ae3b202852c28b88eb863189f5c2d81dc2` | Exact full selected preprint; all pages parse. Existing `GHETLQZF` remains an abstract-only text derivative. |
| S285 `53D9GIMM` v5880 | `6556W8FI` v6631; ACM TOG **38(6)**, article 159, *SceneGit* | 67,513,366; 15 pages; `be79bc0e13f4e49daee7975f461e2b3499a1888218d1e1b805adc33b6f10470e` | Exact November 2019 full journal article; the PDF cover/running headers and native parent agree on volume 38. All pages parse. Existing `7V6ABH46` remains an abstract-only text derivative. |

## Long-form completeness review

| Parent | Existing PDF children and evidence | Scope disposition |
| --- | --- | --- |
| `2IXS2XZF` v5821, *Étude de faisabilité du runtime monitoring dans les jeux vidéo* | `ZNGSJWM2` v5819; 3,063,571 bytes; 87 pages; SHA-256 `cc0f1c799b84673550a74ed135f60b8270cf9f0bc1023ba786bfa17ae90eeeca`. Title page identifies the UQAC master's thesis and January 2014; ending pages contain the complete numbered reference tail through p. 75. | Full thesis, not front matter or excerpt. All 87 pages open; 80 contain extractable text. |
| `VY3FT5TX` v5756, *The Unlimited Rulebook* | `EQTPC8GB` v5753, USP corrected thesis edition: 26,722,768 bytes, 191 pages, SHA-256 `adac9d0bf1c0045797021a26ecdd74870fe811c8cd390d291f97f98fbc5df953`; `64YJKF87` v5748, author-hosted thesis edition: 26,090,775 bytes, 191 pages, SHA-256 `80ebc5d9828ba60aad5036b62228eed743d41d338d999e7240312bda369c9a9d`. Both identify the September 2021 doctorate and corrected post-defense version and end with references/ludography. `4FSGB37H` v5754 is a separate 11-page August 2020 interview protocol, SHA-256 `dd0af95c7082325f5b0cd550a5e081e766c4412ca3489a6634b94f24cf75effa`. | Two existing full-thesis files with different bytes and the same observed selected identity/end matter; no claim of byte or complete semantic equivalence. The protocol is a supplement, not the thesis. |
| `RFWD6G8J` v4960, *Seamless Concurrent Programming of Objects, Aspects and Events* | `TY27SXGM` v4956; 1,643,081 bytes; 233 pages; SHA-256 `9346fc6d38ee044a9a2c56af54481f89c48ccd20e0f8de7b3130986dfdcfd204`. HAL cover and dissertation title pages identify the 2015 joint doctorate; final page contains the bilingual thesis abstract/back matter. | Full thesis, not front matter or excerpt. All 233 pages open; 214 contain extractable text. |

## Bounded final-edition attempt and remaining barrier

The only residual named acquisition gap is S305's 1991 *Human–Computer Interaction* journal edition. A fresh queue used the modern publisher alias `10.1080/07370024.1991.9667171` while preserving the parent DOI `10.1207/s15327051hci0603&4_5`. The helper initially classified accessibility strings as a verification challenge, but the user's authoritative screenshot showed the rendered DOI Foundation page actually said **DOI NOT FOUND** for that alias. The resulting request for human verification was mistaken and was withdrawn; no such action was needed. The official Taylor & Francis article page independently verifies the exact title, Lewis/Rieman/Bell authorship, volume 6 issues 3–4, pages 319–355 and publication identity at `https://www.tandfonline.com/doi/abs/10.1080/07370024.1991.9667171`. The existing task tab was navigated directly to that publisher page and then to its official `.../doi/epdf/10.1080/07370024.1991.9667171?needAccess=true` link. The `epdf` page's actual accessibility text identifies the exact article and says **Get Access**, **Log in via your institution**, and **PDF download + Online access / 48 hours access**. The bounded helper found neither accessible PDF bytes nor a verified download route; purchasing, a trial and a new login were outside the authorized scope. A separate MHTML snapshot attempt on the abstract page stopped before saving because the native Save As filename control did not commit the exact requested path; it supplied no page-body evidence and created no local snapshot. Task `20261015T132406-aac5665a` remains saved under `.artifacts/pdf-acquisition-20261015/s305-final-run/` with the official `epdf` access page open in the original task-owned tab. No candidate bytes were downloaded, reviewed or attached. The existing technical report is sufficient for a separately labelled report-edition reading, but not for a final-edition or exact-correspondence claim.

This audit reused fourteen existing PDF children across twelve parents: eight exact full paper/preprint PDFs, one complete technical report, four full-thesis files and one interview-protocol supplement. It downloaded **0**, attached **0**, and created **0** duplicates. The PDF presence findings supersede the older absence statements only; they do not establish reading coverage or change scientific conclusions until the relevant papers are reconstructed and integrated.

## Second native attachment reconciliation

A later read-only audit checked remaining access statements against native
collection `PKLXQNEE`. It found ten more local bodies. No download, tab opening,
Zotero mutation or paper-body reading occurred during this acquisition audit;
subsequent readings have separate coverage receipts. The exact audit is saved
privately in `.artifacts/remaining-pdf-audit-20261015/reconciliation.json`.

| Work / edition | Parent version | PDF version | Pages / bytes | SHA-256 |
| --- | --- | --- | --- | --- |
| S240, Pixel 15(2),254–266 | `Y5VD4GHT` v5445 | `WX4AFBYI` v5512 | 13 / 918,452 | `1adcd87739f8a1ac2a7d016810d708a3dcb78d2a34d63d626af3a86c2d655627` |
| S265, final journal article | `DMZN5HBS` v5709 | `4QRS6N42` v6691 | 15 / 3,165,249 | `55888c06e3f3906b9f10bfa716918b20c94630af5e4d4c4aa7c1208ddb3a9a4a` |
| S272, IEEE/GAS 2015 | `65ZQHDSY` v5770 | `9MDVQYLC` v6740 | 7 / 158,593 | `90c400c1c367994d18ae580648a9bbc1eb7e12320b677072cf27bda2571c4681` |
| S273, licentiate thesis inner body | `EXNYNNFZ` v6837 | `U7ZHDKJX` v6839 | 98 / 1,677,504 | `eb14868217cd6c6bc45ee26acea21d1f99dd83f8170350a3da0198f12a1554aa` |
| S274, SuBViS conference paper | `BDIULBB9` v5774 | `SPFK8U3V` v6730 | 11 / 725,534 | `9cbda76d1bc12d4c66b8b5b3fdf0a4571f292cec3bad45f0f1d4bf19b2d31659` |
| S275, BPAlt journal article | `9LNAAB57` v5780 | `Z7NRDBW8` v6689 | 16 / 9,620,630 | `1fcaa9a2c584c0a2651847ed843e470222d19dde1410d4d68a7c64e0de1bd91b` |
| S279, expanded journal article | `GDCSUS2I` v5813 | `TRQ4KJAC` v6635 | 28 / 1,392,026 | `76095506f42097b1d63ddc2fad9d3597ec2473f46eeefb9e0ee0f96c7ce46743` |
| S280, IEEE/ICST 2014 | `RQN7VPZM` v5815 | `H4QLJ685` v6738 | 10 / 715,155 | `22adf53044d226450a9deae3ba65f271e7bc043412ca1f7c7bb70d60f7879232` |
| S282, PACMHCI 6/CHI PLAY article245 | `AQRML7QI` v5831 | `FU3P6Z22` v6633 | 31 / 6,998,068 | `b62b3c43c64285c084f96dc8612451efddb044c2bd3b3c6481c189f5d065b3e5` |
| S286, TOG 42(6) journal article | `BQG8UT5U` v5886 | `JUFDJX8H` v6669 | 12 / 21,967,350 | `3df0cd5b0bb6c22532f3e392017e95fa06c44b91b0f70ea81cd4153311e1e598` |

The initial audit called S286 an ACM conference paper; the original identifies
the selected edition as a TOG journal article. S273 starts at its abstract and
has blank PDF title/author metadata. Its outer cover/title leaf is absent. The
assigned reading must bind the abstract, institutional identity and numbered
extent before claiming complete available-body coverage; the file is not
assumed equivalent to a cover-inclusive institutional package. Reading and
integration status belong to the [reading index](full-reading/INDEX.md).

### Subsequent accepted reading coverage

All ten bodies in this second reconciliation were subsequently read at the
scopes recorded in their linked full-reading notes, raising the current
checkpoint to **281 = 13 P + 3 A + 265 S**. This later reading completion does
not change the acquisition result: the reconciliation still downloaded **0**,
attached **0**, created **0** duplicates and made no Zotero mutation. These are
ten publication/work readings, not ten independent empirical studies; the
S272/S273 and S279/S280 edition/case lineages, the S274/S275 follow-on lineage
and S282's shared infrastructure with S283 remain explicit.

S273's accepted scope is the complete available 98-page inner thesis body.
The prior registered catalog record, author-deposit abstract/contents and
internal study lineage support its identity and extent; the live institutional
route was unavailable. The absent outer cover/title leaf and blank PDF
title/author metadata remain provenance limits. S286's selected body is the twelve-page **ACM
Transactions on Graphics 42(6) journal article**, correcting the initial
conference-paper label. The original attachment identities, page counts,
bytes and hashes in the table above remain the acquisition receipt.

### Later S262 VOR acquisition and accepted reading — 2026-10-15

After the two zero-acquisition audits above, the already authorized integration
acquired **one** additional exact PDF and attached **one** new child for S262.
This is a separate dated event and does not revise either earlier audit's zero
result. Parent `PKVMQLQ2` remained version 5688 with its bibliographic data and
collection membership unchanged; only its child count increased. New imported
attachment `LGLJ8WXT` version 7115 is the ACM version of record for
*Phylogenix: Bringing phylogenetics to Unity*, SPLC 2024 Volume B, pp. 38–41,
DOI `10.1145/3646548.3676604`: **1,978,099 bytes**, **4 pages**, SHA-256
`2980ef35ccff890303c576838d258c86f213c37179181bb4a701e74af7e2154e`.
Page 1 visibly confirms the title, five authors, venue, extent and DOI. The
acquisition receipt is
`.artifacts/s262-acquisition-20261015/acquisition-receipt.json`; the earlier
children were preserved and no second same-hash PDF child was created.

The body was subsequently accepted as one complete publication reading: all
four pages, Figures 1–3, Table 1, footnotes, acknowledgments and all 32
references were read and visually inspected. Its exact scope and the unresolved
Figure 1 notation are recorded in [the S262 note](full-reading/S262-phylogenix-integration-partial.md)
and `.artifacts/s262-reading-20261015/coverage-receipt.json`. Exact source/build
correspondence, viewer bodies, video, project snapshots, hardware/timing
protocol and reproduction remain open. The four Unity projects overlap the
later S254 Phylogenix cases, so this is one publication-reading increment, not
an independent-study increment. The current checkpoint is therefore
**282 = 13 P + 3 A + 266 S**.

### Later S206 publisher-volume acquisition and accepted reading — 2026-10-15

After the zero-acquisition audits and the separately dated S262 event above,
the authorized integration downloaded **one** publisher source volume and
attached **one** exact article derivative for S206. This later event does not
revise any earlier acquisition count. The publisher source is the complete
610-page LNCS 6183 volume: **9,348,114 bytes**, SHA-256
`3f9c290a84dee40c4bc337070c11d53577e9e4a04897574147dee88b581c65dd`.
Only source PDF leaves 311–314, corresponding to printed pp. 300–303, were
extracted and attached as the article; the volume's other 606 pages receive no
reading credit.

At acquisition, parent `TCF847EU` remained version 4983 with bibliographic data
and memberships unchanged; only its child count increased. Later canonical
note/tag maintenance and final versions are recorded in the
[background ledger](nu-background-searches-2026-09-30.md#s206-publisher-completion-and-s132-lineage-reconciliation-2026-10-15).
New imported attachment `VCD95IIU`
version 7119 is the exact four-page publisher VOR of Stefan Hanenberg,
*Doubts about the Positive Impact of Static Type Systems on Programming Tasks
in Single Developer Projects — An Empirical Study*, ECOOP 2010 / LNCS 6183,
pp. 300–303, DOI `10.1007/978-3-642-14107-2_14`: **122,120 bytes**, **4
pages**, SHA-256
`37728b772a2306074172761cb994e8d30c3ff68996052a801c955858fd72fe74`.
The historical two-page preview `TDV38UY3` version 4985 remains unchanged, and
no second same-hash article child was created. The exact acquisition receipt is
`.artifacts/s206-acquisition-20261015/acquisition-receipt.json`.

All four article pages, Figure 1's scanner/parser boxplots and all nine
references were subsequently read and visually inspected. The accepted scope
is in [the S206 note](full-reading/S206-ecoop-type-study-partial.md) and
`.artifacts/s206-reading-20261015/coverage-receipt.md`. Matching author,
49-person sample, scanner/parser task, language treatment, training, outcomes
and p-values strongly support one experiment lineage with S132 rather than an
independent replication. Exact participant, log and test-suite identity is
unverified, and S206 prints 25 hidden scanner tests where S132 prints 23. The
unlocated intermediate technical report, primary logs, source programs, hidden
tests, participant data and analysis code remain provenance or artifact gaps,
not S206 body gaps. This publication increment makes the current checkpoint
**283 = 13 P + 3 A + 267 S**.

Primary-body gaps remain for S305's journal, S221's
original/revised-chapter remainder, S152's dissertation and S153's
dissertation. S206 no longer has a primary-body gap. S305's previously listed
report attachment has
since been moved, with its lineage preserved, to the separate report parent
`KJKJRYQA`; the old journal parent remains `VFB2TP7A` v6495. The report reading
does not close the journal gap. S01,S20,S27,S75,S198,S231,S241,S247,S255,S267,
S270,S276,S278,S284,S288 and S303 have usable alternate editions with explicit
final-edition correspondence limits. Selected supplements remain missing for
S30,S210,S249,S260,S265,S284 and S293. S144's main paper and 31-page design
supplement are both local; its remaining selected-coverage limit is reading,
not acquisition. These are exact residual scopes, not evidence that a method
or research direction is absent.

## S305 supplied journal reconciliation, 2026-10-18

The user updated existing journal parent `VFB2TP7A` to DOI
`10.1080/07370024.1991.9667171` and attached `54NZJ2S2` before reading.
The [complete reading and edition comparison](full-reading/S305-problem-centered-design-journal-reading-2026-10-18.md)
now supersedes the earlier journal access gap without changing the failed
route history. The PDF is 2,159,372 bytes / 39 pages, SHA256
`fbd75ba736d0ddf629d3eba15802e54ea1b26ebed2b9da6658107691697ad511`,
MD5 `99513a6d3c10bcc329f251dc0974930f`. Two publisher leaves precede the
37-page article, pp.319-355. All text and all 11 figures were inspected.

Native Zotero 10.0.6 API reconciliation retains the `journalArticle` type,
parent key, collection `PKLXQNEE`, 1991 date, citation key
`lewis_problem-centered_1991`, both PDF attachments and separate report parent.
The journal URL now points to the verified publisher page; legacy DOI
`10.1207/s15327051hci0603&4_5` remains in Extra with the supported identity and
formal-alias limits. Stale access-gap tags/Extra and the managed note were
updated. Verified versions: journal 7462 to 7470, note `CEE3V4N8` 6897 to 7472,
report `KJKJRYQA` 6875 to 7473; PDFs remain 7461 and 6868 respectively.
The initial exact-array checks flagged reordered tag arrays only; subsequent
canonical verification confirmed every field, tag membership and attachment,
with all earlier receipts retained. No compensating metadata rewrite occurred.

The journal adds the same S304 prototype study and removes the report appendix;
no work/study count is added. No remote fetch or new Zotero item was needed.
Private API snapshots, guarded write/readback receipts, metadata evidence,
PDF renders and extraction remain in the C: recovery reconciliation directory,
outside Git. CU-CS-480-90 remains unread.
