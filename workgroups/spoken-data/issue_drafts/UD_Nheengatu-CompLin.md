---
layout: base
title: 'Issue draft: Nheengatu CompLin'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Nheengatu CompLin](../treebanks/UD_Nheengatu-CompLin.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Nheengatu-CompLin](https://github.com/UniversalDependencies/UD_Nheengatu-CompLin)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Nheengatu-CompLin`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (no signal found):

**Finding:** Not identifiable from the data - almost every sentence carries a written-source citation, so presence/absence of a source field doesn't discriminate spoken vs. written.

**Evidence:** Of 2,839 sentences, 2,827 have at least one `text_*source` field (citing grammars, dictionaries, or Bible translations by page/verse); only 12 lack one, too few to correspond to a spoken subset. All sampled source values are published written works (Amorim, Rodrigues, Stradelli, bible.com).

**Suggestion:** Could you confirm whether any sentences originate from spoken/elicited fieldwork rather than the cited written sources, and if so how they're distinguished in the source data?

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field   | Suggestion                                                                           |
| ------- | ------------------------------------------------------------------------------------ |
| `title` | possibly rename to `newdoc id` (see Document-level in metadata.html) - please verify |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field                       | Suggestion                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------------- |
| `text_annotator`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `reviewer1`                 | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `speaker`                   | possibly rename to `speaker_id` (see Speaker-level in metadata.html) - please verify     |
| `reviewer2`                 | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `title_eng`                 | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `acknowledgement`           | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_orig_transcriber`     | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_sec_source`           | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_sec_source`       | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_translator`       | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `title_por_orig`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_modernizer`       | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `review_status`             | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `spelling_adaptation`       | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_alt_translator`   | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_gloss_modernizer` | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_transcriber`      | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `speaker_gender`            | possibly rename to `speaker_gender` (see Speaker-level in metadata.html) - please verify |
| `text_modernizer`           | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `ethnicity_orig`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field                            | Suggestion                                                      |
| -------------------------------- | --------------------------------------------------------------- |
| `text_eng`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_source`                    | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_orig`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `phrase_structure`               | corpus-specific (sentence-level) - verify against metadata.html |
| `title_por`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_alt`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_alt`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_alt_source`                | corpus-specific (sentence-level) - verify against metadata.html |
| `text_prim`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_prim`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_prim_transcriber`          | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_prim_modernizer`       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_prim_source`               | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_prim_source`           | corpus-specific (sentence-level) - verify against metadata.html |
| `inputline`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `cross_reference`                | corpus-specific (sentence-level) - verify against metadata.html |
| `text_source_orig`               | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_orig`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_prim_transcription`        | corpus-specific (sentence-level) - verify against metadata.html |
| `reviewer3`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_alt1`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_alt2`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_prim_transcriber`      | corpus-specific (sentence-level) - verify against metadata.html |
| `previous`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `next`                           | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_ggl`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_prim_gloss`            | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_gloss`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_adapt`                | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_gll`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_orig_transcriber`      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_prim_gloss_modernizer` | corpus-specific (sentence-level) - verify against metadata.html |
| `text_rus`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_rus_source`                | corpus-specific (sentence-level) - verify against metadata.html |
| `text_prim_por`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_prim_por_source`           | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_alt`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_alt_source`            | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_alt_source`            | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_pos`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_sec`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_sec`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_source`                | corpus-specific (sentence-level) - verify against metadata.html |
| `tex_por_alt`                    | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_source`                | corpus-specific (sentence-level) - verify against metadata.html |
| `alt_id`                         | corpus-specific (sentence-level) - verify against metadata.html |
| `text_source_url`                | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_alt`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_orig_alt`              | corpus-specific (sentence-level) - verify against metadata.html |
| `text_source_alt`                | corpus-specific (sentence-level) - verify against metadata.html |
| `title_orig`                     | corpus-specific (sentence-level) - verify against metadata.html |
| `place`                          | corpus-specific (sentence-level) - verify against metadata.html |
| `date`                           | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_lit`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_por`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_context`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `place_orig_por`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `narrator`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `ethnicity`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_translator`            | corpus-specific (sentence-level) - verify against metadata.html |
| `text_sec_alt`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_orig_sec`              | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_orig_sec_source`       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_adapt`                     | corpus-specific (sentence-level) - verify against metadata.html |
| `place_por`                      | corpus-specific (sentence-level) - verify against metadata.html |
| `title_number`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `title_por_gloss`                | corpus-specific (sentence-level) - verify against metadata.html |
| `variant_number`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `alt_id_error`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_gloss`                | corpus-specific (sentence-level) - verify against metadata.html |
| `place_orig`                     | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_corr`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `cross_reference1`               | corpus-specific (sentence-level) - verify against metadata.html |
| `cross_reference2`               | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_man`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_eng_man_translator`        | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_orig_source`           | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_sec_translator`        | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_source_adapt`          | corpus-specific (sentence-level) - verify against metadata.html |
| `text_transcriber`               | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_sec_alt`               | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_sec_alt_source`        | corpus-specific (sentence-level) - verify against metadata.html |
| `sent_number_orig`               | corpus-specific (sentence-level) - verify against metadata.html |
| `people`                         | corpus-specific (sentence-level) - verify against metadata.html |
| `note_por`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `subtitle_orig`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `note`                           | corpus-specific (sentence-level) - verify against metadata.html |
| `note_source`                    | corpus-specific (sentence-level) - verify against metadata.html |
| `text_adapt_source`              | corpus-specific (sentence-level) - verify against metadata.html |
| `text_sec_alt_source`            | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_part1`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_part2`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_part2_modernizer`      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_part1_translator`      | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_modern`                | corpus-specific (sentence-level) - verify against metadata.html |
| `title_orig_alt`                 | corpus-specific (sentence-level) - verify against metadata.html |
| `title_por_alt`                  | corpus-specific (sentence-level) - verify against metadata.html |
| `text_sec_pos`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_var`                       | corpus-specific (sentence-level) - verify against metadata.html |
| `text_adapter`                   | corpus-specific (sentence-level) - verify against metadata.html |
| `text_adapt_reviewer`            | corpus-specific (sentence-level) - verify against metadata.html |
| `comment`                        | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_alt_place`            | corpus-specific (sentence-level) - verify against metadata.html |
| `text_orig_total`                | corpus-specific (sentence-level) - verify against metadata.html |
| `text_por_sec_corr`              | corpus-specific (sentence-level) - verify against metadata.html |
| `chapter_title_por`              | corpus-specific (sentence-level) - verify against metadata.html |
| `text_author`                    | corpus-specific (sentence-level) - verify against metadata.html |

### 5. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field      | Suggestion           |
| ---------- | -------------------- |
| `OrigLang` | rename to `OrigLang` |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
