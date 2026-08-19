---
layout: base
title: 'Skolt_Sami Giellagas'
udver: '2'
---

# Skolt_Sami Giellagas

[Back to index](../ud_spoken_treebanks.html)

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

### languages and translation(s)

| Field     | Advice                           |
| --------- | -------------------------------- |
| `text_fi` | rename to `text_fin` (ISO 639-3) |
| `text_en` | rename to `text_eng` (ISO 639-3) |

### doc (and paragraphs) metadata

 no `document_id` exists, but it can be derived from the source-identifier prefix of `sent_id` (the part before the timestamp/counter suffix), e.g. `11308_1a` and `NA2_00635_1az` (recordings), `kotus-skak2010-1-1` (published transcription), `SK2020`, `SKKV2020`, `Juutinen2023`, `FofonoffHilkka_brat_2018` (other sources). The exact delimiter varies by source (`::` before timestamps, `:`/`-` before a numeric counter otherwise) - please confirm the intended document granularity with the maintainer.

| Field | Advice                                                           |
| ----- | ---------------------------------------------------------------- |
| —     | derive `# document_id` from the `sent_id` source-identifier prefix |

### modality metadata

 add `# modality = written` to `sms_giellagas-ud-train.conllu` sentences and `# modality = spoken` to `sms_giellagas-ud-test.conllu` sentences (see Modality identification above).

### additional fields

`aannotation` (likely a typo for "annotation") packs three XML-style attributes into one comment line: `# aannotation="yes" begintime="0:39:13" endtime="0:09:18"` (`endtime` is sometimes empty). We suggest splitting these into the standard sentence-level timing fields; `sound_alignment_begin`/`sound_alignment_end` are specified in milliseconds, so `begintime`/`endtime` (currently `H:MM:SS`) need converting, not just copying.

| Field                       | Advice                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aannotation` (`begintime`) | convert `H:MM:SS` to milliseconds, split into `sound_alignment_begin`                                                                             |
| `aannotation` (`endtime`)   | convert `H:MM:SS` to milliseconds, split into `sound_alignment_end` (when present); derive `duration` (ms) from begin/end when both are available |
| `text_olo`                  | unsure                                                                                                                                            |
| `text_mdf`                  | unsure                                                                                                                                            |
