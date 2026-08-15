---
layout: base
title: 'Issue draft: Ika ChibErgIS'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Ika ChibErgIS](../treebanks/UD_Ika-ChibErgIS.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Ika-ChibErgIS](https://github.com/UniversalDependencies/UD_Ika-ChibErgIS)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Ika-ChibErgIS`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                                                                           |
| ----------- | ------------------------------------------------------------------------------------ |
| `sound_url` | possibly rename to `sound_url` (see Document-level in metadata.html) - please verify |

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field            | Suggestion             |
| ---------------- | ---------------------- |
| `morphemic_text` | make tags: annot_morph |

### 3. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

### Implementation notes

**Quick search & replace**
- `morphemic_text` → `annot_morph` (`# morphemic_text =` → `# annot_morph =`).
- `AlignBegin` → `WordAlignmentBegin`, `AlignEnd` → `WordAlignmentEnd` (token-level MISC keys):
  `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-misc <path> --map AlignBegin=WordAlignmentBegin,AlignEnd=WordAlignmentEnd --write`

**Needs a small script**
- None outstanding - `sound_url` is already present under the standard name in `arh_chibergis-ud-test.conllu` (verified), so item 1 needs no change once confirmed (see below).

**Needs manual input from maintainers**
- `sound_url`: the draft flags this as "possibly rename to `sound_url`" - the field is already named `sound_url` in the released data, so this looks like a leftover from an earlier check; please just confirm no change is actually needed here.
