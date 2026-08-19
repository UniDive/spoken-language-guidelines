---
layout: base
title: 'Issue draft: Hausa WesternAutogramm'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Hausa WesternAutogramm](../treebanks/UD_Hausa-WesternAutogramm.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Hausa-WesternAutogramm](https://github.com/UniversalDependencies/UD_Hausa-WesternAutogramm)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Hausa-WesternAutogramm`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (no signal found):

**Finding:** No genre-like field or `document_id` found at all.

**Evidence:** No comment-level metadata beyond `sent_id`/`text` detected.

**Suggestion:** Could you point us to which sentences/documents are spoken vs. written?

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                      |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field        | Suggestion |
| ------------ | ---------- |
| `speaker_id` | OK         |

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field           | Suggestion                                                                |
| --------------- | ------------------------------------------------------------------------- |
| `text_en`       | change to `text_eng`                                                      |
| `text_ortho`    | change to `text_orthographic`                                             |
| `sent_timecode` | split into `sound_alignment_begin`, `sound_alignment_end`, and `duration` |

### Implementation notes

**Quick search & replace**
- `text_en` → `text_eng`, `text_ortho` → `text_orthographic` (`# oldkey =` → `# newkey =`).

**Needs a small script**
- `sound_url` → document level: the released `ha_westernautogramm-ud-test.conllu` has no `# document_id` at all, but `sound_url` is constant within each of the 6 source recordings (verified against `not-to-release/original_split/*.conllu`, one distinct `sound_url` per file, matching 6 distinct values in the released file). `sent_id` (`BC_HAU_Gouffé_1_01_Zugal_001-002_split1`, …) doesn't have a clean numeric-suffix delimiter `derive-document-id` can parse automatically, so `# document_id` needs to be (re)introduced first, either from the `original_split` file boundaries or from a maintainer-confirmed `sent_id` pattern; after that, `hoist-to-doc --key sound_url` is a one-line, already-constant hoist.
- Once the format below is confirmed, most `sent_timecode` values (single `begin, end` pair, e.g. `1000, 3000`) split cleanly with `split-field --key sent_timecode --sep ", " --into sound_alignment_begin,sound_alignment_end`; `duration` would then be a trivial `end - begin` computed in a follow-up pass, not a plain split.

**Needs manual input from maintainers**
- Modality: no genre/`document_id` signal found at all - need pointers to which sentences/documents are spoken vs. written before anything can be tagged.
- `sent_timecode` format: dry-running the split above shows a subset of values hold **two** `begin, end` pairs space-separated in one field (e.g. `34892, 35164 35164, 35361`) - these line up with `_split1`/`_split2` suffixes in `sent_id`, i.e. one original utterance re-split into two sentences that both kept the parent's full timecode range. Need to confirm whether each half should get its own half of the range, or whether these should be left as corpus-specific.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
