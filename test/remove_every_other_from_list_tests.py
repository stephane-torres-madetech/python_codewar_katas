from ..codewar_problems.remove_every_other_from_list import remove_every_other

def test_removes_every_other_from_list():
    assert remove_every_other([1, 2]) == [1]
    assert remove_every_other([1, 2, 3]) == [1, 3]
    assert remove_every_other([2, 3, 4, 5, 6]) == [2, 4, 6]
    assert remove_every_other(['Hi', 'bye', 'hello', 'ciao']) == ['Hi', 'hello']
    # assert remove_every_other([2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]