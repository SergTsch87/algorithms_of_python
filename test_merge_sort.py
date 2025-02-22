import pytest
from merge_sort import merge_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_empty_list():
    assert merge_sort([]) == []


# Test case 2: A single element list should remain unchanged
def test_single_element():
    assert merge_sort([5]) == [5]


def test_sort_two_elements():
    assert merge_sort([2,1]) == [1,2]
    # Now we need logic to sort two elements.


def main():
    pass


if __name__ == "__main__":
    pytest.main()