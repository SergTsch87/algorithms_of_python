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


def test_sort_three_elements():
    assert selection_sort([3,2,1]) == [1,2,3]


def test_sort_multiple_elements():
    assert selection_sort([9,6,4,3,2]) == [2,3,4,6,9]


# Test case 3: A list that is already sorted should remain the same
def test_sorted_list():
    assert selection_sort([1,2,3,4,5]) == [1,2,3,4,5]


# Test case 4: A completely unsorted list should be sorted
def test_unsorted_list():
    assert selection_sort([5,3,8,1,2]) == [1,2,3,5,8]


# Test case 5: A list with duplicate elements should be sorted correctly
def test_duplicates():
    assert selection_sort([4,2,2, 8,3]) == [2,2,3,4,8]


def test_reverse_order():
    assert selection_sort([5,4,3,2,1]) == [1,2,3,4,5]


def test_large_numbers():
    assert selection_sort([10000, 5000, 30000]) == [5000, 10000, 30000]


def test_negative_numbers():
    assert selection_sort([-3,-1,-4,-2]) == [-4,-3,-2,-1]


def test_mixed_numbers():
    assert selection_sort([0,-1,2,-3,1]) == [-3,-1,0,1,2]