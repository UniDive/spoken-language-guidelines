---
layout: base
title: 'Issue draft: Norwegian NynorskLIA'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Norwegian NynorskLIA](../treebanks/UD_Norwegian-NynorskLIA.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Norwegian-NynorskLIA](https://github.com/UniversalDependencies/UD_Norwegian-NynorskLIA)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Norwegian-NynorskLIA`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion                                                                                                                       |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `dialect` | OK as corpus-specific field, but `speaker_id` is currently embedded within it - please split `speaker_id` out into its own field |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
