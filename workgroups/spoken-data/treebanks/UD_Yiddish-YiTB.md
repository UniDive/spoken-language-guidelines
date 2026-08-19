---
layout: base
title: 'Yiddish YiTB'
udver: '2'
---

# Yiddish YiTB

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                |
| **available since** | 2.17                                                                                                                 |
| **link**            | [https://github.com/UniversalDependencies/UD_Yiddish-YiTB](https://github.com/UniversalDependencies/UD_Yiddish-YiTB) |
| **genre**           | grammar-examples learner-essays bible wiki fiction nonfiction spoken web                                             |
| **contributors**         | Andrews, Kirk |
| **sentences**       | 3113                                                                                                                 |
| **tokens**          | 27954                                                                                                                |

**Issue draft:** [UD_Yiddish-YiTB](../issue_drafts/UD_Yiddish-YiTB.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - via the sentence-level `genre` field. `genre` (9 distinct values): `grammar-examples/learner-essays` (2,437), `spoken, web` (160), `nonfiction` (126), `bible` (126), `fiction` (120), `proverb` (60), `wiki` (19), `spoken, liturgical` (5), `grammar-examples` (1). 165 sentences have a `genre` value containing "spoken".

### modality metadata

_(none found)_ - add `# modality = spoken` to the 165 sentences whose `genre` value contains "spoken" (`spoken, web` / `spoken, liturgical`).

### speaker metadata

| Field | Advice |
| --- | --- |
| `rtl` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `source` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |

### additional fields found by clone verification (2026-07-30)

| Field      | Advice                            |
| ---------- | --------------------------------- |
| `translit` | rename to `text_translitteration` |
| `text_en`  | rename to `text_eng` (ISO 639-3)  |
| `note` | corpus-specific (sentence-level) - verify against metadata.html |
