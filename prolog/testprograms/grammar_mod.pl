
sentence(Number, sentence(NP, VP)) -->
	noun_phrase(Number, NP),
	verb_phrase(Number, VP).

verb_phrase(Number, verb_phrase(Verb, NP)) -->
	verb(Number, Verb),
	noun_phrase(Number1, NP).
noun_phrase(Number, noun_phrase(Det, Noun)) -->
	determiner(Det),
	noun(Number, Noun).
verb(singular,verb(hates)) --> [hates].
verb(plural,verb(hate)) --> [hate].
determiner(determiner(the)) --> [the].
noun(singular, noun(cat)) --> [cat].
noun(plural, noun(cats)) --> [cats].
noun(singular, noun(mouse)) --> [mouse].
noun(plural, noun(mice)) --> [mice].