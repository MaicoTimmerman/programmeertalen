sentence - -> noun_phrase, verb_phrase.
verb_phrase - -> verb, noun_phrase.
noun_phrase - -> determiner, noun.
determiner - -> [a].
determiner - -> [the].
noun - -> [cat].
noun - -> [mouse].
verb - -> [scares].
verb - -> [hates].
/*
noun --> [cats].
noun --> [mice].
verb --> [scare].
verb --> [hate].
*/

/*
noun_phrase(Number).
verb_phrase(Number).

sentence(Number) - -> noun_phrase(Number), verb_phrase(Number).
verb_phrase(Number) --> verb(Number), noun_phrase(Number).
noun_phrase(Number) --> determiner(Number), noun(Number).
noun(singular) --> mouse.
noun(plural) - -> mice.

*/

/*
noun_phrase(determiner(the), noun(cat)).

Genereer parse trees bijvoorbeeld met

noun_phrase(DetTree, NounTree).

noun_phrase(noun_phrase(DetTree,NounTree)) -- >
	determiner(DetTree), noun(NounTree).
*/

/*
sentence(Number, sentence(NP, VP)) -->
	noun_phrase(Number, NP),
	verb_phrase(Number, VP).

verb_phrase(Number, verb_phrase(Verb, NP)) -->
	verb(Number, Verb),
	nount_phrase(Number, NP).
noun_phrase(Number, noun_phrase(Det, Noun)) - ->
	determiner(Det),
	noun(Number, Noun).
determiner(determiner(the)) - -> [the].
noun(singular, noun(cat)) - -> [cat].
noun(plural, noun(cats)) - -> [cats].
*/

