---
layout: base
title: 'Issue draft: Ukrainian ParlaMint'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Ukrainian ParlaMint](../treebanks/UD_Ukrainian-ParlaMint.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint](https://github.com/UniversalDependencies/UD_Ukrainian-ParlaMint)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Ukrainian-ParlaMint`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

Yes - the entire corpus should be `# modality = spoken`. The README describes it as "Ukrainian parliamentary plenary session transcripts" drawn from ParlaMint-UA and other open sources (NSDC); there's no written material.

**Suggestion:** Add `# modality = spoken` corpus-wide.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

`document_id` already exists for the ParlaMint-sourced sentences (one per utterance, e.g. `ParlaMint-UA_2022-01-25-m0.u100`), but is entirely missing for the 502 sentences sourced from NSDC (`sent_id` like `NSDC_UA_28_Feb2014-1`). These can easily get a `document_id` too, derived from the `sent_id` prefix (everything before the trailing `-<number>`) - all 502 collapse to a single document, `NSDC_UA_28_Feb2014`.

| Field | Suggestion                                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |
| —     | derive `# document_id = NSDC_UA_28_Feb2014` for the NSDC-sourced sentences (`sent_id` prefix before the trailing `-<number>`) |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

`text_en` and `phonetic_text` each appear exactly once across the entire corpus, both with the literal placeholder value `undefined undefined` - these look like leftover template artifacts rather than real content.

| Field           | Suggestion                                                                         |
| --------------- | ---------------------------------------------------------------------------------- |
| `text_en`       | remove (single occurrence, placeholder value `undefined undefined`) |
| `phonetic_text` | remove (single occurrence, placeholder value `undefined undefined`) |
| `WARNING`       | corpus-specific (sentence-level, parser-diagnostic comments e.g. dependency-cycle warnings) - verify against metadata.html |

### 4. Token-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#token-level))

| Field  | Suggestion                                                                   |
| ------ | ---------------------------------------------------------------------------- |
| `lang` | rename to `Lang` |

### Implementation notes

- **Quick search & replace:**
  - Add corpus-wide `# modality = spoken` - since the whole corpus is spoken, this is a single-line insertion after every `# document_id` (or every `# sent_id` if `document_id` is still missing for the NSDC block, see below): `sed -i '' '/^# document_id/a\
# modality = spoken' *.conllu`.
  - Remove `text_en` / `phonetic_text` (placeholder `undefined undefined`). Checked the local clone: this occurs once per release split (dev/test/train = 3 total occurrences, not "exactly once" as the draft states - each is one line pair, e.g. `uk_parlamint-ud-dev.conllu:5432-5433`) - safe to delete both lines wherever they appear: `sed -i '' '/^# text_en = undefined undefined$/d;/^# phonetic_text = undefined undefined$/d' *.conllu`.
  - `lang` → `Lang` (MISC key): note this key was **not found** in the currently-cloned copy of the corpus (`grep` for `lang=`/`Lang=` in MISC came up empty) - double-check it still exists in the maintainers' working copy before running `harmonize_metadata.py rename-misc UD_Ukrainian-ParlaMint --map lang=Lang --write`; it may already have been fixed upstream.
- **Needs a small script:** derive `# document_id = NSDC_UA_28_Feb2014` for the 502 NSDC-sourced sentences. Note `harmonize_metadata.py derive-document-id` isn't directly usable here since it skips any file that already contains *some* `# document_id` comments (which this file does, from the ParlaMint-sourced sentences) - but since all 502 NSDC sentences collapse into a single document, this is actually simpler than the generic tool: insert one line before the first NSDC sentence: `sed -i '' '/^# sent_id = NSDC_UA_28_Feb2014-1$/i\
# document_id = NSDC_UA_28_Feb2014' *.conllu` (confirmed only `train` contains the NSDC block).
- **Needs manual input from maintainers:** `WARNING` (sentence-level, parser-diagnostic comments) - corpus-specific, needs a naming decision.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
