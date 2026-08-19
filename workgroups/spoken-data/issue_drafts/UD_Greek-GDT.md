---
layout: base
title: 'Issue draft: Greek GDT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Greek GDT](../treebanks/UD_Greek-GDT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Greek-GDT](https://github.com/UniversalDependencies/UD_Greek-GDT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Greek-GDT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. It's identifiable via the source-outlet component embedded in `document_id` (`gdt-<date>-<source>-<docname>`).

**Finding:** Sentences with `ep` as the source (e.g. `gdt-20020204-ep-sessions_*-*`) are transcripts of European Parliament plenary sessions (45 docs); `ert`/`ertonline` (Greek public broadcaster, 23 docs) are also spoken/broadcast material. `voa` (Voice of America, 8 docs) is written news text, grouped with `elwikinews`/`wikipedia`/`apogevmatini` (~94 docs total).

**Suggestion:** Add `# modality = spoken` to documents whose `document_id` source component is `ep`, `ert`, or `ertonline`.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                                                                                                                                                                                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `document_id` | make tags: doc_id                                                                                                                                                                                                                                                         |
| —           | add `# genre = speech` on `ep`-sourced documents (European Parliament plenary session transcripts)                                                                                                                                                                        |
| —           | add `# genre = news` on `ert`/`ertonline`-sourced documents (broadcast news)                                                                                                                                                                                              |
| —           | interaction-parameter classification for `ep` documents (please confirm): `degree_of_spontaneity = planned`, `number_of_participants = monologic`, `context = professional`, `setting = broadcast`, `symmetry = symmetric`                                                |
| —           | interaction-parameter classification for `ert`/`ertonline` documents (please confirm): `degree_of_spontaneity = planned`, `number_of_participants = monologic` (unless interview segments are present), `context = public`, `setting = broadcast`, `symmetry = symmetric` |

### Implementation notes

- **Needs a small script:** the modality tag is mechanical and verified against the real corpus (all three release files): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality DIR --spoken-if '\-(ep|ert|ertonline)\-' --written-if '.*' --write` gives 68 spoken documents (11 dev + 12 test + 45 train) - matching the draft's "45 `ep` + 23 `ert`/`ertonline` = 68" total exactly. The `# genre = speech` (on `ep` docs) and `# genre = news` (on `ert`/`ertonline` docs) additions follow the same pattern but with a fixed value instead of `spoken`/`written` - not yet a dedicated subcommand, but a ~10-line variant of `tag-modality` using the same regex groups would cover it.
- **Quick search & replace:** `document_id`→tag `doc_id` is a tagset addition, not a text rename - handle via the repo's tagset file rather than `rename-comment`.
- **Needs manual input from maintainers:** the proposed interaction-parameter values for `ep` and `ert`/`ertonline` documents (`degree_of_spontaneity`, `number_of_participants`, `context`, `setting`, `symmetry`) are genre-level defaults, not verified per document - need sign-off before scripting the inserts.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
