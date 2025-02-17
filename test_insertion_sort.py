import pytest
from insertion_sort import insertion_sort   # Import the function (not implemented yet)


# # Test case 1: Sorting an empty list should return an empty list
# def test_empty_list():
#     assert insertion_sort([]) == []


# # Test case 2: A single element list should remain unchanged
# def test_single_element():
#     assert insertion_sort([5]) == [5]


# # Test case 2: A single element list should remain unchanged
# def test_sort_single_element():
#     assert insertion_sort([1]) == [1]
#     # The function already returns the same list, so no change is needed.


# def test_sort_two_elements():
#     assert insertion_sort([2,1]) == [1,2]
#     # Now we need logic to sort two elements.


# def test_sort_three_elements():
#     assert insertion_sort([3,2,1]) == [1,2,3]


# # Test case 3: A list that is already sorted should remain the same
# def test_sorted_list():
#     assert insertion_sort([1,2,3,4,5]) == [1,2,3,4,5]


# # Test case 4: A completely unsorted list should be sorted
# def test_unsorted_list():
#     assert insertion_sort([5,3,8,1,2]) == [1,2,3,5,8]


# # Test case 5: A list with duplicate elements should be sorted correctly
# def test_duplicates():
#     assert insertion_sort([4,2,2, 8,3]) == [2,2,3,4,8]


# def test_reverse_order():
#     assert insertion_sort([5,4,3,2,1]) == [1,2,3,4,5]


# def test_large_numbers():
#     assert insertion_sort([10000, 5000, 30000]) == [5000, 10000, 30000]


# def test_negative_numbers():
#     assert insertion_sort([-3,-1,-4,-2]) == [-4,-3,-2,-1]


# def test_mixed_numbers():
#     assert insertion_sort([0,-1,2,-3,1]) == [-3,-1,0,1,2]
