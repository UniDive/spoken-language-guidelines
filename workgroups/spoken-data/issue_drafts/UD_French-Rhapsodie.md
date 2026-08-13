---
layout: base
title: 'Issue draft: French Rhapsodie'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to French Rhapsodie](../treebanks/UD_French-Rhapsodie.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_French-Rhapsodie](https://github.com/UniversalDependencies/UD_French-Rhapsodie)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_French-Rhapsodie`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `newdoc id` exists, but `sent_id` already encodes it: e.g. `Rhap_D0001-1` is document `Rhap_D0001`, sentence `1`. 57 distinct documents across 3209 sentences, matching exactly the 57 distinct `sound_url` values (present on every single sentence). Several other fields are also constant within each document (verified: none vary within a document) and should move to document level too: `genre`, `subgenre`, `type`, `task`, `subject`, `channel`, `modalities`.

| Field                                                                   | Suggestion                                                                                  |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| —                                                                       | derive `# newdoc id` from the `sent_id` prefix (everything before the trailing `-<number>`) |
| `sound_url`                                                             | move to document level, set once per `newdoc id`                                            |
| `genre`, `subgenre`, `type`, `task`, `subject`, `channel`, `modalities` | move to document level (constant per document)                                              |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion                                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `speaker` | corpus-specific turn-position label (`L1`, `L2`, ...), distinct from and redundant with `speaker_id` (e.g. `§LF30`) - keep, `speaker_id` is already standard |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field                 | Suggestion                                                                            |
| --------------------- | ------------------------------------------------------------------------------------- |
| `macrosyntax`         | rename to `text_macrosyntax`                                                          |
| `prosodic_annotation` | corpus-specific (only on a subset of sentences) - please confirm what this represents |

### 4. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field        | Suggestion                     |
| ------------ | ------------------------------ |
| `AlignBegin` | rename to `WordAlignmentBegin` |
| `AlignEnd`   | rename to `WordAlignmentEnd`   |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
