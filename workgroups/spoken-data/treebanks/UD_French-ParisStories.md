---
layout: base
title: 'French ParisStories'
udver: '2'
---

# French ParisStories

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                        |
| **available since** | 2.9                                                                                                                                |
| **link**            | [https://github.com/UniversalDependencies/UD_French-ParisStories](https://github.com/UniversalDependencies/UD_French-ParisStories) |
| **genre**           | spoken                                                                                                                             |
| **contributors**         | Gerdes, Kim; Kahane, Sylvain; Mahamdi, Menel |
| **sentences**       | 2776                                                                                                                               |
| **tokens**          | 42257                                                                                                                              |

**Issue draft:** [UD_French-ParisStories](../issue_drafts/UD_French-ParisStories.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A - spoken data only

## Metadata review

### doc (and paragraphs) metadata

_(none found)_ - no `document_id` exists at all. But `sent_id` already encodes it: e.g. `ParisStories_2020_maisonAbondonnee_1` is document `ParisStories_2020_maisonAbondonnee`, sentence `1`. 86 distinct documents across 2776 sentences. `sound_url` (currently repeated per sentence, present on 2749/2776 sentences - 27 sentences in one document lack it) should move to document level once `document_id` exists.

| Field       | Advice                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------- |
| —           | derive `# document_id` from the `sent_id` prefix (everything before the trailing `_<number>`) |
| `sound_url` | move to document level, set once per `document_id`                                            |

### transcription and annotation levels available

| Field         | Advice                                                                                  |
| ------------- | --------------------------------------------------------------------------------------- |
| `macrosyntax` | change to `text_macrosyntax`                                                            |
| `tags`        | corpus-specific (only 1 occurrence, value `TODO`) - please confirm what this represents |

### speaker metadata

| Field     | Advice                 |
| --------- | ---------------------- |
| `speaker` | change to `speaker_id` |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |
