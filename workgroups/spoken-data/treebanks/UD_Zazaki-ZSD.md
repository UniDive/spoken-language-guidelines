---
layout: base
title: 'Zazaki ZSD'
udver: '2'
---

# Zazaki ZSD

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                      |
| **available since** | 2.17                                                                                                             |
| **link**            | [https://github.com/UniversalDependencies/UD_Zazaki-ZSD](https://github.com/UniversalDependencies/UD_Zazaki-ZSD) |
| **genre**           | spoken                                                                                                           |
| **contributors**         | Dogan, Mahîr; Talamo, Luigi; Vaz, Helena; Verkerk, Annemarie |
| **sentences**       | 200                                                                                                              |
| **tokens**          | 1371                                                                                                             |

**Issue draft:** [UD_Zazaki-ZSD](../issue_drafts/UD_Zazaki-ZSD.html)

## Modality identification

**Is spoken part clearly identifiable?** n/a

## Metadata review

(none found)

### doc (and paragraphs) metadata

_(none found)_ - no `document_id` exists, but it's trivial to derive: `sent_id` follows `Seyristane_dialogue_<number><A/B>` (e.g. `Seyristane_dialogue_171A`), and the whole corpus (200 sentences) seems a single interview/dialogue.

| Field | Advice                                                                |
| ----- | --------------------------------------------------------------------- |
| —     | add `# document_id = Seyristane_dialogue` corpus-wide (single document) |

| Field     | Advice                           |
| --------- | -------------------------------- |
| `text_en` | rename to `text_eng` (ISO 639-3) |
