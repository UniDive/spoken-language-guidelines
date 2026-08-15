---
layout: base
title: 'Issue draft: Naija NSC'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Naija NSC](../treebanks/UD_Naija-NSC.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Naija-NSC](https://github.com/UniversalDependencies/UD_Naija-NSC)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Naija-NSC`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but it can be derived from the `sent_id` prefix (please confirm the exact delimiter/recording identifier).

| Field       | Suggestion                                                                           |
| ----------- | ------------------------------------------------------------------------------------ |
| —           | derive `# newdoc id` from the `sent_id` prefix identifying the source recording      |
| `sound_url` | possibly move to document level |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------- |
| `text_ortho` | change to `text_orthographic`  |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### Implementation notes

**Quick search & replace**
- `text_ortho` → `text_orthographic` (`# text_ortho =` → `# text_orthographic =`).
- `AlignBegin` → `WordAlignmentBegin`, `AlignEnd` → `WordAlignmentEnd` (token-level MISC keys):
  `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc <path> --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`

**Needs a small script**
- Derive `# newdoc id` from `sent_id`: the released files (`pcm_nsc-ud-{train,dev,test}.conllu`) use a clean `<DOC>__<N>` pattern (e.g. `ABJ_GWA_14_Mary-Lifestory_MG__1`), confirmed by dry-run:
  `python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc <path> --pattern '^(?P<doc>.+)__\d+$' --write`
  (10/10 documents in `pcm_nsc-ud-test.conllu` derived cleanly.)
- Move `sound_url` to document level, **after** the derive-newdoc step above:
  `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc <path> --key sound_url --write`
  ⚠️ Dry-run turned up a discrepancy worth flagging to maintainers before running for real: 2 of the 10 documents in `pcm_nsc-ud-test.conllu` have **two distinct `sound_url` values** within the same derived document (not fully constant), so those 2 would be skipped by the script and need manual resolution rather than an automatic hoist.

**Needs manual input from maintainers**
- Confirm the `sent_id` delimiter/pattern above is correct for the whole corpus (not just the sample checked here), and resolve the 2 documents with non-constant `sound_url` before hoisting.
