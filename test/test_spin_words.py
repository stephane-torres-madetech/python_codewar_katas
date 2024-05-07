from ..codewar_problems.stop_spinning_my_words import spin_words

def test_string_no_words_longer_than_five_letters():
    assert spin_words("this is a test") == "this is a test"