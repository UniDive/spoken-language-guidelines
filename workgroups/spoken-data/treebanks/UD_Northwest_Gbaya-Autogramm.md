---
layout: base
title: 'Northwest_Gbaya Autogramm'
udver: '2'
---

# Northwest_Gbaya Autogramm

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                                    |
| **available since** | 2.15                                                                                                                                           |
| **link**            | [https://github.com/UniversalDependencies/UD_Northwest_Gbaya-Autogramm](https://github.com/UniversalDependencies/UD_Northwest_Gbaya-Autogramm) |
| **genre**           | spoken                                                                                                                                         |
| **contact**         | <pauletteroulon@gmail.com>                                                                                                                     |
| **sentences**       | 403                                                                                                                                            |
| **tokens**          | 2692                                                                                                                                           |

**Issue draft:** [UD_Northwest_Gbaya-Autogramm](../issue_drafts/UD_Northwest_Gbaya-Autogramm.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

| Field     | Advice               |
| --------- | -------------------- |
| `text_fr` | change to `text_fra` |

### transcription and annotation levels available

| Field           | Advice                    |
| --------------- | ------------------------- |
| `phonetic_text` | change to `text_phonetic` |

### speaker metadata

| Field        | Advice |
| ------------ | ------ |
| `speaker_id` | OK     |

### sent metadata

| Field           | Advice                                                                    |
| --------------- | ------------------------------------------------------------------------- |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |
| `sound_url`     | possibly move to document level                                           |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |
