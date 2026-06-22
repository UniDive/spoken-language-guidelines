---
layout: base
title:  'Metadata harmonisation'
udver: '2'
---

# Metadata harmonisation

## Problem identification

Speech-related metadata in UD treebanks is currently encoded in heterogeneous and inconsistent ways. This affects both spoken-only and mixed-modality treebanks. As a result, it is often difficult to reliably identify spoken data within mixed-modality resources and to retrieve specific types of speech (e.g. spontaneous vs. prepared, public vs. private, monologue vs. dialogue), or speaker-related information (e.g. age, gender, education). Harmonization is therefore essential to enable efficient retrieval of relevant spoken data within and across treebanks and thus advance the underexplored field of spoken grammar research.

## Current situation

Variation in the encoding of speech-related metadata in UD treebanks—both in the information recorded and in how it is represented in CoNLL-U—has already been documented by [Dobrovoljc (2022)](https://aclanthology.org/2022.lrec-1.191/), who recommends systematically recording all available speech-specific metadata in line with prevailing treebank practices and the initial recommendations proposed by [Kahane et al. (2021)](https://aclanthology.org/2021.tlt-1.4/). The results of the [UniDive spoken data annotation survey](https://docs.google.com/forms/d/e/1FAIpQLSerAtOMoRmEiO3o99Qv0tMio8m0uriNUhGu-aoKnc29BVUcNg/viewform) among spoken UD treebank developers ([results overview](https://docs.google.com/presentation/d/1KMZbS_dTAlsL-IOb6YDL8gw25_-NW4SPbF-xdbclHMo/edit?slide=id.g2af43d13921_0_95#slide=id.g2af43d13921_0_95)), carried out at the end of 2024, and the automatically extracted metadata inventory (see [overview table](https://tables.grew.fr/?data=SP_meta/META) in Grew) confirm that such heterogeneity persists. For example, not all mixed-modality treebanks explicitly mark spoken material, and among spoken-only treebanks only 72% provide additional speech-specific metadata, which, when present, varies considerably in type, granularity, and encoding conventions.

More broadly, questions concerning the encoding of metadata in CoNLL-U have also been discussed within the UD community (see issues [#1135](https://github.com/UniversalDependencies/docs/issues/1135) and [#1146](https://github.com/UniversalDependencies/docs/issues/1146), highlighting the need for clearer and more consistent practices beyond speech-specific data only.

## Our proposal for cross-linguistic harmonization

### Main principles
When preparing a spoken UD treebank, two core principles should guide the treatment of metadata: (1) **preserve all available metadata** associated with the recordings rather than discarding it during conversion to .conllu, and (2) **adopt shared naming conventions** to avoid reinventing feature names that have already been used in existing treebanks.

### Core metadata categories and naming
Below, we list the most recurrent speech-related metadata categories and propose their standardized naming. In addition to corpus-level information, such as the authors or data collection principles (to be documented in the treebank's README), we distinguish four levels at which such metadata may apply: document level (information that holds for an entire recording or interaction, e.g. genre or links to audio recordings), speaker level (information describing individual participants, e.g. age or education),  sentence level (information that applies to individual utterances, e.g. speaker identification, alignment data, or translations), and token level (information that applies to individual words, e.g. language switching or word-level audio alignment).

TODO @all: Please revise the proposed namings below and think whether any other types of core metadata should be added to this core list (previously mentioned in discussions below but not retained yet: addressee_id, participant_id).

add also alternative values where applicable, e.g. modality=written, modality=signed

* Document-level:
  * modality=spoken: marking spoken data in mixed-modality treebanks
  * document_id: unique identifier of the speech event
  * media_url: link to audio or video recording associated with the speech event - general agreement for more type-specific naming, e.g. sound_url, video_url, manuscript_url
  * genre: descriptive label of the speech event (e.g. conversation, interview). For a more detailed set of parameters used to describe speech events, see 3.3.3.

* Speaker-level
  * speaker_age: age or age range of the speaker.
  * speaker_gender: gender of the speaker (if available).
  * speaker_education: highest completed education level.
  * speaker_residence: place of residence of the speaker

* Sentence-level:
  * sent_id: unique identifier of the speech event sentence
  * speaker_id: unique identifier of the speaker producing the utterance
  * sound_alignment_begin: start timestamp of the sentence in the recording (ms)
  * sound_alignment_end: end timestamp of the sentence in the recording (in ms)
  * duration: duration of the sentence in milliseconds
  * text_[type of transcription]: transcription of a different type (e.g text_orthographic, text_phonetic, text_morphemic, text_transliteration, text_conversationanalysis, text_macrosyntax)
  * text_[ISO]: translation into another language (in ISO code)
  * speaker_role: e.g. interviewer/interviewee; professor/student

* Token-level:
  * Lang: language identifier for code-switched tokens.
  * OrigLang: original language of borrowed or inserted tokens
  * WordAlignmentBegin: start timestamp of a token in the recording (milliseconds)
  * WordAlignmentEnd: end timestamp of a token in the recording (milliseconds).

rename word to token + casing (see Ludovica’s comment)

Additional metadata may be encoded flexibly; however, developers are encouraged to first verify whether a suitable solution already exists in current treebanks (see Grew-match inventory of metadata found in existing spoken data treebanks).

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
