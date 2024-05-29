from ..codewar_problems.does_my_number_look_big_in_this import narcissistic, split, sum_array

def test_153_is_narcissisic():
    assert narcissistic(153) == True

def test_122_is_not_narcissistic():
    assert narcissistic(122) == False

def test_number_splitter():
    assert split(153) == [1, 5, 3]

def test_sum_array():
    assert sum_array([1, 2, 3]) == 6
    assert sum_array([1, 2, 3, 4, 5]) == 15
    assert sum([1, 2, 3, 4, 5]) == 15
