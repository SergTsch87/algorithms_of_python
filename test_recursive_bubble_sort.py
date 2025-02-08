import pytest
from bubble_sort import recursive_bubble_sort   # Import the function (not implemented yet)
import time


# Test case 1: Sorting an empty list should return an empty list
def test_sort_empty():
    assert recursive_bubble_sort([]) == []