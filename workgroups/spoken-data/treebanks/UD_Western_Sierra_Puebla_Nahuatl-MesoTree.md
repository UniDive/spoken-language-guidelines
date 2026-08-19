---
layout: base
title: 'Western_Sierra_Puebla_Nahuatl MesoTree'
udver: '2'
---

# Western_Sierra_Puebla_Nahuatl MesoTree

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **type**            | mixed                                                                                                                                                                    |
| **available since** | 2.11                                                                                                                                                                     |
| **link**            | [https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-MesoTree](https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-MesoTree) |
| **genre**           | spoken fiction grammar-examples nonfiction                                                                                                                               |
| **contact**         | <pughrob@iu.edu>                                                                                                                                                         |
| **sentences**       | 3024                                                                                                                                                                     |
| **tokens**          | 19191                                                                                                                                                                    |

**Issue draft:** [UD_Western_Sierra_Puebla_Nahuatl-MesoTree](../issue_drafts/UD_Western_Sierra_Puebla_Nahuatl-MesoTree.html)

## Modality identification

**Is spoken part clearly identifiable?** No - the only `genre`-like field has a single constant value (`examples`, 2,115 sentences); no `document_id` or other field was found either. Flagged to maintainers to confirm which documents (if any) are transcribed spoken material.

## Metadata review

### languages and translation(s)

| Field         | Advice                     |
| ------------- | -------------------------- |
| `text[spa]`   | change to `text_spa`       |
| `text[orig]`  | change to `text_original`  |
| `text[morf]` | change to `text_morphemic` |
| `text[eng]`   | change to `text_eng`       |
| `text[gloss]` | change to `text_glossing`  |

### speaker metadata

| Field | Advice |
| --- | --- |
| `user_id` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `finished` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `location` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `orthography` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |

### sent metadata

| Field | Advice |
| --- | --- |
| `timestamp` | possibly rename to `sound_alignment_begin` / `sound_alignment_end` - please verify |
| `hash` | corpus-specific (sentence-level) - verify against metadata.html |
| `alimg` | corpus-specific (sentence-level) - verify against metadata.html |
| `locale` | corpus-specific (sentence-level) - verify against metadata.html |
| `text[orig_omitlan]` | corpus-specific (sentence-level) - verify against metadata.html |
| `text[orig_smt]` | corpus-specific (sentence-level) - verify against metadata.html |
| `label` | corpus-specific (sentence-level) - verify against metadata.html |
| `note` | corpus-specific (sentence-level) - verify against metadata.html |
