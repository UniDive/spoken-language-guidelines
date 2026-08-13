---
layout: base
title: 'Bokota ChibErgIS'
udver: '2'
---

# Bokota ChibErgIS

[Back to index](ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.16 |
| **link** | [https://github.com/UniversalDependencies/UD_Bokota-ChibErgIS](https://github.com/UniversalDependencies/UD_Bokota-ChibErgIS) |
| **genre** | spoken |
| **contact** | marie.benzerrak@laposte.net |
| **sentences** | 406 |
| **tokens** | 2713 |

**Issue draft:** [UD_Bokota-ChibErgIS](../issue_drafts/UD_Bokota-ChibErgIS.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A

## Metadata review



### languages and translation(s)

| Field | Advice |
|---|---|
| `text_en` | change to `text_eng` |

### transcription and annotation levels available

| Field | Advice |
|---|---|
| `text_ortho` | change to `text_orthographic` |
| `morphemic_text` | change to `text_morphemic` |

### speaker metadata

| Field | Advice |
|---|---|
| `speaker_id` | OK |

### doc (and paragraphs) metadata

| Field | Advice |
|---|---|
| — | no `newdoc id` exists at all (0 occurrences across 406 sentences) - but the 54 distinct `sound_url` values (e.g. `SAB-TXT-AN-00000-01.WAV`) already identify document boundaries; derive `# newdoc id` from the recording basename and set it once per document |
| `sound_url` | currently repeated on every sentence - move to document level once `newdoc id` exists |

### sent metadata

| Field | Advice |
|---|---|
| `sent_timecode` | change to `sound_alignment_begin`, `sound_alignment_end` and `duration` |


### token-level metadata (MISC)

| Field | Advice |
|---|---|
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd` | rename to `WordAlignmentEnd` |
