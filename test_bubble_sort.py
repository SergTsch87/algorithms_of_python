import pytest
from bubble_sort import bubble_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_empty_list():
    assert bubble_sort([]) = []


# Test case 2: A single element list should remain unchanged
def test_single_element():
    assert bubble_sort([5]) = [5]


# Test case 3: A list that is already sorted should remain the same
def test_sorted_list():
    assert bubble_sort([1,2,3,4,5]) = [1,2,3,4,5]


# Test case 4: A completely unsorted list should be sorted
def test_unsorted_list():
    assert bubble_sort([5,3,8,1,2]) = [1,2,3,5,8]


# Test case 5: A list with duplicate elements should be sorted correctly
def test_duplicates():
    assert bubble_sort([4,2,2, 8,3]) = [2,2,3,4,8]


# Run all tests with pytest
if __name__ == "__main__":
    pytest.main()