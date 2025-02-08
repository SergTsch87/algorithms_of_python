import pytest
from selection_sort import recursive_selection_sort


# Test case 1: Sorting an empty list should return an empty list
def test_sort_empty():
    assert recursive_selection_sort([]) == []


# Test case 2: Sorting an empty list should return an empty list
def test_single_element():
    assert recursive_selection_sort([2]) == [2]


# Test case 3: A list that is already sorted should remain the same
def test_sort_two_elements():
    assert recursive_selection_sort([9,4]) == [4,9]