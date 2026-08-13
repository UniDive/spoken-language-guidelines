---
layout: base
title: 'French Rhapsodie'
udver: '2'
---

# French Rhapsodie

[Back to index](ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                                  |
| **available since** | 2.2                                                                                                                          |
| **link**            | [https://github.com/UniversalDependencies/UD_French-Rhapsodie](https://github.com/UniversalDependencies/UD_French-Rhapsodie) |
| **genre**           | spoken                                                                                                                       |
| **contact**         | <kim@gerdes.fr>                                                                                                              |
| **sentences**       | 3209                                                                                                                         |
| **tokens**          | 43691                                                                                                                        |

**Issue draft:** [UD_French-Rhapsodie](../issue_drafts/UD_French-Rhapsodie.html)

## Modality identification

**Is spoken part clearly identifiable?** N/A

## Metadata review

### doc (and paragraphs) metadata

_(none found)_ - no `newdoc id` exists at all. But `sent_id` already encodes it: e.g. `Rhap_D0001-1` is document `Rhap_D0001`, sentence `1`. 57 distinct documents across 3209 sentences, matching exactly the 57 distinct `sound_url` values (present on every single sentence, unlike ParisStories). Several other fields are also constant within each document and should move to document level once `newdoc id` exists: `genre`, `subgenre`, `type`, `task`, `subject`, `channel`, `modalities` (verified: none of these vary within a document). `speaker_id`/`speaker_age` correctly stay sentence-level, since they do vary within documents (multi-speaker dialogues).

| Field                                                                   | Advice                                                                                      |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| —                                                                       | derive `# newdoc id` from the `sent_id` prefix (everything before the trailing `-<number>`) |
| `sound_url`                                                             | move to document level, set once per `newdoc id`                                            |
| `genre`, `subgenre`, `type`, `task`, `subject`, `channel`, `modalities` | move to document level (constant per document)                                              |

### transcription and annotation levels available

| Field         | Advice                       |
| ------------- | ---------------------------- |
| `macrosyntax` | change to `text_macrosyntax` |
| `prosodic_annotation` | corpus-specific (only on a subset of sentences) - please confirm what this represents |

### speaker metadata

| Field        | Advice |
| ------------ | ------ |
| `speaker_id` | OK     |
| `speaker` | corpus-specific turn-position label (`L1`, `L2`, ...), distinct from and redundant with `speaker_id` (e.g. `§LF30`) - keep, `speaker_id` is already standard |

### token-level metadata (MISC)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |
