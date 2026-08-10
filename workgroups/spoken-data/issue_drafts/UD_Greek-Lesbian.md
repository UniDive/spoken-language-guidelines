---
layout: base
title: 'Issue draft: Greek Lesbian'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Greek Lesbian](../treebanks/UD_Greek-Lesbian.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Greek-Lesbian](https://github.com/UniversalDependencies/UD_Greek-Lesbian)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Greek-Lesbian`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken.

**Finding:** Identifiable via the sentence-level `oral_corpus` field, which marks sentences drawn from audio recordings as opposed to published dictionaries/books. This aligns with the `source` field, which also splits cleanly into `Recording (Date:..., Location:..., Gender:...)` entries (151+72+19+13+11+4 = 270 sentences, across 6 recording locations) and published dictionary/book citations (e.g. Ralli 2017, Tsokarou-Mitsioni 1998/2019, Papanis 2004, Anagnostopoulou 2021, Anagnostou 2014).

**Suggestion:** Add `# modality = spoken` to sentences where `oral_corpus` marks the source as an audio recording.

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

For recording entries, `source` packs several attributes into one string (`Recording (Date:..., Location:..., Gender:...)`). We suggest decomposing it into structured fields:

| Field                                | Suggestion                                                                          |
| ------------------------------------ | ----------------------------------------------------------------------------------- |
| `source` (`Gender:...`)              | split out as `speaker_gender`                                                       |
| `source` (`Location:...`)            | split out as `speaker_residence`                                                    |
| `source` (`Date:...`)                | split out as a corpus-specific date field (no standard field covers recording date) |
| `source` (dictionary/book citations) | keep as-is - not applicable to the decomposition above                              |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field      | Suggestion                                                      |
| ---------- | --------------------------------------------------------------- |
| `text_el`  | rename to `text_ell` (ISO 639-3 code)                           |
| `text__el` | corpus-specific (sentence-level) - verify against metadata.html |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
