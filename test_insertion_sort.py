import pytest
from insertion_sort import insertion_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_empty_list():
    assert insertion_sort([]) == []


# Test case 2: A single element list should remain unchanged
def test_single_element():
    assert insertion_sort([5]) == [5]


# Test case 2: A single element list should remain unchanged
def test_sort_single_element():
    assert insertion_sort([1]) == [1]
    # The function already returns the same list, so no change is needed.


def test_sort_two_elements():
    assert insertion_sort([2,1]) == [1,2]
    # Now we need logic to sort two elements.


def test_sort_three_elements():
    assert insertion_sort([3,2,1]) == [1,2,3]


# Test case 3: A list that is already sorted should remain the same
def test_sorted_list():
    assert insertion_sort([1,2,3,4,5]) == [1,2,3,4,5]