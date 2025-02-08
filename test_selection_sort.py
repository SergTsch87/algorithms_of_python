import pytest
from selection_sort import selection_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_sort_empty():
    assert selection_sort([]) == []


# Test case 2: Sorting an empty list should return an empty list
def test_single_element():
    assert selection_sort([2]) == [2]


# Test case 3: A list that is already sorted should remain the same
def test_sort_two_elements():
    assert selection_sort([9,4]) == [4,9]