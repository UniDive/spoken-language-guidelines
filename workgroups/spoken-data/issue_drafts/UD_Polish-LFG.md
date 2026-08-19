---
layout: base
title: 'Issue draft: Polish LFG'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Polish LFG](../treebanks/UD_Polish-LFG.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Polish-LFG](https://github.com/UniversalDependencies/UD_Polish-LFG)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Polish-LFG`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (fairly confident):

**Finding:** Identifiable via the sentence-level `genre` field, which has explicit spoken values.

**Evidence:** `genre` (10 distinct values) includes `spoken (conversational)` (789), `spoken (prepared)` (306), `spoken (media)` (158) = 1,253 sentences, alongside `fiction` (7,252), `news` (6,744), `nonfiction` (1,273), `social` (526), `blog` (136), `academic` (51), `legal` (11).

**Suggestion:** Add `# modality = spoken` to sentences whose `genre` starts with `spoken`. `genre` also currently packs two things into one string: the top-level category (`spoken`) and a parenthetical sub-type (`conversational`, `prepared`, `media`). We suggest decomposing this into `# genre` plus the optional [interaction-parameter layer](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#interaction-parameters-optional-add-on):

| `genre` value             | Suggestion                                                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `spoken (conversational)` | split into `# genre = conversation` + `# degree_of_spontaneity = unplanned`                                                      |
| `spoken (prepared)`       | split into `# genre = speech` + `# degree_of_spontaneity = planned`                                                              |
| `spoken (media)`          | split into `# genre = spoken` (or a more specific value, please confirm - radio show/TV show/podcast?) + `# setting = broadcast` |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field                           | Suggestion                                                      |
| ------------------------------- | --------------------------------------------------------------- |
| `This program is free software` | corpus-specific (sentence-level) - verify against metadata.html |
| `converted_from_file`           | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

**Needs a small script**
- Tag `# modality = spoken` on sentences whose `genre` starts with `spoken`: `genre` is sentence-level (not doc-level), so this isn't the `tag-modality` subcommand (which keys off `document_id`) - it needs a short script that reads the `genre` comment per sentence and inserts `# modality = spoken`/`written` next to it directly (adapting the `tag-modality` logic to match on `genre` instead of `document_id`, ~15 lines).
- Splitting `genre` into `# genre` + `# degree_of_spontaneity`/`# setting`: once the three-way mapping is confirmed (see below), this is a per-value lookup-and-rewrite (not a generic separator split, since `spoken (media)`'s target genre value is still open - "please confirm"), so also needs a short custom script rather than `split-field`.

**Needs manual input from maintainers**
- The `genre = spoken (media)` → `# genre` value is explicitly unconfirmed ("radio show/TV show/podcast?") - needed before the script above can be finalized.
- `This program is free software` and `converted_from_file` - corpus-specific fields needing clarification/confirmation before any action.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
