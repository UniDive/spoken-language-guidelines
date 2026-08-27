---
layout: base
title:  'Metadata harmonisation'
udver: '2'
---

[Guidelines for Spoken Language UD Treebanks](../spoken-data/)

# Metadata harmonisation

## Background

Speech-related metadata in UD treebanks remains heterogeneous and inconsistently encoded in both spoken-only and mixed-modality resources. This makes it difficult to identify spoken material reliably or retrieve data by speech type (e.g. spontaneous vs. prepared, monologue vs. dialogue) or speaker characteristics (e.g. age, gender, education).

This variation (both in the metadata recorded and in its representation in CoNLL-U) was initially documented by [Dobrovoljc (2022)](https://aclanthology.org/2022.lrec-1.191/), who recommends retaining all available speech-specific metadata in line with prevailing treebank practices and the initial recommendations of [Kahane et al. (2021)](https://aclanthology.org/2021.tlt-1.4/). The [UniDive survey](https://docs.google.com/forms/d/e/1FAIpQLSerAtOMoRmEiO3o99Qv0tMio8m0uriNUhGu-aoKnc29BVUcNg/viewform) (see summary of [results](https://docs.google.com/presentation/d/1KMZbS_dTAlsL-IOb6YDL8gw25_-NW4SPbF-xdbclHMo/edit?slide=id.g2af43d13921_0_95#slide=id.g2af43d13921_0_95)) and the Grew [metadata inventory](https://tables.grew.fr/?data=SP_meta/META) confirm that this heterogeneity persists: not all mixed-modality treebanks explicitly mark spoken material, and many spoken-only treebanks provide no additional speech-specific metadata; where such metadata is available, it varies in type, granularity, and encoding.

Related UD discussions in issues [#1135](https://github.com/UniversalDependencies/docs/issues/1135) and [#1146](https://github.com/UniversalDependencies/docs/issues/1146) further underline the need for clearer and more consistent metadata practices.

## Core metadata categories and naming

When preparing a spoken UD treebank, two core principles should guide the treatment of metadata: (1) **preserve all available metadata** associated with the recordings rather than discarding it during conversion to .conllu, and (2) **adopt shared naming conventions** to avoid reinventing feature names that have already been used in existing treebanks.

Below, we list the most recurrent speech-related metadata categories occurring in existing treebanks and propose their standardized naming, organized by the level at which they apply. The list is not exhaustive: additional metadata may be encoded as needed, but before introducing a new feature, check whether a suitable convention is already used in existing spoken treebanks (see the [Grew metadata inventory](https://tables.grew.fr/?data=SP_meta/META)).

### Document-level

| Feature | Description | Examples |
|---|---|---|
| `modality` | Data modality in mixed-modality treebanks | `# modality = spoken`, `# modality = written`, `# modality = signed` |
| `document_id` | Unique identifier of the speech event | `# document_id = doc01` |
| `sound_url` | Link to the audio recording| `# sound_url = link-to-audio.mp3` |
| `video_url` | Link to the video recording| `# video_url = link-to-video.mp4` |
| `genre` | Descriptive label of the speech event ([more here](#Taxonomy-for-describing-speech-events))  | `# genre = interview`, `# genre = conversation`, `# genre = lecture` |

### Speaker-level

| Feature | Description | Examples |
|---|---|---|
| `speaker_id` | Speaker producing the turn | `# speaker_id = Cf-stra-07534` |
| `speaker_role` | Role in the interaction | `# speaker_role = interviewer` |
| `speaker_age` | Age or age range of the speaker | `# speaker_age = 18 to 35` |
| `speaker_gender` | Gender of the speaker, if available | `# speaker_gender = female`|
| `speaker_education` | Highest completed education level | `# speaker_education = high-school` |
| `speaker_residence` | Place of residence of the speaker | `# speaker_region = south-west`|

### Sentence-level

| Feature | Description | Examples |
|---|---|---|
| `sent_id` | Unique identifier of the utterance | `# sent_id = doc01.s144` |
| `sound_alignment_begin` | Start timestamp in the recording (ms) | `# sound_alignment_begin = 12340` |
| `sound_alignment_end` | End timestamp in the recording (ms) | `# sound_alignment_end = 14560` |
| `duration` | Duration of the sentence (ms) | `# duration = 2220` |
| `text_[type]` | Transcription of a given type | `# text_orthographic = qu'est-ce que tu fais` (other types: `text_phonetic`, `text_morphemic`, `text_transliteration`, `text_conversationanalysis`, `text_macrosyntax`) |
| `text_[ISO]` | Translation into another language (ISO 639-1 two-letter code) | `# text_en = what are you doing` |

### Token-level

| Feature | Description | Examples |
|---|---|---|
| `Lang` | Language identifier for code-switched tokens | `Lang=en` |
| `OrigLang` | Original language of borrowed or inserted tokens | `OrigLang=en` |
| `WordAlignmentBegin` | Start timestamp of the token (ms) | `WordAlignmentBegin=14120` |
| `WordAlignmentEnd` | End timestamp of the token (ms) | `WordAlignmentEnd=14560` |


## (Optional) taxonomy for describing speech events

Spoken treebanks often describe speech events by the type of interaction recorded. To make such descriptions more comparable across treebanks, we propose to distinguish two complementary approaches: an open, descriptive **# genre** label that treebanks define flexibly, and an optional, fixed set of labels describing **interaction parameters** capturing the main dimensions along which speech events vary.

### Genre

Genre is encoded as `genre`, an open descriptive label that treebanks define flexibly to best capture their data, and is the most common way speech events are described. The most frequently reported genres in the survey are `interview`, `conversation`, `lecture`, `speech`, `narrative`, and `monologue`; others include `radio show`, `TV show`, `exam`, `court`, `vlog`, `podcast`, and `commentary`. See also the broader [UD genre discussion here](https://universaldependencies.org/contributing/genres.html).

### Interaction parameters (optional add-on)

In addition to the open-class `genre` label, speech events may be described with a fixed set of interaction parameters. This optional, more fine-grained layer captures the key dimensions of variation in spoken communication, drawing on controlled value sets so that descriptions stay comparable across treebanks. Each parameter is drawn from a fixed value set:

| Parameter | Values | Meaning (in order) |
|---|---|---|
| `degree_of_spontaneity` | `unplanned`, `planned`, `elicited` | no prior preparation; prepared or scripted in advance; produced in response to a task or prompt |
| `number_of_participants` | `monologic`, `dialogic`, `multi-party` | one speaker; two alternating; three or more |
| `context` | `public`, `private`, `professional` | open/general audience; closed personal setting; institutional or workplace setting |
| `setting` | `face-to-face`, `telephone`, `broadcast`, `online` | co-present in one space; audio telephony; mass transmission (radio, TV); internet-mediated |
| `channels` | `phonic-auditory`, `gestural-visual`, `graphic-visual` | spoken/heard; signed/seen; written/read (may combine) |
| `symmetry` | `symmetric`, `asymmetric` | comparable participant roles; differing roles (e.g. interviewer/interviewee) |

For example, a spontaneous face-to-face conversation among friends would be described as:

```
# genre = conversation
# degree_of_spontaneity = unplanned
# number_of_participants = dialogic
# context = private
# setting = face-to-face
# channels = phonic-auditory; gestural-visual
# symmetry = symmetric
```
## Metadata placement and encoding

This metadata can be encoded directly in the CoNLL-U files following standard practice: token-level features in the MISC column, and sentence-, speaker-, and document-level information as `# key = value` comment lines. To avoid repeating shared document- and speaker-level metadata on every sentence, there is also a proposal to store such metadata in an external `metadata.json` file, referenced from the CoNLL-U files via stable identifiers like `document_id` and `speaker_id`, described in more detail [here](treebank_structure.html).
