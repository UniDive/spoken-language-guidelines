---
layout: base
title: 'Issue draft: Frisian_Dutch Fame'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Frisian_Dutch Fame](../treebanks/UD_Frisian_Dutch-Fame.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Frisian_Dutch-Fame](https://github.com/UniversalDependencies/UD_Frisian_Dutch-Fame)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Frisian_Dutch-Fame`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

`speaker` is a composite/slash-separated string packing three pieces of metadata in one field, e.g. `fr/female/sp0013f`, `fr/child/sp0061c`: `<language variety>/<gender-or-age category>/<speaker code>` (the code's trailing letter redundantly repeats the category: `f`/`m`/`c`). We'd suggest splitting it into separate fields rather than a simple rename:

| Field                                                                 | Suggestion                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `speaker` (3rd segment, e.g. `sp0013f`)                               | split out and rename to `speaker_id`                                                                                                                                                                                                                                                                       |
| `speaker` (2nd segment: `male`/`female`/`child`, 285/114/2 sentences) | split out and rename to `speaker_gender` - `child` doesn't fit a gender value, would need `speaker_age` instead for those 2 sentences; could you confirm the intended handling?                                                                                                                            |
| `speaker` (1st segment: `fr`/`nl`)                                    | split out; not a standard field in our conventions - it's stable per speaker (142 of 143 speaker codes have only one value), likely the speaker's dominant/native language variety in this Frisian-Dutch bilingual corpus - could you confirm and suggest a name (e.g. corpus-specific `speaker_variety`)? |

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
