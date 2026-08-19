---
layout: base
title: 'Ika ChibErgIS'
udver: '2'
---

# Ika ChibErgIS

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                            |
| **available since** | 2.16                                                                                                                   |
| **link**            | [https://github.com/UniversalDependencies/UD_Ika-ChibErgIS](https://github.com/UniversalDependencies/UD_Ika-ChibErgIS) |
| **genre**           | spoken                                                                                                                 |
| **contact**         | <jana.bajorat@hu-berlin.de>                                                                                            |
| **sentences**       | 628                                                                                                                    |
| **tokens**          | 5307                                                                                                                   |

**Issue draft:** [UD_Ika-ChibErgIS](../issue_drafts/UD_Ika-ChibErgIS.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

| Field       | Advice                          |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |

### languages and translation(s)

| Field                | Advice               |
| -------------------- | -------------------- |
| `text_en`            | change to `text_eng` |
| `text_phrase-gls-es` | change to `text_esp` |

### transcription and annotation levels available

| Field                | Advice                                                                    |
| -------------------- | ------------------------------------------------------------------------- |
| `morphemic_text`     | change to `text_morphemic`                                                |
| `sent_timecode`      | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |
| `text_phrase-gls-tl` | not sure what this is                                                     |

### speaker metadata

| Field        | Advice |
| ------------ | ------ |
| `speaker_id` | OK     |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |
