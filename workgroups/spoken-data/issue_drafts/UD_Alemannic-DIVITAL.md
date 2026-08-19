---
layout: base
title: 'Issue draft: Alemannic DIVITAL'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Alemannic DIVITAL](../treebanks/UD_Alemannic-DIVITAL.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Alemannic-DIVITAL](https://github.com/UniversalDependencies/UD_Alemannic-DIVITAL)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Alemannic-DIVITAL`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Mark spoken documents with `# modality`
The spoken portion of this treebank is clearly identifiable via the `form` field: all 97 documents carry a `# form = ...` value (`dialog` 18, `mixed (form)` 38, `prose` 40, `verse` 1).

**Suggestion:** Add `# modality = spoken` to the 18 documents with `form = dialog`, and `# modality = written` to the remaining 79 (`form` = `mixed (form)`, `prose`, or `verse`), per the [Document-level metadata conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level). We also suggest interpreting the existing `channel` field as `phonic-auditory`, `gestural-visual`, or `graphic-visual`.

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| `author` | make tags: speaker_id |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `language_variety` | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

**Quick search & replace**
- `author` → `speaker_id`
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map author=speaker_id --write
  ```

**Needs a small script**
- Tagging `# modality` from `# form`: confirmed via dry-run that `form` values are `dialog` (18 docs) / `mixed (form)` (38) / `prose` (40) / `verse` (1). Our shared script's `tag-modality` command only matches against `document_id`, not an arbitrary field, so this needs a short bespoke pass (~10 lines) that reads `# form` per document and inserts `# modality = spoken` for `dialog`, `# modality = written` otherwise. Happy to extend `harmonize_metadata.py` with a `--from-field` option if useful.

**Needs manual input from maintainers**
- Confirm `language_variety` naming/placement against metadata.html (flagged as "verify" in the draft).
- Confirm the intended mapping of existing `channel` values (`digital`, `printed`, `typescript` - none of these look like phonic-auditory/gestural-visual/graphic-visual) onto the proposed `channel` vocabulary before any script writes it.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
