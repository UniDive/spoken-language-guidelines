---
layout: base
title: 'Abaza ATB'
udver: '2'
---

# Abaza ATB

[Back to index](../ud_spoken_treebanks.html)

## Overview

|                     |                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| **type**            | only spoken                                                                                                    |
| **available since** | 2.11                                                                                                           |
| **link**            | [https://github.com/UniversalDependencies/UD_Abaza-ATB](https://github.com/UniversalDependencies/UD_Abaza-ATB) |
| **genre**           | spoken                                                                                                         |
| **contributors**         | Koshevoy, Alexey; Panova, Anastasia; Makarchuk, Ilya |
| **sentences**       | 98                                                                                                             |
| **tokens**          | 652                                                                                                            |

**Issue draft:** [UD_Abaza-ATB](../issue_drafts/UD_Abaza-ATB.html)

## Modality identification

**Is spoken part clearly identifiable?**
N/A

## Metadata review


Every sentence carries exactly the same six comment fields, plus one MISC feature on (nearly) every token:

| Field                | Level                                                                                                 | Example                                                    | Standard name ([metadata.md](../metadata.html))                                                         | Advice                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `text_orth`          | sentence                                                                                              | `# text_orth = сарА сы-хьиз фатима-пI`                     | this seems a **morpheme-segmented** orthographic form (hyphens mark morpheme boundaries, stress marked) | rename to `text_morphemic`                                                                                                                  |
| `text_transcription` | sentence                                                                                              | `# text_transcription = sará sə-χ'iz fatima-ṗ`             | Latin-script rendering of the Cyrillic orthographic form (not a phonetic/IPA transcription)             | rename to `text_transliteration`                                                                                                            |
| `text_rus`           | sentence                                                                                              | `# text_rus = Меня зовут Фатима.`                          | translation field; project convention now uses 2-letter ISO 639-1 codes                                 | rename to `text_ru`                                                                                                                         |
| `text_name`          | sentence *(but constant across all sentences of one recording — 6 distinct values over 98 sentences)* | `# text_name = Professija_AjsanovaFB_11072017_checked.eaf` | this seems a **document identifier**, wrongly repeated per-sentence instead of set once per document    | convert to `# document_id = ...` at the first sentence of each of the 6 documents (drop the per-sentence repetition and the `.eaf` extension) |

### Not present, worth considering

- **Speaker metadata**: none at all (`speaker_id`, `speaker_role`, etc. absent). The 6 `text_name` filenames encode a speaker per recording (e.g. `AjsanovaFB`, `SanashokovaCKh`, `DzhuzhuevKM`, `BidzhevaTA`, `AsanaevaFM` — initials suggest one speaker/informant per file). Once `text_name` is converted to `document_id`, a `speaker_id` could plausibly be derived from the same filename component.
- **Genre**: no `# genre = ...` field, even though topics are recoverable from filenames. These read as personal narrative/interview elicitations — could add `# genre = narrative` or `interview` per document.
- **`sound_url`**: the corpus homepage ([lingconlab.ru/spoken_abaza](http://lingconlab.ru/spoken_abaza/)) implies underlying audio recordings exist; no link is included in the `.conllu`. Worth asking whether individual recording URLs can be shared.