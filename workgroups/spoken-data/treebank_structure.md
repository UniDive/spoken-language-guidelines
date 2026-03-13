---
layout: base
title:  'Treebank structure'
udver: '2'
---

# Treebank structure

## Problem identification

Speech-related metadata in UD treebanks is currently encoded in heterogeneous and inconsistent ways. This affects both spoken-only and mixed-modality treebanks. As a result, it is often difficult to reliably identify spoken data within mixed-modality resources and to retrieve specific types of speech (e.g. spontaneous vs. prepared, public vs. private, monologue vs. dialogue), or speaker-related information (e.g. age, gender, education). Harmonization is therefore essential to enable efficient retrieval of relevant spoken data within and across treebanks and thus advance the underexplored field of spoken grammar research.

## Current situation

Variation in the encoding of speech-related metadata in UD treebanks (including differences in the type of information recorded and its structural placement within the CoNLL-U format) has been documented in previous work (Dobrovoljc 2022), which recommended systematically recording all available speech-specific metadata in line with existing treebank practices and recommendations proposed by Kahane et al. 2021. The results of the UniDive survey among spoken UD treebank developers (see survey results), carried out at the end of 2024, and the automatically extracted metadata inventory (see Grew-match table and spreadsheet) confirm that such heterogeneity persists. For example, not all mixed-modality treebanks explicitly mark spoken material, and among spoken-only treebanks only 72% provide additional speech-specific metadata, which, when present, varies considerably in type, granularity, and encoding conventions.

More broadly, questions concerning the encoding of metadata in CoNLL-U have also been discussed within the UD community (see issues #1135 and #1146), highlighting the need for clearer and more consistent practices beyond speech-specific data only.

## Proposal for cross-linguistic harmonization

### Main principles
When preparing a spoken UD treebank, two core principles should guide the treatment of metadata: include all available corpus metadata rather than discarding it during conversion to .conllu, and adopt shared naming conventions to avoid reinventing feature names that have already been used in existing treebanks.

### Core metadata categories and naming
Below, we list the most recurrent speech-related metadata categories and propose their standardized naming. In addition to corpus-level information (to be documented in the README), we distinguish four levels at which such metadata may apply: document level (information that holds for an entire recording or interaction, e.g. genre or links to audio recordings), speaker level (information describing individual participants, e.g. age or education),  sentence level (information that applies to individual utterances, e.g. speaker identification, alignment data, or translations), and token level (information that applies to individual words, e.g. language switching or word-level audio alignment).

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


### Metadata placement and encoding
While token- and sentence-level information should remain encoded directly in the CoNLL-U files (in the MISC column for tokens and in # comment lines for sentences), we propose storing document-level and speaker-level metadata, such as detailed information on speech events and speakers, in an external metadata file to avoid redundancy, improve readability, and enable consistent maintenance.

Concretely, this takes the form of a metadata.json file placed in a designated not-to-release folder, containing entries indexed by stable identifiers (e.g. document_id and speaker_id) that are referenced in the CoNLL-U files through those identifiers, as in the examples below.

if there is a general template generated for a new treebank, the creation of metadata.json could be a default feature -- to discuss with Dan Zeman

1 - Minimal metadata.json example (see also here):

.conllu file
metadata.json




2- Example of metadata.json with detailed speech event type information:
```
{
  "sample1": {
    "speaker_ids": ["G0125"],
    "sample_id": "G0125",
    "sound_url": "G0125.mp3",
    "description": "Face-to-face conversation among friends",
    "genre": "conversation",
    "parameters": {<-- more practical if omitted
      "degree_of_spontaneity": "unplanned",
      "number_of_participants": "dialogic",
      "context": "private",
      "setting": "face-to-face",
      "channels": ["phonic-auditory", "gestural-visual"],
      "symmetry": "symmetric"
    }
  },
  "speaker_id": {
    "G0125": {
      "speaker_age": "XXX",
      "speaker_birthplace": "XXX",
      "speaker_education": "XXX",
      "speaker_naija_competency": "XXX",
      "speaker_primary_other_language": "XXX",
      "speaker_residence": "XXX",
      "speaker_sex": "XXX",
      "speaker_gender": "XXX"
    }
  }
}



—------------

{
  "example": {
    "description": "Face-to-face conversation among friends",
    "genre": "conversation",
    "parameters": {
      "degree_of_spontaneity": "unplanned",
      "number_of_participants": "dialogic",
      "context": "private",
      "setting": "face-to-face",
      "channels": ["phonic-auditory", "gestural-visual"],
      "symmetry": "symmetric"
    },
    "sample_id": "G0125",
    "speaker_ids": ["G0125"]
  },
  "sample_id": {
    "SAMPLE1": {
      "sound_url": "EX1.mp3"
    }
  },
  "speaker_id": {
    "G0125": {
      "speaker_age": "XXX",
      "speaker_birthplace": "XXX",
      "speaker_education": "XXX",
      "speaker_naija_competency": "XXX",
      "speaker_primary_other_language": "XXX",
      "speaker_residence": "XXX",
      "speaker_sex": "XXX",
      "speaker_gender": "XXX"
    }
  }
}
```

## Implementation proposal
TBD. As a first step, it would be useful if a small group of treebank developers tried applying these guidelines to their data and shared the results with the community. Working through concrete examples will likely reveal ambiguities and help us refine the proposal before wider adoption.
The guidelines can be adopted gradually, depending on available time and resources:
Minimal effort: Simply rename existing metadata fields to match the proposed conventions.
Intermediate effort: Add metadata that is already available in the underlying corpus but not yet encoded in the treebank.
Extended effort: Introduce additional metadata where relevant and feasible.
The metadata can be encoded either directly in CoNLL-U or in an external file as outlined above. The exact storage format is probably secondary to consistent naming and structure. Scripts could also be proposed to help with conllu2json and json2conllu conversions.

@andidyer → propose a metadata.json template with overview of core metadata categories
@bguil → pull requests
