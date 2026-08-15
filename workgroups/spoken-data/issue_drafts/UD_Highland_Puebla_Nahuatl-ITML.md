---
layout: base
title: 'Issue draft: Highland_Puebla_Nahuatl ITML'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Highland_Puebla_Nahuatl ITML](../treebanks/UD_Highland_Puebla_Nahuatl-ITML.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Highland_Puebla_Nahuatl-ITML](https://github.com/UniversalDependencies/UD_Highland_Puebla_Nahuatl-ITML)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Highland_Puebla_Nahuatl-ITML`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken.

**Finding:** Identifiable via `sent_id`: sentences from spoken material carry a `.eaf` (ELAN annotation file) reference in their `sent_id`.

**Suggestion:** Add `# modality = spoken` to sentences whose `sent_id` contains `.eaf`.

### 2. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field         | Suggestion                                                      |
| ------------- | --------------------------------------------------------------- |
| `text[spa]`   | change to `text_spa`                                             |
| `text[orig]`  | change to `text_transcription`                                  |
| `text[gloss]` | change to `text_glossing` - unsure what this is, please confirm |
| `text[glosa]` | typo (duplicate of `text[gloss]`) - please confirm               |

### 3. Other / corpus-specific

`# text[a\d+] = ...` generates a very large number of distinct metadata labels (one per numbered variant). We suggest consolidating these into a single field, e.g. converting:

```text
# text[a134] = Ke:mah wa:n pos nika:n Kwesala:n tikitah, *este**, ki...,
# text[a136] = ki..., kinamakah a:mo ika *kilo**, ta: ata ika tamachi:w.
```

into:

```text
# text_original = [a134] Ke:mah wa:n pos nika:n Kwesala:n tikitah, *este**, ki..., [a136] ki..., kinamakah a:mo ika *kilo**, ta: ata ika tamachi:w.
```

### Implementation notes

**Quick search & replace**
- `text[spa]` → `text_spa`, `text[orig]` → `text_transcription` (`# oldkey =` → `# newkey =`).
- Tag modality: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality <path> --spoken-if '\.eaf'` (matched against `sent_id`, not `newdoc id` - the script currently only pattern-matches `newdoc id`, so this one needs a one-line tweak to match on `sent_id` instead, or a small adaptation; the underlying detection pattern itself is unambiguous, 499/… sentences carry `.eaf`).

**Needs a small script**
- Consolidate the ~136 `# text[a<N>] = ...` comments per file into one `# text_original = [a134] ... [a136] ...` field, in file order. Purpose-built helper, tested against the real corpus:
  `python3 workgroups/spoken-data/scripts/consolidate_text_variants.py <path> --pattern 'text\[(a\d+)\]' --into text_original --write`

**Needs manual input from maintainers**
- `text[gloss]` → `text_glossing`: unsure what this field represents, please confirm before renaming.
- `text[glosa]`: looks like a duplicate/typo of `text[gloss]` - please confirm whether to drop or merge.
