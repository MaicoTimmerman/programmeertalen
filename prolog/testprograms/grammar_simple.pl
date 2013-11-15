/* grammar simple */
sentence --> noun_phrase, verb_phrase.
verb_phrase --> verb, noun_phrase.
noun_phrase --> determiner, noun.
determiner --> [a].
determiner --> [the].
noun --> [cat].
noun --> [cats].
noun --> [mouse].
noun --> [mice].
verb --> [scare].
verb --> [scares].
verb --> [hate].
verb --> [hates].
