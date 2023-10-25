from random import choice


def main():
    for _ in range(6):
        if _ == 3 or _ == 4 or _ == 5:
            determiner = get_determiner(2)
            noun = get_noun(2)
            prepositional_phrase = get_prepositional_phrase(2)
            if _ == 3:
                verb = get_verb("present")
            elif _ == 4:
                verb = get_verb("past")
            else:
                verb = get_verb("future")

        else:
            determiner = get_determiner()
            noun = get_noun()
            prepositional_phrase = get_prepositional_phrase()
            if _ == 0:
                verb = get_verb("present")
            elif _ == 1:
                verb = get_verb("past")
            else:
                verb = get_verb("future")


        print(f"{determiner} {noun} {verb} {prepositional_phrase}")


def get_prepositional_phrase(quantity=1):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or plural.
    Return: a prepositional phrase.
    """
    the_preposition = get_preposition()
    the_determiner = get_determiner(quantity)
    the_noun = get_noun(quantity)

    return f"{the_preposition} {the_determiner} {the_noun}"


def get_determiner(quantity=1):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise, this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise, this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = choice(words)
    return word


def get_noun(quantity=1):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        singular = choice(["bird", "boy", "car", "cat", "child",
                          "dog", "girl", "man", "rabbit", "woman"])
        return singular
    else:
        plural = choice(["birds", "boys", "cars", "cats", "children", "dogs",
                         "girls", "men", "rabbits", "women"])
        return plural


def get_verb(tense, quantity=1):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        past_tense = choice(["drank", "ate", "grew", "laughed", "thought",
                             "ran", "slept", "talked", "walked", "wrote"])
        return past_tense

    elif quantity == 1 and tense == "present":
        present_tense = choice(["drinks", "eats", "grows", "laughs", "thinks",
                                "runs", "sleeps", "talks", "walks", "writes"])
        return present_tense

    elif quantity != 1 and tense == "present":
        present_plural = choice(["drink", "eat", "grow", "laugh", "think",
                                 "run", "sleep", "talk", "walk", "write"])
        return present_plural

    elif tense == "future":
        future_tense = choice(["will drink", "will eat", "will grow", "will laugh",
                               "will think", "will run", "will sleep", "will talk",
                               "will walk", "will write"])
        return future_tense


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on",
                    "onto", "out", "over",  "past", "to", "under", "with", "without"]
    return choice(prepositions)


if __name__ == "__main__":
    main()
