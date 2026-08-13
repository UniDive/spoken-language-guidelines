---
layout: base
title: 'Skolt_Sami Giellagas'
udver: '2'
---

# Skolt_Sami Giellagas

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | mixed                                                                                                                                |
| **available since** | 2.5                                                                                                                                  |
| **link**            | [https://github.com/UniversalDependencies/UD_Skolt_Sami-Giellagas](https://github.com/UniversalDependencies/UD_Skolt_Sami-Giellagas) |
| **genre**           | nonfiction news spoken                                                                                                               |
| **contact**         | <rueter.jack@gmail.com>                                                                                                              |
| **sentences**       | 261                                                                                                                                  |
| **tokens**          | 3049                                                                                                                                 |

**Issue draft:** [UD_Skolt_Sami-Giellagas](../issue_drafts/UD_Skolt_Sami-Giellagas.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - it aligns exactly with the file split. Per the README, the corpus "originally consists of twenty translated sentences ... made by Hilkka Fofonoff from the Finnish texts", with all subsequent sentences from the Giellagas Corpus of Spoken Saami Languages. Confirmed in the data: `sms_giellagas-ud-train.conllu` contains exactly those 20 sentences (`sent_id` prefix `FofonoffHilkka_brat_2018`) - written, translated from Finnish. `sms_giellagas-ud-test.conllu` contains the remaining 241 sentences - spoken, drawn from field recordings (`sent_id` prefixes like `11308_1a::<timestamp>`, `NA2_00635_1az::<timestamp>`) and published transcriptions of recorded speech (`kotus-skak2010-*`). Note: a handful of `test` sentences (`SK2020-*`, `SKKV2020:*`) seem grammar-book examples rather than recordings.

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

_(none found)_ - no `newdoc id` exists, but it can be derived from the source-identifier prefix of `sent_id` (the part before the timestamp/counter suffix), e.g. `11308_1a` and `NA2_00635_1az` (recordings), `kotus-skak2010-1-1` (published transcription), `SK2020`, `SKKV2020`, `Juutinen2023`, `FofonoffHilkka_brat_2018` (other sources). The exact delimiter varies by source (`::` before timestamps, `:`/`-` before a numeric counter otherwise) - please confirm the intended document granularity with the maintainer.

| Field | Advice                                                           |
| ----- | ---------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` source-identifier prefix |

### modality metadata

_(none found)_ - add `# modality = written` to `sms_giellagas-ud-train.conllu` sentences and `# modality = spoken` to `sms_giellagas-ud-test.conllu` sentences (see Modality identification above).

### sent metadata

(none found)

### varia (all corpus specific)

(none found)

### token-level metadata (MISC)

| Field         | Advice                                         |
| ------------- | ---------------------------------------------- |
| `GTtags`      | keep (corpus-specific)                         |
| `SpaceAfter`  | n/a (standard UD feature, not spoken-specific) |
| `CGdephead`   | keep (corpus-specific)                         |
| `CGdeprel`    | keep (corpus-specific)                         |
| `CorrectForm` | n/a (standard UD feature, not spoken-specific) |
| `Correctform` | n/a (standard UD feature, not spoken-specific) |

### additional fields found by clone verification (2026-07-30)

`aannotation` (likely a typo for "annotation") packs three XML-style attributes into one comment line: `# aannotation="yes" begintime="0:39:13" endtime="0:09:18"` (`endtime` is sometimes empty). We suggest splitting these into the standard sentence-level timing fields; `sound_alignment_begin`/`sound_alignment_end` are specified in milliseconds, so `begintime`/`endtime` (currently `H:MM:SS`) need converting, not just copying.

| Field                       | Advice                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aannotation` (`begintime`) | convert `H:MM:SS` to milliseconds, split into `sound_alignment_begin`                                                                             |
| `aannotation` (`endtime`)   | convert `H:MM:SS` to milliseconds, split into `sound_alignment_end` (when present); derive `duration` (ms) from begin/end when both are available |
| `text_fi`                   | rename to `text_fin` (ISO 639-3)                                                                                                                  |
| `story_id`                  | corpus-specific (sentence-level) - verify against metadata.html                                                                                   |
| `comment`                   | corpus-specific (sentence-level) - verify against metadata.html                                                                                   |
| `text_en`                   | rename to `text_eng` (ISO 639-3)                                                                                                                  |
| `-`                         | corpus-specific (sentence-level) - verify against metadata.html                                                                                   |
| `text_olo`                  | OK - Olonets/Livvi Karelian translation (`olo` is already the correct ISO 639-3 code); only present on the 20 written/translated sentences        |
| `text_mdf`                  | OK - Moksha translation (`mdf` is already the correct ISO 639-3 code); only present on the 20 written/translated sentences                        |

## Things to check manually

- **modality metadata:** confirm modality split by file (`train` = written, `test` = spoken); confirm whether `SK2020`/`SKKV2020` grammar-example sentences in `test` should count as spoken
- **doc (and paragraphs) metadata:** derive `# newdoc id` from the `sent_id` source-identifier prefix; confirm intended document granularity
- **additional fields found by clone verification (2026-07-30):** `aannotation` → split into `sound_alignment_begin`, `sound_alignment_end`, `duration`
- **additional fields found by clone verification (2026-07-30):** `text_fi` → rename to `text_fin`
- **additional fields found by clone verification (2026-07-30):** `text_en` → rename to `text_eng`
- **additional fields found by clone verification (2026-07-30):** `story_id` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `comment` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `-` → corpus-specific (sentence-level) - verify against metadata.html
- **additional fields found by clone verification (2026-07-30):** `text_olo` → OK, Olonets/Livvi Karelian translation, already ISO-compliant
- **additional fields found by clone verification (2026-07-30):** `text_mdf` → OK, Moksha translation, already ISO-compliant
