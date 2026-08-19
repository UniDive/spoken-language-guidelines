---
layout: base
title: 'Issue draft: Western_Sierra_Puebla_Nahuatl MesoTree'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Western_Sierra_Puebla_Nahuatl MesoTree](../treebanks/UD_Western_Sierra_Puebla_Nahuatl-MesoTree.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-MesoTree](https://github.com/UniversalDependencies/UD_Western_Sierra_Puebla_Nahuatl-MesoTree)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Western_Sierra_Puebla_Nahuatl-MesoTree`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (no signal found):

**Finding:** Not identifiable - the only `genre`-like field has a single constant value.

**Evidence:** Sentence-level `genre` has exactly one value across all sentences: `examples` (2,115). No `document_id` or other field was found either.

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

### Implementation notes

- **Quick search & replace:** the bracketed `text[...]` fields are literal fixed-string comment keys that `harmonize_metadata.py`'s key regex doesn't currently parse (it doesn't allow `[`/`]` in a key name), so plain `sed` is actually simpler here. Confirmed the exact key format in the local clone (`nhi_mesotree-ud-test.conllu`, e.g. `# text[spa] = `):
  ```
  sed -i '' \
    -e 's/^# text\[spa\] = /# text_spa = /' \
    -e 's/^# text\[orig\] = /# text_original = /' \
    -e 's/^# text\[eng\] = /# text_eng = /' \
    -e 's/^# text\[morf\] = /# text_morphemic = /' \
    -e 's/^# text\[gloss\] = /# text_glossing = /' \
    *.conllu
  ```
- **Needs manual input from maintainers:** which documents (if any) are spoken material (item 1, no signal found in the data at all); `timestamp`'s possible mapping to `sound_alignment_begin`/`sound_alignment_end`; and all remaining corpus-specific fields needing a naming decision (`user_id`, `finished`, `location`, `orthography`, `hash`, `alimg`, `locale`, `text[orig_omitlan]`, `text[orig_smt]`, `label`, `note`).

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
