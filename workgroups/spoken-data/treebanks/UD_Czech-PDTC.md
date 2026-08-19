---
layout: base
title: 'Czech PDTC'
udver: '2'
---

# Czech PDTC

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | mixed |
| **available since** | 1.0 |
| **link** | [https://github.com/UniversalDependencies/UD_Czech-PDTC](https://github.com/UniversalDependencies/UD_Czech-PDTC) |
| **genre** | news reviews nonfiction academic spoken social |
| **contact** | zeman@ufal.mff.cuni.cz |
| **sentences** | 213897 |
| **tokens** | 3432078 |

**Issue draft:** [UD_Czech-PDTC](../issue_drafts/UD_Czech-PDTC.html)

## Modality identification

**Is spoken part clearly identifiable?** yes - via the `newdoc id` prefix `pdtsc` (not "sentences starting with `s`" as mentioned in the README. The actual `newdoc id`/`sent_id` values spell it out in full, e.g. `pdtsc_jg-27638_04.00`).

**Advise:** add `# modality = spoken` to the 1553 sentences (documents) with `newdoc id` starting `pdtsc`, and `# modality = written` to the rest.