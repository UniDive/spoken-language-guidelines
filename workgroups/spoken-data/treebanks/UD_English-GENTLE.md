---
layout: base
title: 'English GENTLE'
udver: '2'
---

# English GENTLE

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | mixed |
| **available since** | 2.12 |
| **link** | [https://github.com/UniversalDependencies/UD_English-GENTLE](https://github.com/UniversalDependencies/UD_English-GENTLE) |
| **genre** | academic grammar-examples legal medical nonfiction poetry social spoken |
| **contributors** | Aoyama, Tatsuya; Behzad, Shabnam; Gessler, Luke; Levine, Lauren; Lin, Yi-Ju Jessica; Liu, Yang Janet; Peng, Siyao Logan; Zhu, Yilun; Zeldes, Amir |
| **sentences** | 1334 |
| **tokens** | 17619 |

**Issue draft:** [UD_English-GENTLE](../issue_drafts/UD_English-GENTLE.html)

## Modality identification

**Is spoken part clearly identifiable?** yes - via `meta::genre = esports`. Exactly 2 of 26 documents: `GENTLE_esports_fifa` ("CHAMPIONS LEAGUE SEMI-FINAL!!! FIFA 20 AC MILAN CAREER MODE #16") and `GENTLE_esports_fortnite` ("WORLD CUP SOLO'S FINAL MATCH | Fortnite World Cup Game 6 | Live commentary"), both sourced from YouTube live-commentary videos.

**Advise:** add `# modality = spoken` to `GENTLE_esports_fifa` and `GENTLE_esports_fortnite`, and `# modality = written` to the rest, per the [Document-level metadata conventions](../metadata.html#document-level).

## Metadata review

### speaker metadata

| Field | Advice |
|---|---|
| `speaker` | change to `speaker_id` |

### doc (and paragraphs) metadata

| Field | Advice |
|---|---|
| `document_id` | OK |

### modality metadata

| Field | Advice |
|---|---|
| `meta::genre` | consider switching to `genre` |
