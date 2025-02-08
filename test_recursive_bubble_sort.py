import pytest
from bubble_sort import recursive_bubble_sort   # Import the function (not implemented yet)
import time


# Test case 1: Sorting an empty list should return an empty list
def test_sort_empty():
    assert recursive_bubble_sort([]) == []


# Test case 2: A single element list should remain unchanged
def test_sort_single_element():
    assert recursive_bubble_sort([1]) == [1]
    # The function already returns the same list, so no change is needed.


def test_sort_two_elements():
    assert recursive_bubble_sort([2,1]) == [1,2]
    # Now we need logic to sort two elements.


def test_sort_three_elements():
    assert recursive_bubble_sort([3,2,1]) == [1,2,3]
