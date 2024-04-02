from ..codewar_problems.sum_of_nums_without_highest_or_lowest import get_sum_from_list

def test_empty_list():
    assert get_sum_from_list([]) == 0
    assert get_sum_from_list(None) == 0

def test_lists_with_only_one_element():
    assert get_sum_from_list([1]) == 0

def test_lists_with_only_two_elements():
    assert get_sum_from_list([3, 5]) == 0
    assert get_sum_from_list([-3, -5]) == 0

def test_with_three_elements():
    assert get_sum_from_list([1, 2, 3]) == 2

def test_with_four_or_more_elements():
    assert get_sum_from_list([1, 2, 3, 4]) == 5
    assert get_sum_from_list([10, 20, 30, 40, 50]) == 90

def test_with_unsorted_lists_with_more_than_three_elements():
    assert get_sum_from_list([2, 4, 3, 1]) == 5