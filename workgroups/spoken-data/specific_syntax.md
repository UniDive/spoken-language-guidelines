---
layout: base
title:  'Other Constructions'
udver: '2'
---

# Other Constructions

This section of the [syntax overview](syntax.html) contains detailed discussion of particular linguistic constructions that fall outside (or cut across) the main categories of simple clauses, complex clauses, and nominal phrases.

## Paratactic Constructions

In spoken data, the `parataxis` deprel is less used as the two clauses, which are not otherwise syntactically connected, should be split into two different maximal units (i.e., sentences).

We therefore suggest to restrict the use of parataxis to these specific cases:

### Insertions

In the case of reported speech, when the speech verb is not the main predicate.
In right branching languages, this happens often when the segment starts with reported speech, and the speech verb appears later on in the sentence (e.g., "Don't do that -- she said").

In French for instance, this is easy to detect as the speech verb appears with inversion (e.g., "Ne fais pas ça, a-t-elle dit" 'Don't do that -- she said')

Other examples:
- If you do that, she said, you won't be able to stay

These are marked with `parataxis:insert`

### Parentheticals

A parenthesis is a clause that could be uttered alone but interrupts another maximal unit. It is generally a comment on the whole sentence.

Example:
- It. Partiva da, come si chiama, via Porrettana 'He was leaving from, what is the name again, via Porrettana'

These are marked with `parataxis:parenth`

### Restarts

A false start is considered as a restart if there is repair that comes after it. For this reason it is not considered an autonomous unit and therefore it is kept in the same sentence of its repair.

Examples:
- In peggio perchè non ... prima c'era più sicurezza 'Worse because it's not ... it was safer before'
- what did you just -- which line will you draw

If there is no repair, the false start is a separate sentence.

## Tag questions

NOTE: difference from guidelines

We suggest to use `discourse` for tag questions such as _isn't it?_ or _haven't you?_, as these do not constitute autonomous units.

~~~ sdparse
It 's not me , is it ?
discourse(me, is)
punct(is, ,)
~~~

## Feedback words

NOTE: difference from guidelines

In a sentence starting with a feedback word such as _yes_ or _no_ and continuing with a main clause, we take the feedback to be the root of the sentence and attach the rest of the clause (other feedbacks and the *main* clause) to the first feedback with a `conj` relation:

~~~ sdparse
yes , we should apply for membership .
conj(yes, apply)
~~~
