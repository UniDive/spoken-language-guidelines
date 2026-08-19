---
layout: base
title: 'Issue draft: English GENTLE'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to English GENTLE](../treebanks/UD_English-GENTLE.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_English-GENTLE](https://github.com/UniversalDependencies/UD_English-GENTLE)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_English-GENTLE`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Mark spoken documents with `# modality`
The spoken portion of this treebank is identifiable via `meta::genre = esports`, which points to exactly 2 of the 26 documents:

| `document_id` | Title | Source |
|---|---|---|
| `GENTLE_esports_fifa` | CHAMPIONS LEAGUE SEMI-FINAL!!! FIFA 20 AC MILAN CAREER MODE #16 | [YouTube](https://www.youtube.com/watch?v=afGtqs-_LBo) |
| `GENTLE_esports_fortnite` | WORLD CUP SOLO'S FINAL MATCH \| Fortnite World Cup Game 6 \| Live commentary | [YouTube](https://www.youtube.com/watch?v=_zRaMRXCMrQ) |

Both are live esports commentary videos - the other 6 `meta::genre` values (`poetry`, `threat`, `medical`, `dictionary`, `proof`, `legal`, `syllabus`) are written or mixed registers.

**Suggestion:** Add `# modality = spoken` to `GENTLE_esports_fifa` and `GENTLE_esports_fortnite`, and `# modality = written` to the rest.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field | Suggestion |
|---|---|
| `document_id` | make tags: doc_id |
| `meta::genre` | make tags: genre |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| `speaker` | make tags: speaker_id |

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `meta` | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

- **Quick search & replace:** `document_id`→tag `doc_id`, `meta::genre`→tag `genre`, `speaker`→tag `speaker_id` are plain renames: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map meta::genre=genre,speaker=speaker_id --write` (the `document_id`→`doc_id` "tag" is a UD tagset addition, not a comment rename - handle via the repo's tagset file).
- **Needs a small script:** the modality tag is mechanical once the genre→modality mapping is fixed - verified against the real corpus (`en_gentle-ud-test.conllu`): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality DIR --spoken-if '_esports_' --written-if '.*' --write` correctly isolates `GENTLE_esports_fifa`/`GENTLE_esports_fortnite` as the only 2 matches out of 26 documents, matching the draft's finding exactly.
- **Needs manual input from maintainers:** the `meta` sentence-level field is corpus-specific with no proposed name yet - needs a maintainer decision on what it holds before it can be classified or scripted.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
