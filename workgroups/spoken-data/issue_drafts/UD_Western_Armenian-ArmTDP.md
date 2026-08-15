---
layout: base
title: 'Issue draft: Western_Armenian ArmTDP'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Western_Armenian ArmTDP](../treebanks/UD_Western_Armenian-ArmTDP.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Western_Armenian-ArmTDP](https://github.com/UniversalDependencies/UD_Western_Armenian-ArmTDP)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Western_Armenian-ArmTDP`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (fairly confident):

**Finding:** Identifiable via the `newdoc id` prefix, which already encodes genre.

**Evidence:** `newdoc id` values are `genre-code`, e.g. `spoken-002R`. Full prefix distribution: news (38), fiction (16), blog (15), nonfiction (9), wiki (7), reviews (3), web (2), spoken (2), social (1).

**Suggestion:** Add `# modality = spoken` to the 2 documents whose `newdoc id` starts with `spoken-`.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                                                                                                                             |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `doc_title` | `newdoc id` already exists separately (e.g. `spoken-002R`); `doc_title` is the human-readable document title - keep as corpus-specific |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion                                                      |
| ---------- | --------------------------------------------------------------- |
| `translit` | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

- **Needs a small script:** add `# modality = spoken` to the 2 documents whose `newdoc id` starts with `spoken-` (`spoken-002R` and one other). Intended one-liner is `harmonize_metadata.py tag-modality UD_Western_Armenian-ArmTDP --spoken-if '^spoken-' --write`, but note the shared script's `COMMENT_RE` currently only matches single-word comment keys (`[A-Za-z_][A-Za-z0-9_]*`), so it silently fails to recognize `# newdoc id = ...` (a two-word key) - confirmed via dry-run against the local clone (0 matches reported, when there should be 2). Until that regex is widened to allow spaces in the key, use a plain search & replace instead: `sed -i '' '/^# newdoc id = spoken-/a\
# modality = spoken' *.conllu`.
- **Needs manual input from maintainers:** `translit` - corpus-specific field, needs a naming decision. `doc_title` needs no change (kept as corpus-specific, distinct from `newdoc id`).

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
