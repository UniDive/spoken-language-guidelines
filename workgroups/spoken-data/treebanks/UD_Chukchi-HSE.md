---
layout: base
title: 'Chukchi HSE'
udver: '2'
---

# Chukchi HSE

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | only spoken |
| **available since** | 2.7 |
| **link** | [https://github.com/UniversalDependencies/UD_Chukchi-HSE](https://github.com/UniversalDependencies/UD_Chukchi-HSE) |
| **genre** | spoken |
| **contributors** | Tyers, Francis; Mischenkova, Karina |
| **sentences** | 1004 |
| **tokens** | 5389 |

**Issue draft:** [UD_Chukchi-HSE](../issue_drafts/UD_Chukchi-HSE.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A - spoken data only

## Metadata review

### doc (and paragraphs) metadata

No `# document_id` exists, but document boundaries are fully recoverable: the README documents that `sent_id` encodes `<filename>:<sentence_number>`, where `<filename>` matches the text's name on the source corpus site ([chuklang.ru](http://chuklang.ru/)). Splitting `sent_id` on `:` gives 65 distinct document prefixes (e.g. `Abramovich`, `GUM`, `Katyusha`) across the 1004 sentences.

| Field | Advice |
|---|---|
| — | derive `# document_id` from the `sent_id` prefix (everything before `:`), set once at each document's first sentence |

### languages and translation(s)

| Field | Advice |
|---|---|
| `text[eng]` | change to `text_en` |
| `text[eng']` | change to `text_en_literal` |
| `text[rus]` | change to `text_ru` |

### transcription and annotation levels available

| Field | Advice |
|---|---|
| `text[phon]` | change to `text_phonetic` |

### sent metadata

| Field | Advice |
|---|---|
| `timestamp` | change to `sound_alignment_begin`, `sound_alignment_end` and `duration` (only 8 sentences carry this field) |

