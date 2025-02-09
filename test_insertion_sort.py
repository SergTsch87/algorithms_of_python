import pytest
from insertion_sort import insertion_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_empty_list():
    assert insertion_sort([]) == []