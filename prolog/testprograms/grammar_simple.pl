/* grammar simple */
sentence(Number) --> noun_phrase(Number), verb_phrase(Number).
verb_phrase(Number) --> verb(Number), noun_phrase(Number).
noun_phrase(Number) --> determiner(Number), noun(Number).
determiner(singular) --> [a].
determiner(singular) --> [the].
/* nouns */
noun(plural) --> [cats].
noun(plural) --> [mice].
noun(singular) --> [cat].
noun(singular) --> [mouse].
/* verbs */
verb(plural) --> [scares].
verb(plural) --> [hates].
verb(singular) --> [hate].
verb(singular) --> [scare].
