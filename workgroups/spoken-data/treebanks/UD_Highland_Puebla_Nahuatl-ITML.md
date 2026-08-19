---
layout: base
title: 'Highland_Puebla_Nahuatl ITML'
udver: '2'
---

# Highland_Puebla_Nahuatl ITML

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **type**            | mixed                                                                                                                                                |
| **available since** | 2.13                                                                                                                                                 |
| **link**            | [https://github.com/UniversalDependencies/UD_Highland_Puebla_Nahuatl-ITML](https://github.com/UniversalDependencies/UD_Highland_Puebla_Nahuatl-ITML) |
| **genre**           | spoken grammar-examples nonfiction                                                                                                                   |
| **contact**         | <pughrob@iu.edu>                                                                                                                                     |
| **sentences**       | 1260                                                                                                                                                 |
| **tokens**          | 10018                                                                                                                                                |

**Issue draft:** [UD_Highland_Puebla_Nahuatl-ITML](../issue_drafts/UD_Highland_Puebla_Nahuatl-ITML.html)

## Modality identification

**Is spoken part clearly identifiable?** Yes - via `sent_id`: sentences from spoken material carry a `.eaf` (ELAN annotation file) reference in their `sent_id`.

## Metadata review

### corpus metadata

(none found)

### languages and translation(s)

| Field        | Advice                         |
| ------------ | ------------------------------ |
| `text[spa]`  | change to `text_spa`           |
| `text[orig]` | change to `text_transcription` |

### transcription and annotation levels available

| Field         | Advice                                                 |
| ------------- | ------------------------------------------------------ |
| `text[gloss]` | change to `text_glossing` -- NOTE: unsure what this is |
| `text[glosa]` | typo                                                   |

### modality metadata

add `# modality = spoken` to sentences whose `sent_id` contains `.eaf` and `# modality = written` to others

## general suggestion

change all `# text[a\d+] = .*` to a different format, in order not to generate a huge number of metadata labels. It can be something like:

```text
# text[a134] = Ke:mah wa:n pos nika:n Kwesala:n tikitah, *este**, ki...,
# text[a136] = ki..., kinamakah a:mo ika *kilo**, ta: ata ika tamachi:w.
```

transformed into

```text
# text_original = [a134] Ke:mah wa:n pos nika:n Kwesala:n tikitah, *este**, ki..., [a136] ki..., kinamakah a:mo ika *kilo**, ta: ata ika tamachi:w.
```
