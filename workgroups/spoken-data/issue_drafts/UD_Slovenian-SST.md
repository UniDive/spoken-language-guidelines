---
layout: base
title: 'Issue draft: Slovenian SST'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Slovenian SST](../treebanks/UD_Slovenian-SST.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Slovenian-SST](https://github.com/UniversalDependencies/UD_Slovenian-SST)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Slovenian-SST`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field       | Suggestion                      |
| ----------- | ------------------------------- |
| `sound_url` | possibly move to document level |

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field        | Suggestion |
| ------------ | ---------- |
| `speaker_id` | OK         |

### Implementation notes

**Needs manual input from maintainers**
- `sound_url` → document level: dry-run of `python3 workgroups/spoken-data/scripts/harmonize_metadata.py hoist-to-doc DIR --key sound_url` against the real `train` file shows it's **not** safe to hoist as-is - only 34 of 277 documents have a constant `sound_url` across all their sentences; the other 243 vary sentence-to-sentence (each sentence likely points at its own audio clip within the recording, not one file per document). This confirms the draft's "possibly" hedge - please clarify whether `sound_url` is meant to be per-sentence (in which case no change is needed, it's already correctly scoped) or whether there's a separate constant per-document URL to add instead. No script change is safe to propose until that's settled.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
