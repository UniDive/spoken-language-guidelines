---
layout: base
title: 'Issue draft: Nheengatu CompLin'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Nheengatu CompLin](../treebanks/UD_Nheengatu-CompLin.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Nheengatu-CompLin](https://github.com/UniversalDependencies/UD_Nheengatu-CompLin)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Nheengatu-CompLin`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

Not from the current data. 2,827 of 2,839 sentences carry a written-source citation (grammars, dictionaries, Bible translations), and all sampled sources are published written works - could you confirm whether any sentences actually originate from spoken/elicited fieldwork, and if so how they're distinguished?

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field   | Suggestion                          |
| ------- | ------------------------------------ |
| `title` | rename to `document_id` - please verify |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field            | Suggestion                             |
| ---------------- | --------------------------------------- |
| `speaker`        | rename to `speaker_id` - please verify |
| `speaker_gender` | OK - already standard                   |

Besides these, the corpus carries ~18 editorial/philological fields at speaker or paragraph level (`reviewer1/2`, `text_orig_transcriber`, `acknowledgement`, `review_status`, translators/modernizers of the Portuguese text, etc.). These are source-critical apparatus rather than spoken-language metadata, so we're not proposing renames for them - please confirm they should stay as-is.

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
| ----------------------------- | ------------------------------------------ |
| `text_eng`, `text_por`, `text_rus` | OK - already ISO 639-3 (`eng`/`por`/`rus`) |

The corpus also carries roughly 100 further sentence-level fields (`text_orig`, `text_source*`, `text_prim*`, `text_sec*`, `text_alt*`, `place*`, `date`, `note*`, cross-references, and similar variant/source-tracking fields, plus their Portuguese-suffixed counterparts). These document the philological apparatus of the printed sources (variant readings, glosses, cross-references) rather than spoken-language properties, so we're not proposing individual renames - happy to share the full field list if useful for your own review.

### 5. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

`OrigLang` is already used with the standard name - no change needed.

### Implementation notes

**Needs manual input from maintainers**
- Whether any sentences are actually spoken/elicited fieldwork (vs. published written sources) - this is a factual question only the maintainers can answer; nothing to script until it's resolved.
- `title` → `document_id`: mechanically a one-line rename (field occurs once per document already), but flagged "please verify" since it changes the document-identification scheme - once confirmed: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map title="document_id" --write`.
- `speaker` → `speaker_id`: mechanically a one-line rename (`# speaker = Gerson` style, repeats per sentence, no split/hoist needed), but flagged "please verify" - once confirmed: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map speaker=speaker_id --write`.
- The ~18 editorial/philological fields and ~100 source-tracking sentence-level fields: no rename proposed, just need maintainer confirmation they should stay as-is (no script involved either way).

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
