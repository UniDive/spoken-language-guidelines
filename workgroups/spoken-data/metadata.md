---
layout: base
title:  'Metadata harmonisation'
udver: '2'
---

# Metadata harmonisation

## Problem overview

Speech-related metadata in UD treebanks is currently encoded in heterogeneous and inconsistent ways. This affects both spoken-only and mixed-modality treebanks. As a result, it is often difficult to reliably identify spoken data within mixed-modality resources and to retrieve specific types of speech (e.g. spontaneous vs. prepared, public vs. private, monologue vs. dialogue), or speaker-related information (e.g. age, gender, education). Harmonization is therefore essential to enable efficient retrieval of relevant spoken data within and across treebanks and thus advance the underexplored field of spoken grammar research.

## Current situation

Variation in the encoding of speech-related metadata in UD treebanks (both in the information recorded and in how it is represented in CoNLL-U) has already been documented by [Dobrovoljc (2022)](https://aclanthology.org/2022.lrec-1.191/), who recommends systematically recording all available speech-specific metadata in line with prevailing treebank practices and the initial recommendations proposed by [Kahane et al. (2021)](https://aclanthology.org/2021.tlt-1.4/). The results of the [UniDive spoken data annotation survey](https://docs.google.com/forms/d/e/1FAIpQLSerAtOMoRmEiO3o99Qv0tMio8m0uriNUhGu-aoKnc29BVUcNg/viewform) among spoken UD treebank developers ([results overview](https://docs.google.com/presentation/d/1KMZbS_dTAlsL-IOb6YDL8gw25_-NW4SPbF-xdbclHMo/edit?slide=id.g2af43d13921_0_95#slide=id.g2af43d13921_0_95)), carried out at the end of 2024, and the automatically extracted metadata inventory (see [overview table](https://tables.grew.fr/?data=SP_meta/META) in Grew) confirm that such heterogeneity persists. For example, not all mixed-modality treebanks explicitly mark spoken material, and among spoken-only treebanks only 72% provide additional speech-specific metadata, which, when present, varies considerably in type, granularity, and encoding conventions.

More broadly, questions concerning the encoding of metadata in CoNLL-U have also been discussed within the UD community (see issues [#1135](https://github.com/UniversalDependencies/docs/issues/1135) and [#1146](https://github.com/UniversalDependencies/docs/issues/1146)), highlighting the need for clearer and more consistent practices beyond speech-specific data only.

## Our proposal for cross-linguistic harmonization of metadata encoding

### Main principles
When preparing a spoken UD treebank, two core principles should guide the treatment of metadata: (1) **preserve all available metadata** associated with the recordings rather than discarding it during conversion to .conllu, and (2) **adopt shared naming conventions** to avoid reinventing feature names that have already been used in existing treebanks.

### Core metadata categories and naming
Below, we list the most recurrent speech-related metadata categories occurring in existing treebanks and propose their standardized naming, organized by the level at which they apply.

#### Document-level

| Feature | Description | Examples |
|---|---|---|
| `modality` | Data modality in mixed-modality treebanks | `# modality = spoken`, `# modality = written`, `# modality = signed` |
| `newdoc id` | Unique identifier of the speech event | `# newdoc id = doc01` |
| `sound_url` | Link to the audio recording| `# sound_url = link-to-audio.mp3` |
| `video_url` | Link to the video recording| `# video_url = link-to-video.mp4` |
| `genre` | Descriptive label of the speech event (see [alternative](###ADD))  | `# genre = interview`, `# genre = conversation`, `# genre = lecture` |

#### Speaker-level

| Feature | Description | Examples |
|---|---|---|
| `speaker_id` | Speaker producing the turn | `# speaker_id = Cf-stra-07534` |
| `speaker_role` | Role in the interaction | `# speaker_role = interviewer` |
| `speaker_age` | Age or age range of the speaker | `# speaker_age = 18 to 35` |
| `speaker_gender` | Gender of the speaker, if available | `# speaker_gender = female`|
| `speaker_education` | Highest completed education level | `# speaker_education = high-school` |
| `speaker_residence` | Place of residence of the speaker | `# speaker_region = south-west`|

#### Sentence-level

| Feature | Description | Examples |
|---|---|---|
| `sent_id` | Unique identifier of the utterance | `# sent_id = doc01.s144` |
| `sound_alignment_begin` | Start timestamp in the recording (ms) | `# sound_alignment_begin = 12340` |
| `sound_alignment_end` | End timestamp in the recording (ms) | `# sound_alignment_end = 14560` |
| `duration` | Duration of the sentence (ms) | `# duration = 2220` |
| `text_[type]` | Transcription of a given type | `# text_orthographic = qu'est-ce que tu fais` (other types: `text_phonetic`, `text_morphemic`, `text_transliteration`, `text_conversationanalysis`, `text_macrosyntax`) |
| `text_[ISO]` | Translation into another language (ISO code) | `# text_en = what are you doing` |

#### Token-level

| Feature | Description | Examples |
|---|---|---|
| `Lang` | Language identifier for code-switched tokens | `Lang=en` |
| `OrigLang` | Original language of borrowed or inserted tokens | `OrigLang=en` |
| `WordAlignmentBegin` | Start timestamp of the token (ms) | `WordAlignmentBegin=14120` |
| `WordAlignmentEnd` | End timestamp of the token (ms) | `WordAlignmentEnd=14560` |


Additional metadata may be encoded flexibly; however, developers are encouraged to first check whether a suitable solution already exists in current treebanks (see the [Grew inventory of metadata](https://tables.grew.fr/?data=SP_meta/META) found in existing spoken data treebanks).


### Taxonomy for describing speech events
In addition to technical metadata harmonization, spoken treebanks often describe speech events in terms of the type of interaction recorded. To make such descriptions more comparable across treebanks, we propose distinguishing between genre as an open, descriptive label (which treebanks can define flexibly), and a fixed set of interaction parameters that capture the main dimensions along which speech events vary. (See also Luisa’s nice longer introduction in green below.)

It should be noted that some genres display a high level of routinization (i.e. exams-> e.g. much anxiety leads to use of certain functional elements etc.): this, because of all the components of modality, is mirrored by language. Keeping genre open and the parameters fixed leaves scholars to their own interpretation and anyways provides a schema to conform to.

* Genres
  * Genre is encoded as genre, and treebanks may use descriptive labels that best capture their data. According to the survey of existing spoken treebanks, the most frequently reported genres include:
    * interview
    * conversation
    * lecture
    * speech
    * narrative
    * monologue
    * Others also include: radio show, TV show, exam, court, vlog, podcast, commentary, etc. See also genre-related discussions and categorizations in UD more broadly here.

* Interaction parameters:
  * To complement genre labels, we additionally propose a fixed set of interaction parameters capturing key dimensions of variation in spoken communication.
	TODO: add short definitions/examples for each of the options below

* degree_of_spontaneity:
  * unplanned
  * planned
  * elicited

* number_of_participants:
  * monologic
  * dialogic
  * multi-party

* context:
  * public
  * private
  * professional →  clarify with very clear examples, delimitations

* setting:
  * face-to-face
  * telephone
  * broadcast
  * online

* channels:
  * phonic-auditory
  * gestural-visual
  * graphic-visual

* Symmetry:
  * symmetric
  * asymmetric

For example, a spontaneous face-to-face conversation among friends could be described as:
 genre = conversation
with parameters such as
degree_of_spontaneity = spontaneous
number_of_participants = dialogic
context = private
setting = face-to-face
channels = phonic-auditory; gestural-visual.

## Implementation proposal
TBD. As a first step, it would be useful if a small group of treebank developers tried applying these guidelines to their data and shared the results with the community. Working through concrete examples will likely reveal ambiguities and help us refine the proposal before wider adoption.
The guidelines can be adopted gradually, depending on available time and resources:
Minimal effort: Simply rename existing metadata fields to match the proposed conventions.
Intermediate effort: Add metadata that is already available in the underlying corpus but not yet encoded in the treebank.
Extended effort: Introduce additional metadata where relevant and feasible.
The metadata can be encoded either directly in CoNLL-U or in an external file as outlined in [treebank structure](treebank_structure.html). The exact storage format is probably secondary to consistent naming and structure. 

@andidyer → propose a metadata.json template with overview of core metadata categories
> see also [treebank structure](treebank_structure.html)
