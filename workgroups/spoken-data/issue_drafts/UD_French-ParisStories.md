---
layout: base
title: 'Issue draft: French ParisStories'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to French ParisStories](../treebanks/UD_French-ParisStories.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_French-ParisStories](https://github.com/UniversalDependencies/UD_French-ParisStories)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_French-ParisStories`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but `sent_id` already encodes it: e.g. `ParisStories_2020_maisonAbondonnee_1` is document `ParisStories_2020_maisonAbondonnee`, sentence `1`. 86 distinct documents across 2776 sentences. `sound_url` is currently repeated per sentence (present on 2749/2776 sentences - 27 sentences in one document lack it).

| Field       | Suggestion                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------- |
| —           | derive `# newdoc id` from the `sent_id` prefix (everything before the trailing `_<number>`) |
| `sound_url` | move to document level, set once per `newdoc id`                                            |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion             |
| --------- | ---------------------- |
| `speaker` | rename to `speaker_id` |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field         | Suggestion                                                                              |
| ------------- | --------------------------------------------------------------------------------------- |
| `macrosyntax` | rename to `text_macrosyntax`                                                            |
| `tags`        | corpus-specific (only 1 occurrence, value `TODO`) - please confirm what this represents |

### 4. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
