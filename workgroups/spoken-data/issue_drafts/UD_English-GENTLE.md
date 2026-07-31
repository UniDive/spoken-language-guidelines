---
layout: base
title: 'Issue draft: English GENTLE'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to English GENTLE](../treebanks/UD_English-GENTLE.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_English-GENTLE](https://github.com/UniversalDependencies/UD_English-GENTLE)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_English-GENTLE`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Mark spoken documents with `# modality`
The spoken portion of this treebank is identifiable via `meta::genre = esports`, which points to exactly 2 of the 26 documents:

| `newdoc id` | Title | Source |
|---|---|---|
| `GENTLE_esports_fifa` | CHAMPIONS LEAGUE SEMI-FINAL!!! FIFA 20 AC MILAN CAREER MODE #16 | [YouTube](https://www.youtube.com/watch?v=afGtqs-_LBo) |
| `GENTLE_esports_fortnite` | WORLD CUP SOLO'S FINAL MATCH \| Fortnite World Cup Game 6 \| Live commentary | [YouTube](https://www.youtube.com/watch?v=_zRaMRXCMrQ) |

Both are live esports commentary videos - the other 6 `meta::genre` values (`poetry`, `threat`, `medical`, `dictionary`, `proof`, `legal`, `syllabus`) are written or mixed registers.

**Suggestion:** Add `# modality = spoken` to `GENTLE_esports_fifa` and `GENTLE_esports_fortnite`, and `# modality = written` to the rest.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field | Suggestion |
|---|---|
| `newdoc id` | make tags: doc_id |
| `meta::genre` | make tags: genre |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| `speaker` | make tags: speaker_id |

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `meta` | corpus-specific (sentence-level) - verify against metadata.html |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
