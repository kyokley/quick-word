from src.quick_word.words import wordlist, words


def test_words():
    test_num_words = 3
    output_words = words(test_num_words)
    split_words = list(output_words)

    assert len(split_words) == test_num_words
    for word in split_words:
        assert word in wordlist
