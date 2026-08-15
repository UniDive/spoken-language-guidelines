---
layout: base
title: 'Issue draft: Abaza ATB'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Abaza ATB](../treebanks/UD_Abaza-ATB.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Abaza-ATB](https://github.com/UniversalDependencies/UD_Abaza-ATB)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Abaza-ATB`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field | Suggestion |
|---|---|
| `text_name` | this is a document identifier but is wrongly repeated on every sentence (only 6 distinct values across 98 sentences) — convert to `# newdoc id = ...` set once at the first sentence of each of the 6 documents, dropping the per-sentence repetition and the `.eaf` extension |
| — | no `genre` field exists, even though topics are recoverable from the `text_name` filenames (e.g. `Professija` = "profession", `O_muzhe` = "about (my) husband", `Deti_v_pole` = "children in the field") — these read as personal narrative/interview elicitations; could add `# genre = narrative` or `interview` per document, please confirm |
| — | no `sound_url` field, though the corpus homepage ([lingconlab.ru/spoken_abaza](http://lingconlab.ru/spoken_abaza/)) implies underlying audio recordings exist — could individual recording links be added? |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| — | no speaker metadata exists at all. The 6 `text_name` filenames each seem to encode one speaker/informant (e.g. `AjsanovaFB`, `SanashokovaCKh`, `DzhuzhuevKM`) — once `text_name` becomes `newdoc id`, could a `speaker_id` be derived from the same filename component? |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `text_orth` | this is a morpheme-segmented orthographic form (hyphens mark morpheme boundaries, stress marked) rather than a duplicate of `text` — rename to `text_morphemic` |
| `text_transcription` | this is a Latin-script rendering of the Cyrillic orthographic form, not a phonetic/IPA transcription — rename to `text_transliteration` |

### Implementation notes

**Quick search & replace**
- `text_orth` → `text_morphemic`
- `text_transcription` → `text_transliteration`
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR \
      --map text_orth=text_morphemic,text_transcription=text_transliteration --write
  ```

**Needs a small script**
- Convert `text_name` (6 distinct values across 98 sentences, confirmed by dry-run) into `# newdoc id`, deduped per document and with the `.eaf` extension stripped:
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-newdoc-from-field DIR \
      --key text_name --strip-suffix .eaf --write
  ```
  This adds `# newdoc id` once per document but leaves the original repeated `# text_name` comments in place - a follow-up `rename-comment`/removal pass is needed if `text_name` should disappear entirely rather than stay as a corpus-specific field.
- Once `newdoc id` exists, a `speaker_id` could likely be derived from the same filename component (e.g. `AjsanovaFB`) with a small regex extraction script - worth doing only after the maintainers confirm the naming convention (see below).

**Needs manual input from maintainers**
- Whether `# genre` (`narrative`/`interview`) should be added per document - inferred from filenames only, not confirmed.
- Whether individual recording links exist and can be published as `# sound_url`.
- Confirm the `speaker_id` extraction pattern from `text_name` before scripting it.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
