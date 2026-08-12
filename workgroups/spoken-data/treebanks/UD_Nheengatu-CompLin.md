---
layout: base
title: 'Nheengatu CompLin'
udver: '2'
---

# Nheengatu CompLin

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | mixed                                                                                                                          |
| **available since** | 2.11                                                                                                                           |
| **link**            | [https://github.com/UniversalDependencies/UD_Nheengatu-CompLin](https://github.com/UniversalDependencies/UD_Nheengatu-CompLin) |
| **genre**           | spoken bible fiction nonfiction grammar-examples                                                                               |
| **contact**         | <leonel.de.alencar@ufc.br>                                                                                                     |
| **sentences**       | 2839                                                                                                                           |
| **tokens**          | 26444                                                                                                                          |

**Issue draft:** [UD_Nheengatu-CompLin](../issue_drafts/UD_Nheengatu-CompLin.html)

## Modality identification

**Is spoken part clearly identifiable?** No - almost every sentence carries a written-source citation, so presence/absence of a source field doesn't discriminate spoken vs. written. Of 2,839 sentences, 2,827 have at least one `text_*source` field (citing grammars, dictionaries, or Bible translations by page/verse). All sampled source values are published written works (Amorim, Rodrigues, Stradelli, bible.com) - flagged to maintainers to confirm whether any sentences actually originate from spoken/elicited fieldwork.

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

(none found)

### transcription and annotation levels available

(none found)

### speaker metadata

(none found)

### doc (and paragraphs) metadata

(none found)

### modality metadata

(none found)

### sent metadata

(none found)

### varia (all corpus specific)

(none found)

### token-level metadata (MISC)

| Field                  | Advice                                         |
| ---------------------- | ---------------------------------------------- |
| `TokenRange`           | keep (corpus-specific)                         |
| `SpaceAfter`           | n/a (standard UD feature, not spoken-specific) |
| `ModernForm`           | keep (corpus-specific)                         |
| `OrigLang`             | rename to `OrigLang`                           |
| `CorrectForm`          | n/a (standard UD feature, not spoken-specific) |
| `ModernPerson`         | keep (corpus-specific)                         |
| `ModernVerbForm`       | keep (corpus-specific)                         |
| `ModernMood`           | keep (corpus-specific)                         |
| `ModernLemma`          | keep (corpus-specific)                         |
| `Orig`                 | keep (corpus-specific)                         |
| `ModernCase`           | keep (corpus-specific)                         |
| `CorrectSpaceAfter`    | keep (corpus-specific)                         |
| `ModernNumber`         | keep (corpus-specific)                         |
| `ModernRel`            | keep (corpus-specific)                         |
| `StandardForm`         | keep (corpus-specific)                         |
| `StandardPerson`       | keep (corpus-specific)                         |
| `StandardMood`         | keep (corpus-specific)                         |
| `ModernSpaceAfter`     | keep (corpus-specific)                         |
| `StandardNumber`       | keep (corpus-specific)                         |
| `StandardVerbForm`     | keep (corpus-specific)                         |
| `Alomorph`             | keep (corpus-specific)                         |
| `ModernNumber[psor]`   | keep (corpus-specific)                         |
| `ModernPerson[psor]`   | keep (corpus-specific)                         |
| `LDeriv`               | keep (corpus-specific)                         |
| `StandardRel`          | keep (corpus-specific)                         |
| `ModernAdvType`        | keep (corpus-specific)                         |
| `MGloss`               | keep (corpus-specific)                         |
| `MSeg`                 | keep (corpus-specific)                         |
| `ModernNumber[Grnd]`   | keep (corpus-specific)                         |
| `ModernPerson[Grnd]`   | keep (corpus-specific)                         |
| `StandardSpaceAfter`   | keep (corpus-specific)                         |
| `CorrectLemma`         | keep (corpus-specific)                         |
| `VerbForm`             | keep (corpus-specific)                         |
| `StandardNumber[Grnd]` | keep (corpus-specific)                         |
| `StandardPerson[Grnd]` | keep (corpus-specific)                         |
| `ModeTokenRange`       | keep (corpus-specific)                         |
| `ModernNumber[Psor]`   | keep (corpus-specific)                         |
| `ModernPerson[Psor]`   | keep (corpus-specific)                         |
| `StandardCase`         | keep (corpus-specific)                         |
| `StandardLemma`        | keep (corpus-specific)                         |
| `ModernStyle`          | keep (corpus-specific)                         |
| `TokeFnRange`          | keep (corpus-specific)                         |

### additional fields found by clone verification (2026-07-30)

| Field                            | Advice                                                                                   |
| -------------------------------- | ---------------------------------------------------------------------------------------- |
| `text_eng`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_source`                    | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_annotator`                 | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `reviewer1`                      | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_eng_orig`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `phrase_structure`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `speaker`                        | possibly rename to `speaker_id` (see Speaker-level in metadata.html) - please verify     |
| `reviewer2`                      | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `title`                          | possibly rename to `newdoc id` (see Document-level in metadata.html) - please verify     |
| `title_eng`                      | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `title_por`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_alt`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_alt`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_alt_source`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_prim`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_prim`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_prim_transcriber`          | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_prim_modernizer`       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_prim_source`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_prim_source`           | corpus-specific (sentence-level) - verify against metadata.html                          |
| `inputline`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `cross_reference`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_source_orig`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_orig`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_prim_transcription`        | corpus-specific (sentence-level) - verify against metadata.html                          |
| `reviewer3`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_alt1`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_alt2`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_prim_transcriber`      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `acknowledgement`                | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `previous`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `next`                           | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_ggl`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_transcriber`          | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_prim_gloss`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_gloss`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_adapt`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_gll`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_orig_transcriber`      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_prim_gloss_modernizer` | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_rus`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_rus_source`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_prim_por`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_prim_por_source`           | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_alt`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_alt_source`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_alt_source`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_pos`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_sec`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_sec_source`                | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_sec`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_sec_source`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_source`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `tex_por_alt`                    | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_source`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `alt_id`                         | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_source_url`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_alt`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_orig_alt`              | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_source_alt`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `title_orig`                     | corpus-specific (sentence-level) - verify against metadata.html                          |
| `place`                          | corpus-specific (sentence-level) - verify against metadata.html                          |
| `date`                           | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_translator`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_lit`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_por`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_context`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `place_orig_por`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `narrator`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `ethnicity`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_translator`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_sec_alt`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `title_por_orig`                 | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_modernizer`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_orig_sec`              | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_orig_sec_source`       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_adapt`                     | corpus-specific (sentence-level) - verify against metadata.html                          |
| `review_status`                  | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `place_por`                      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `title_number`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `title_por_gloss`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `variant_number`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `alt_id_error`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_gloss`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `place_orig`                     | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_corr`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `cross_reference1`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `cross_reference2`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `spelling_adaptation`            | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_eng_man`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_eng_man_translator`        | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_orig_source`           | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_alt_translator`        | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_sec_translator`        | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_gloss_modernizer`      | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_por_source_adapt`          | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_transcriber`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_sec_alt`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_sec_alt_source`        | corpus-specific (sentence-level) - verify against metadata.html                          |
| `sent_number_orig`               | corpus-specific (sentence-level) - verify against metadata.html                          |
| `people`                         | corpus-specific (sentence-level) - verify against metadata.html                          |
| `note_por`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_transcriber`           | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `subtitle_orig`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `note`                           | corpus-specific (sentence-level) - verify against metadata.html                          |
| `note_source`                    | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_adapt_source`              | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_sec_alt_source`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_part1`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_part2`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_part2_modernizer`      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_part1_translator`      | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_modern`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `title_orig_alt`                 | corpus-specific (sentence-level) - verify against metadata.html                          |
| `title_por_alt`                  | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_sec_pos`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_var`                       | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_adapter`                   | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_adapt_reviewer`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `speaker_gender`                 | possibly rename to `speaker_gender` (see Speaker-level in metadata.html) - please verify |
| `text_modernizer`                | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `comment`                        | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_orig_alt_place`            | corpus-specific (sentence-level) - verify against metadata.html                          |
| `ethnicity_orig`                 | corpus-specific (speaker/paragraph-level) - verify against metadata.html                 |
| `text_orig_total`                | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_por_sec_corr`              | corpus-specific (sentence-level) - verify against metadata.html                          |
| `chapter_title_por`              | corpus-specific (sentence-level) - verify against metadata.html                          |
| `text_author`                    | corpus-specific (sentence-level) - verify against metadata.html                          |

## Things to check manually

- Confirm whether any sentences originate from spoken/elicited fieldwork rather than the cited written sources, and if so how they're distinguished in the source data.
- **token-level metadata (MISC):** `OrigLang` → rename to `OrigLang`
- **additional fields found by clone verification (2026-07-30):** `text_eng` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_annotator` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `reviewer1` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `phrase_structure` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `speaker` → possibly rename to `speaker_id` (see Speaker-level in metadata.html) - please verify
- **additional fields found by clone verification (2026-07-30):** `reviewer2` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title` → possibly rename to `newdoc id` (see Document-level in metadata.html) - please verify
- **additional fields found by clone verification (2026-07-30):** `title_eng` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_alt_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_prim` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_prim` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_prim_transcriber` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_prim_modernizer` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_prim_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_prim_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `inputline` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `cross_reference` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_source_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_prim_transcription` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `reviewer3` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_alt1` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_alt2` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_prim_transcriber` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `acknowledgement` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `previous` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `next` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_ggl` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_transcriber` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_prim_gloss` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_gloss` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_adapt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_gll` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_orig_transcriber` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_prim_gloss_modernizer` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_rus` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_rus_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_prim_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_prim_por_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_alt_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_alt_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_pos` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_sec` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_sec_source` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_sec` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_sec_source` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `tex_por_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `alt_id` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_source_url` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_orig_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_source_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `place` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `date` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_translator` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_lit` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_context` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `place_orig_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `narrator` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `ethnicity` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_translator` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_sec_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_por_orig` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_modernizer` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_orig_sec` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_orig_sec_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_adapt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `review_status` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `place_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_number` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_por_gloss` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `variant_number` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `alt_id_error` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_gloss` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `place_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_corr` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `cross_reference1` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `cross_reference2` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `spelling_adaptation` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_man` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_eng_man_translator` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_orig_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_alt_translator` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_sec_translator` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_gloss_modernizer` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_source_adapt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_transcriber` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_sec_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_sec_alt_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `sent_number_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `people` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `note_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_transcriber` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `subtitle_orig` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `note` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `note_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_adapt_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_sec_alt_source` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_part1` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_part2` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_part2_modernizer` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_part1_translator` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_modern` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_orig_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `title_por_alt` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_sec_pos` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_var` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_adapter` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_adapt_reviewer` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `speaker_gender` → possibly rename to `speaker_gender` (see Speaker-level in metadata.html) - please verify
- **additional fields found by clone verification (2026-07-30):** `text_modernizer` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `comment` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_alt_place` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `ethnicity_orig` → corpus-specific (speaker/paragraph-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_orig_total` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_por_sec_corr` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `chapter_title_por` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_author` → corpus-specific (sentence-level) - verify against metadata.html
