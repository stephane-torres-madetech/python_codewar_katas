from ..codewar_problems.string_ends_with import string_ends_with

def test_abc_ends_with_bc():
    assert string_ends_with("abc", "bc") == True

def test_abc_does_not_end_with_d():
    assert string_ends_with("abc", "d") == False

