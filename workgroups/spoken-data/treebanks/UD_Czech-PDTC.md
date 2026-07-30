---
layout: base
title: 'Czech PDTC'
udver: '2'
---

# Czech PDTC

[Back to index](ud_spoken_treebanks.html)

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

**Is spoken part clearly identifiable?** yes - via the `newdoc id` prefix `pdtsc` (not "sentences starting with `s`" as previously stated here - that was imprecise; `s` is a single-letter *source* code mentioned in the README, but the actual `newdoc id`/`sent_id` values spell it out in full, e.g. `pdtsc_jg-27638_04.00`).

*Re-checked directly against all 14 `.conllu` files (213897 sentences). `newdoc id` prefixes and counts: `ln` (2906), `wsj` (2312), `pdtsc` (1553), `mf` (1131), `lnd` (712), `cmpr` (372), `vesm` (209), `faust` (60). Per the README, `pdtsc` = Prague Dependency Treebank of Spoken Czech (transcribed spontaneous dialogs from the Malach and Companions projects) - the only spoken source; the rest are written (newspapers, magazines, the Wall Street Journal translation, and the Faust MT-testing corpus).*

**Advise:** add `# modality = spoken` to the 1553 sentences (documents) with `newdoc id` starting `pdtsc`, and `# modality = written` to the rest.