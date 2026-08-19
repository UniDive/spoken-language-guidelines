---
layout: base
title: 'Ukrainian ParlaMint'
udver: '2'
---

# Ukrainian ParlaMint

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                              |
| **available since** | 2.15                                                                                                                               |
| **link**            | [https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint](https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint) |
| **genre**           | government legal spoken                                                                                                            |
| **contact**         | <corpus.textiv@gmail.com>                                                                                                          |
| **sentences**       | 7142                                                                                                                               |
| **tokens**          | 109166                                                                                                                             |

**Issue draft:** [UD_Ukrainian-ParlaMint](../issue_drafts/UD_Ukrainian-ParlaMint.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - the entire corpus should be `# modality = spoken`. The README describes it as "Ukrainian parliamentary plenary session transcripts" drawn from ParlaMint-UA and other open sources (NSDC); there's no written material.

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

(none found)

### transcription and annotation levels available

(none found)

### speaker metadata

(none found)

### doc (and paragraphs) metadata

`document_id` already exists for the ParlaMint-sourced sentences (one per utterance, e.g. `ParlaMint-UA_2022-01-25-m0.u100`), but is entirely missing for the 502 sentences sourced from NSDC (`sent_id` like `NSDC_UA_28_Feb2014-1`). These can easily get a `document_id` too, derived from the `sent_id` prefix (everything before the trailing `-<number>`) - all 502 collapse to a single document, `NSDC_UA_28_Feb2014`.

| Field | Advice                                                                                                                      |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |
| —     | derive `# document_id = NSDC_UA_28_Feb2014` for the NSDC-sourced sentences (`sent_id` prefix before the trailing `-<number>`) |

### sent metadata

`text_en` and `phonetic_text` each appear exactly once across the entire corpus, both with the literal placeholder value `undefined undefined` - leftover template artifacts rather than real content.

| Field           | Advice |
| --------------- | ------ |
| `text_en`       | remove (single occurrence, placeholder value `undefined undefined`) |
| `phonetic_text` | remove (single occurrence, placeholder value `undefined undefined`) |
| `WARNING`       | corpus-specific (sentence-level, parser-diagnostic comments e.g. dependency-cycle warnings) - verify against metadata.html |

### token-level metadata (MISC)

| Field | Advice |
| --- | --- |
| `lang` | rename to `Lang` |
