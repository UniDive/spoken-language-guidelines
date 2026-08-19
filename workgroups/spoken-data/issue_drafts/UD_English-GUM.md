---
layout: base
title: 'Issue draft: English GUM'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to English GUM](../treebanks/UD_English-GUM.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_English-GUM](https://github.com/UniversalDependencies/UD_English-GUM)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_English-GUM`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Mark spoken documents with `# modality`
The spoken portion of this treebank is identifiable via `meta::genre`. Checked directly against `en_gum-ud-dev.conllu` and `en_gum-ud-test.conllu` (30 documents/1575 sentences in dev, 30 documents/1464 sentences in test; 15 genres, 2 documents each per split). 5 of the 15 genres are spoken - `vlog`, `speech`, `podcast`, `court`, `conversation` - 10 documents per split, 20 total:

| Genre | dev | test |
|---|---|---|
| `conversation` | `GUM_conversation_grounded`, `GUM_conversation_risk` | `GUM_conversation_lambada`, `GUM_conversation_retirement` |
| `court` | `GUM_court_loan`, `GUM_court_negligence` | `GUM_court_insanity`, `GUM_court_mitigation` |
| `podcast` | `GUM_podcast_bangladesh`, `GUM_podcast_wrestling` | `GUM_podcast_bezos`, `GUM_podcast_multitasking` |
| `speech` | `GUM_speech_impeachment`, `GUM_speech_inauguration` | `GUM_speech_austria`, `GUM_speech_newzealand` |
| `vlog` | `GUM_vlog_portland`, `GUM_vlog_radiology` | `GUM_vlog_london`, `GUM_vlog_studying` |

The other 10 genres (`academic`, `bio`, `essay`, `fiction`, `interview`, `letter`, `news`, `textbook`, `voyage`, `whow`) are written or mixed-modality (`interview` here is written Q&A, not transcribed speech).

**Suggestion:** Add `# modality = spoken` to the 20 documents listed above and `# modality = written` to the rest. This was checked in dev/test only - please confirm the same genre labels apply consistently in train.

We also checked source/summary metadata for one document per spoken genre to propose [interaction parameters](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#interaction-parameters-optional-add-on) (an optional add-on) - please confirm per-document, since genre alone doesn't guarantee every document in a genre matches exactly:

| Genre | `degree_of_spontaneity` | `number_of_participants` | `context` | `setting` | `channels` | `symmetry` |
|---|---|---|---|---|---|---|
| `conversation` | unplanned | dialogic/multi-party | private | face-to-face | phonic-auditory; gestural-visual | symmetric |
| `court` | planned | multi-party | professional | face-to-face | phonic-auditory; gestural-visual | asymmetric |
| `podcast` | unplanned | multi-party | public | online | phonic-auditory | asymmetric |
| `speech` | planned | monologic | public | broadcast | phonic-auditory; gestural-visual | asymmetric |
| `vlog` | planned | monologic | public | online | phonic-auditory; gestural-visual | asymmetric |

Notes: `conversation` is Santa Barbara Corpus audio (no video) of private family/partner talk; `court` is audio-only Supreme Court oral argument (live Q&A elicited by justices' questions, hence `elicited` rather than `unplanned`); `podcast` (Global Voices) has editors plus 2 guests, audio-only; `speech` and `vlog` are both video-recorded (C-SPAN and YouTube respectively) with a single speaker/creator addressing an audience with no back-and-forth, hence `asymmetric`.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

| Field | Suggestion |
|---|---|
| `document_id` | make tags: doc_id |
| `meta::genre` | make tags: genre |

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| `speaker` | make tags: speaker_id |

### 4. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

| Field | Suggestion |
|---|---|
| `meta` | corpus-specific (sentence-level) - verify against metadata.html |
| `trailing_xml` | corpus-specific (sentence-level) - verify against metadata.html |

### Implementation notes

- **Quick search & replace:** `document_id`→tag `doc_id`, `meta::genre`→tag `genre`, `speaker`→tag `speaker_id`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map meta::genre=genre,speaker=speaker_id --write` (the `doc_id` tag addition is a tagset change, not a comment rename).
- **Needs a small script:** modality tagging by genre is mechanical and verified against the real corpus: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality DIR --spoken-if '_(vlog|speech|podcast|court|conversation)_' --written-if '.*' --write` gives exactly 10/30 spoken documents in dev and 10/30 in test, matching the draft's count precisely. Only run on `en_gum-ud-dev.conllu`/`en_gum-ud-test.conllu` for now (train genre labels aren't yet confirmed - see manual item below); once confirmed, the same command run over the whole treebank directory covers train too.
- **Needs manual input from maintainers:**
  - Confirm the 15 genre labels (and the 5 spoken ones) apply consistently in `en_gum-ud-train.conllu` before running the modality-tagging command over train.
  - The proposed per-genre interaction parameters (`degree_of_spontaneity`, `number_of_participants`, `context`, `setting`, `channels`, `symmetry`) are genre-level defaults, not verified per document - once confirmed, adding them is a mechanical `rename-comment`-style insert per document, but the values themselves need sign-off first.
  - `meta` and `trailing_xml` (sentence-level) are corpus-specific with no proposed names yet.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
