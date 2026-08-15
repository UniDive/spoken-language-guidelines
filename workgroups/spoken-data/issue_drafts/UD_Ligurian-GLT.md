---
layout: base
title: 'Issue draft: Ligurian GLT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Ligurian GLT](../treebanks/UD_Ligurian-GLT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Ligurian-GLT](https://github.com/UniversalDependencies/UD_Ligurian-GLT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Ligurian-GLT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (a weak signal):

**Finding:** Only 12 documents total, with mixed short prefixes - too few for an automatic pattern, but small enough to check by hand. The README mentions a radio broadcast among the sources, but we couldn't work out which `newdoc id`(s) or sentences it corresponds to.

**Evidence:** `newdoc id` values: `bdl-c00`, `cairo`, `esl-c01`, `wp-arba`, `wp-tintin`, and others (12 total, no dominant separator/prefix pattern).

**Suggestion:** Since there are only 12 documents, could you confirm per-document whether each is spoken or written (e.g. do `wp-*` mean Wikipedia/written, is `cairo` a transcribed story), and specifically which document(s) correspond to the radio broadcast mentioned in the README?

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field         | Suggestion                                                      |
| ------------- | --------------------------------------------------------------- |
| `parallel_id` | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

**Needs manual input from maintainers**
- Modality: only 12 documents total, no dominant naming pattern - needs a per-document call from maintainers (spoken vs. written for each of `bdl-c00`, `cairo`, `esl-c01`, `wp-arba`, `wp-tintin`, and the rest), plus identification of which document(s) correspond to the radio broadcast. With only 12 documents this is faster to answer directly than to script; once the per-document list exists, tagging via `harmonize_metadata.py tag-modality --spoken-if '<confirmed ids>'` (or a plain per-document `rename-comment`/manual edit, since 12 is small) is trivial.
- `parallel_id`: corpus-specific field, needs a decision on whether/how it maps to the naming conventions before any action.
