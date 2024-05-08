from ..codewar_problems.stop_spinning_my_words import spin_words

def test_string_no_words_longer_than_five_letters():
    assert spin_words("this is a test") == "this is a test"

def test_a_different_string():
    assert spin_words("this is also a test") == "this is also a test"

def test_string_with_one_word_longer_than_five_chars():
    assert spin_words("i have one longer word") == "i have one regnol word"