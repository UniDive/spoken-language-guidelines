---
layout: base
title: 'Hausa SouthernAutogramm'
udver: '2'
---

# Hausa SouthernAutogramm

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | only spoken                                                                                                                                |
| **available since** | 2.14                                                                                                                                       |
| **link**            | [https://github.com/UniversalDependencies/UD_Hausa-SouthernAutogramm](https://github.com/UniversalDependencies/UD_Hausa-SouthernAutogramm) |
| **genre**           | spoken                                                                                                                                     |
| **contributors**         | Caron, Bernard |
| **sentences**       | 1927                                                                                                                                       |
| **tokens**          | 14398                                                                                                                                      |

**Issue draft:** [UD_Hausa-SouthernAutogramm](../issue_drafts/UD_Hausa-SouthernAutogramm.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

### languages and translation(s)

| Field     | Advice               |
| --------- | -------------------- |
| `text_en` | change to `text_eng` |

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
