---
layout: base
title: 'Issue draft: Skolt_Sami Giellagas'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Skolt_Sami Giellagas](../treebanks/UD_Skolt_Sami-Giellagas.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Skolt_Sami-Giellagas](https://github.com/UniversalDependencies/UD_Skolt_Sami-Giellagas)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Skolt_Sami-Giellagas`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material, and it turns out this aligns exactly with the file split:

**Finding:** Per the README, the corpus "originally consists of twenty translated sentences ... made by Hilkka Fofonoff from the Finnish texts", with all subsequent sentences from the Giellagas Corpus of Spoken Saami Languages. This matches the data exactly: `sms_giellagas-ud-train.conllu` contains exactly those 20 sentences (`sent_id` prefix `FofonoffHilkka_brat_2018`) - written, translated from Finnish. `sms_giellagas-ud-test.conllu` contains the remaining 241 sentences - spoken, drawn from field recordings (`sent_id` prefixes like `11308_1a::<timestamp>`, `NA2_00635_1az::<timestamp>`) and published transcriptions of recorded speech (`kotus-skak2010-*`).

**Suggestion:** Add `# modality = written` to `train` sentences and `# modality = spoken` to `test` sentences. One caveat: a handful of `test` sentences (`SK2020-*`, `SKKV2020:*`) are grammar-book examples rather than recordings - could you confirm whether these should also count as spoken?

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but it can be derived from the source-identifier prefix of `sent_id` (the part before the timestamp/counter suffix), e.g. `11308_1a` and `NA2_00635_1az` (recordings), `kotus-skak2010-1-1` (published transcription), `SK2020`, `SKKV2020`, `Juutinen2023`, `FofonoffHilkka_brat_2018` (other sources). The exact delimiter varies by source (`::` before timestamps, `:`/`-` before a numeric counter otherwise) - please confirm the intended document granularity.

| Field | Suggestion                                                       |
| ----- | ---------------------------------------------------------------- |
| —     | derive `# newdoc id` from the `sent_id` source-identifier prefix |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

`aannotation` (likely a typo for "annotation") packs three XML-style attributes into one comment line: `# aannotation="yes" begintime="0:39:13" endtime="0:09:18"` (`endtime` is sometimes empty).

| Field                       | Suggestion                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `aannotation` (`begintime`) | split into `sound_alignment_begin`                                                                                                         |
| `aannotation` (`endtime`)   | split into `sound_alignment_end` (when present); derive `duration` from begin/end when both are available                                  |
| `text_fi`                   | rename to `text_fin` (ISO 639-3)                                                                                                           |
| `story_id`                  | corpus-specific (sentence-level) - verify against metadata.html                                                                            |
| `comment`                   | corpus-specific (sentence-level) - verify against metadata.html                                                                            |
| `text_en`                   | rename to `text_eng` (ISO 639-3)                                                                                                           |
| `-`                         | corpus-specific (sentence-level) - verify against metadata.html                                                                            |
| `text_olo`                  | OK - Olonets/Livvi Karelian translation (`olo` is already the correct ISO 639-3 code); only present on the 20 written/translated sentences |
| `text_mdf`                  | OK - Moksha translation (`mdf` is already the correct ISO 639-3 code); only present on the 20 written/translated sentences                 |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
