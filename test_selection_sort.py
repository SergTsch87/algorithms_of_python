import pytest
from selection_sort import selection_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_sort_empty():
    assert selection_sort([]) == []