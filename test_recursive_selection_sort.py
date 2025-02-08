import pytest
from selection_sort import recursive_selection_sort


# Test case 1: Sorting an empty list should return an empty list
def test_sort_empty():
    assert recursive_selection_sort([]) == []