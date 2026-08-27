---
layout: base
title: 'Beja Autogramm'
udver: '2'
---

# Beja Autogramm

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.8 |
| **link** | [https://github.com/UniversalDependencies/UD_Beja-Autogramm](https://github.com/UniversalDependencies/UD_Beja-Autogramm) |
| **genre** | spoken |
| **contributors** | Vanhove, Martine; Ziane, Rayan; Kahane, Sylvain; Guillaume, Bruno |
| **sentences** | 763 |
| **tokens** | 11948 |

**Issue draft:** [UD_Beja-Autogramm](../issue_drafts/UD_Beja-Autogramm.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A - spoken data only

## Metadata review

### doc (and paragraphs) metadata

| Field | Advice |
| --- | --- |
| — | no `document_id` exists at all (0 occurrences across 763 sentences) - but the 18 distinct `sound_url` values (one per recording, e.g. `BEJ_MV_NARR_01_SHELTER.WAV`) already identify document boundaries; derive `# document_id` from the recording basename and set it once per document, then move `sound_url` there too |

### languages and translation(s)

| Field | Advice |
|---|---|
| `text_en` | OK (ISO 639-1 two-letter code) |

### transcription and annotation levels available

| Field | Advice |
|---|---|
| `phonetic_text` | change to `text_phonetic` |

### speaker metadata

| Field | Advice |
|---|---|
| `speaker_id` | OK |

### sent metadata

| Field           | Advice |
| --------------- | ------ |
| `sent_timecode` | change to `sound_alignment_begin`, `sound_alignment_end` and `duration`   |
| `sound_url` | move to document level |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

