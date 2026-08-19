---
layout: base
title: 'Hausa NorthernAutogramm'
udver: '2'
---

# Hausa NorthernAutogramm

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | only spoken                                                                                                                                |
| **available since** | 2.14                                                                                                                                       |
| **link**            | [https://github.com/UniversalDependencies/UD_Hausa-NorthernAutogramm](https://github.com/UniversalDependencies/UD_Hausa-NorthernAutogramm) |
| **genre**           | spoken                                                                                                                                     |
| **contact**         | <bernard.l.caron@gmail.com>                                                                                                                |
| **sentences**       | 1305                                                                                                                                       |
| **tokens**          | 15324                                                                                                                                      |

**Issue draft:** [UD_Hausa-NorthernAutogramm](../issue_drafts/UD_Hausa-NorthernAutogramm.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A - spoken data only

## Metadata review

### languages and translation(s)

| Field     | Advice               |
| --------- | -------------------- |
| `text_en` | change to `text_eng` |

### transcription and annotation levels available

| Field        | Advice                        |
| ------------ | ----------------------------- |
| `text_ortho` | change to `text_orthographic` |

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
