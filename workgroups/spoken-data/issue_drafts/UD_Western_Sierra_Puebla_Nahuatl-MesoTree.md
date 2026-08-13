---
layout: base
title: 'Issue draft: Western_Sierra_Puebla_Nahuatl MesoTree'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Western_Sierra_Puebla_Nahuatl MesoTree](../treebanks/UD_Western_Sierra_Puebla_Nahuatl-MesoTree.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-MesoTree](https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-MesoTree)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Western_Sierra_Puebla_Nahuatl-MesoTree`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (no signal found):

**Finding:** Not identifiable - the only `genre`-like field has a single constant value.

**Evidence:** Sentence-level `genre` has exactly one value across all sentences: `examples` (2,115). No `newdoc id` or other field was found either.

**Suggestion:** Could you tell us which documents (if any) are transcribed spoken material?

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field         | Suggestion                                                               |
| ------------- | ------------------------------------------------------------------------ |
| `user_id`     | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `finished`    | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `location`    | corpus-specific (speaker/paragraph-level) - verify against metadata.html |
| `orthography` | corpus-specific (speaker/paragraph-level) - verify against metadata.html |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field                | Suggestion                                                                                                             |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `text[spa]`          | change to `text_spa`                                                                                                   |
| `text[orig]`         | change to `text_original`                                                                                              |
| `timestamp`          | possibly rename to `sound_alignment_begin / sound_alignment_end` (see Sentence-level in metadata.html) - please verify |
| `hash`               | corpus-specific (sentence-level) - verify against metadata.html                                                        |
| `alimg`              | corpus-specific (sentence-level) - verify against metadata.html                                                        |
| `locale`             | corpus-specific (sentence-level) - verify against metadata.html                                                        |
| `text[orig_omitlan]` | corpus-specific (sentence-level) - verify against metadata.html                                                        |
| `text[orig_smt]`     | corpus-specific (sentence-level) - verify against metadata.html                                                        |
| `label`              | corpus-specific (sentence-level) - verify against metadata.html                                                        |
| `text[eng]`          | change to `text_eng`                                                                                                   |
| `text[morf]`         | change to `text_morphemic`                                                                                             |
| `text[gloss]`        | change to `text_glossing`                                                                                              |
| `note`               | corpus-specific (sentence-level) - verify against metadata.html                                                        |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
