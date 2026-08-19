---
layout: base
title: 'Hebrew IAHLTknesset'
udver: '2'
---

# Hebrew IAHLTknesset

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                              |
| **available since** | 2.15                                                                                                                               |
| **link**            | [https://github.com/UniversalDependencies/UD_Hebrew-IAHLTknesset](https://github.com/UniversalDependencies/UD_Hebrew-IAHLTknesset) |
| **genre**           | government spoken                                                                                                                  |
| **contact**         | <amir.zeldes@georgetown.edu>                                                                                                       |
| **sentences**       | 2883                                                                                                                               |
| **tokens**          | 50499                                                                                                                              |

**Issue draft:** [UD_Hebrew-IAHLTknesset](../issue_drafts/UD_Hebrew-IAHLTknesset.html)

## Modality identification

**Is spoken part clearly identifiable?** The entire treebank may already be spoken (transcribed Knesset/parliament proceedings), rather than a partial split. `newdoc id` values follow `<year>_<doctype>_<id>` where `doctype` is only ever `ptv` (65 docs, likely "protocol verbatim") or `ptm` (35 docs, likely "protocol minutes") - both are transcribed parliamentary speech, not a spoken/written split. Rather than partially tagging, please confirm whether the whole corpus should carry `# modality = spoken`, or whether `ptm` (minutes, possibly edited/summarized) should be excluded as not verbatim spoken language.

## Metadata review

### doc (and paragraphs) metadata

| Field | Advice |
| --- | --- |
| `newdoc id` | OK - already standard |

### speaker metadata

| Field     | Advice                 |
| --------- | ---------------------- |
| `speaker` | change to `speaker_id` |
