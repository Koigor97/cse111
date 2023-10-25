from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)
        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners
    # 2. Test the plural determiners.
        plural_determiners = ["some", "many", "the"]
    # This loop will repeat the statements inside it 4 times.
        word = get_determiner(2)
        assert word in plural_determiners


def test_get_noun():
    single_noun = ["bird", "boy", "car", "cat", "child",
                   "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        word = get_noun(1)
        assert word in single_noun

        plural_nouns = ["birds", "boys", "cars", "cats",
                        "children", "dogs", "girls", "men", "rabbits", "women"]
        word2 = get_noun(2)
        assert word2 in plural_nouns


def test_get_verb():
    past_tense = ["drank", "ate", "grew", "laughed",
                  "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb("past")
        assert word in past_tense

        present_singular = ["drinks", "eats", "grows", "laughs",
                            "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        word2 = get_verb("present")
        assert word2 in present_singular

        present_plural = ["drink", "eat", "grow", "laugh",
                          "think", "run", "sleep", "talk", "walk", "write"]
        word3 = get_verb("present", 2)
        assert word3 in present_plural

        future_tense = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep",
                        "will talk", "will walk", "will write"]
        word4 = get_verb("future")
        assert word4 in future_tense


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on",
                    "onto", "out", "over", "past", "to", "under", "with", "without"]
    word = get_preposition()
    for _ in range(4):
        assert word in prepositions


def test_prepositional_phrase():
    the_phrase = get_prepositional_phrase().split()
    for _ in range(4):
        assert the_phrase[0] in the_phrase
        assert the_phrase[1] in the_phrase
        assert the_phrase[2] in the_phrase


pytest.main(["-v", "--tb=line", "-rN", __file__])
