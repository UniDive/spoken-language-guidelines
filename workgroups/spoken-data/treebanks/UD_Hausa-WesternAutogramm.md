---
layout: base
title: 'Hausa WesternAutogramm'
udver: '2'
---

# Hausa WesternAutogramm

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                                    |
| **available since** | 2.17                                                                                                                                     |
| **link**            | [https://github.com/UniversalDependencies/UD_Hausa-WesternAutogramm](https://github.com/UniversalDependencies/UD_Hausa-WesternAutogramm) |
| **genre**           | fiction nonfiction spoken                                                                                                                |
| **contributors**         | Caron, Bernard |
| **sentences**       | 775                                                                                                                                      |
| **tokens**          | 13862                                                                                                                                    |

**Issue draft:** [UD_Hausa-WesternAutogramm](../issue_drafts/UD_Hausa-WesternAutogramm.html)

## Modality identification

**Is spoken part clearly identifiable?** No - no genre-like field or `document_id` found at all; no comment-level metadata beyond `sent_id`/`text` detected. Flagged to maintainers to confirm which sentences/documents are spoken vs. written.

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
