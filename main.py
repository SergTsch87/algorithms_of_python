#!usr/bin/env

# import random as rnd
# import math
from itertools import accumulate


# Iterative version
def bubble_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        swapped = False   # Track swaps
        for j in range(len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   # if no swaps, array is sorted
            break
    return arr


# Recursive version
def bubble_sort_recursive(arr, n = None):
    if n is None:
        n = len(arr)

    swapped = False
    # count = 0

    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            # count += 1
        
    if not swapped:
        return arr
    # if count == 0:
    #     return arr
        
    return bubble_sort_recursive(arr, n - 1)


def selection_sort(arr, len_arr):
    min_pos = 0
    for i in range(len_arr - 1):
        min_pos = i
        for j in range(i + 1, len_arr):
            if  arr[j] < arr[min_pos]:
                min_pos = j
        if min_pos != i:
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr


# 1) Sum of Array Elements
# Task: Write a function that takes a list of numbers and returns the sum of all elements.
# Goal: Understand simple iteration over an array.
def get_sum_list(my_list: int) -> int:
    sum_nums = 0
    for _ in my_list:
        sum_nums += _
    return sum_nums
    # return sum(my_list)


# 2) Find the Maximum and Minimum in an Array
# Task: Given a list, return the smallest and largest number.
# Goal: Track and update variables inside a loop.
def get_max_min_arr(arr: list[int]) -> list[int]:
    if not arr:
        raise ValueError("Array cannot be empty")
    min_arr, max_arr = arr[0], arr[0]
    for num in arr:
        if num > max_arr:
            max_arr = num
        elif num < min_arr:
            min_arr = num

    return [min_arr, max_arr]


# 3) Reverse an Array (Without Using [::-1])
# Task: Implement a function that reverses a list in place using a loop.
# Goal: Work with indices and swapping values.
def get_reverse_an_arr(arr: list[int]) -> list[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr
    
    # temp_arr = []
    # # for num in arr:
    # #     temp_arr = [num] + temp_arr
    # for num in range(len(arr) - 1, -1, -1):
    #     temp_arr.append(arr[num])

    # return temp_arr


# 4) Count Occurrences of an Element
# Task: Given a list and a target value, return the number of times it appears.
# Goal: Use conditional checks within iterations
def get_count_elem(arr: list[int], find_num: int) -> list[int]:
    if not arr:
        raise ValueError("Array cannot be empty")
    
    # count = 0
    # for num in arr:
    #     if num == find_num:
    #         count += 1

    # return count

    # Pythonic ways:
    # return arr.count(find_num)
    return sum(1 for num in arr if num == find_num)


# 5) Prefix Sum of an Array
# Task: Given an array, return a new array where each element at index i is the sum of all elements from 0 to i.
# Goal: Track cumulative changes across iterations.
def get_prefix_sum(arr: list[int]) -> list[int]:
    if not arr:
        raise ValueError('Array cannot be empty')
    
    return list(accumulate(arr))


# 6) Shift Elements in an Array
# Task: Given an array, shift all elements to the right by one position, with the last element moving to the first position.
# Goal: Manipulate indices and track changes.
def shift_elems_in_arr(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    
    # last_elem = arr[- 1]

    # for i in range(len(arr) - 1, 0, -1):
    #     # print(f'i == {i}, arr[i] == {arr[i]}, arr[i-1] == {arr[i-1]}')
    #     arr[i] = arr[i - 1]

    # arr[0] = last_elem
    
    # return arr
    return [arr[-1]] + arr[:-1]  # more Pythonic way to perform the shift is by using slicing


# 7) Find the Index of a Target Element
# Task: Given a list and a target, return the index of the first occurrence (or -1 if not found).
# Goal: Distinguish between index-based and value-based iteration.
def find_ind_of_target_elem(arr, num):
    # # index-based iteration
    # for i in range(len(arr)):
    #     if arr[i] == num:
    #         return i

    # # value-based iteration
    # index = 0
    # for item in arr:
    #     if item == num:
    #         return index
    #     index += 1

    # for index, val in enumerate(arr):
    #     if val == num:
    #         return index

    # return -1

    return arr.index(num) if num in arr else -1  # one-liner using .index() (but it raises an exception if num is not found)


# 8) Find Duplicates in an Array
# Task: Return a list of elements that appear more than once.
# Goal: Use nested loops or a dictionary for frequency counting.
def find_duplicates_in_arr(arr: list[int]) -> list[int]:
    # # 1) with nested loops:
    # new_list = []
    # count = 0
    # temp_elem = 0
    # for i, val in enumerate(arr):
    #     if val not in new_list:
    #         temp_elem = val
    #         count += 1
    #         for j, item in enumerate(arr):
    #             if j > i:
    #                 if item == temp_elem:
    #                     new_list.append(temp_elem)
    #                     break
    # return new_list

    # # 2) with dictionary for frequency counting:
    # dict_for_freq_count = {}
    # new_list = []
    # # count = 0
    # # temp_elem = 0
    # for i, val in enumerate(arr):
    #     if val not in dict_for_freq_count.values():
    #         dict_for_freq_count[val] = 1
    #         # temp_elem = val
    #         # count += 1
    #         for j, item in enumerate(arr):
    #             if j > i:
    #                 if item in dict_for_freq_count.keys():
    #                     new_list.append(val)
    #                     break
    # return new_list
    # [6, 3, 4, 2, 5]

#     3) Optimal Approach: Single Pass Dictionary (O(n))
# The best way to find duplicates is using a single pass dictionary to count occurrences.
    if not arr:
        return arr
    
    freq_count = {}
    duplicates = set()

    for val in arr:
        if val in freq_count:
            duplicates.add(val)   # Only add if already seen
        else:
            freq_count[val] = 1   # Mark as seen
    
    return list(duplicates)


# 9) Move All Zeros to the End
# Task: Given [0, 1, 0, 3, 12], return [1, 3, 12, 0, 0].
# Goal: Differentiate between keeping track of indices and values while modifying an array.
def move_all_zeros_to_the_end(arr):
    # # 1) first way
    # new_list = []
    # count = 0
    # for num in arr:
    #     if num == 0:
    #         count += 1
    #     else:
    #         new_list.append(num)
    
    # new_list += [0 for _ in range(count)]
    # return new_list

    # # # 2) second way
    # # for ind, num in enumerate(arr):
    # #     if num == 0:
    # #         del arr[ind]
    # #         arr.append(0)
        
    # # return arr

    # # 3) third way
    # return [num for num in arr if num != 0] + [0] * arr.count(0)

    # 4) forth way
    #     Best Approach: Two Pointers (In-Place, O(n))
    #     Efficient and Modifies in Place Without Extra Memory
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1

    return arr


# 10) Two Pointers Technique: Find Pair with Target Sum
# Task: Given a sorted list and a target sum, return the indices of two numbers that add up to the target.
# Goal: Use two different indices moving in opposite directions.
def find_pair_with_target_sum(sorted_list: list[int], target_sum: int) -> tuple[int, int] | None:
    # # 1) 1st way: Bad, ineficient
    # # Issue 2:
    # # Inefficient Tracking of "Bad Numbers"
    # list_bad_nums = []
    # for i in range(len(sorted_list)):
    #     if sorted_list[i] not in list_bad_nums:
            
    #         # Issue 1:
    #         # nefficient Search with Nested Loops → O(n^2) Time Complexity
    #         if (target_sum - sorted_list[i]) in sorted_list[i:]:                
    #             # find index (j) of num (target_sum - sorted_list[i])
    #             for index, val in enumerate(sorted_list):
    #                 if val == (target_sum - sorted_list[i]):
    #                     j = index
                
    #             return i, j
            
    #         else:
    #             list_bad_nums += [sorted_list[i]]
    #             list_bad_nums += [target_sum - sorted_list[i]]
        
    # return None, None

    # 2) 2nd way
    # find_second_num = -1
    # tmp_val = 0
    # for ind, val in enumerate(sorted_list):
    #     if (target_sum - val) in sorted_list and tmp_val == 0:
    #         i = ind
    #         find_second_num = target_sum - val
    #         tmp_val += 1
    #     elif val == find_second_num:
    #         j = ind
    #         return i, j
    
    # return None, None

    # # 3) 3d way
    # left, right = 0, len(sorted_list) - 1

    # while left < right:
    #     current_sum = sorted_list[left] + sorted_list[right]

    #     if current_sum == target_sum:
    #         return left, right  # Found the pair
        
    #     elif current_sum < target_sum:
    #         left += 1  # Move left pointer to increase the sum

    #     else:
    #         right -= 1  # Move right pointer to decrease the sum

    # return None, None  # No valid pair found


    # 4) 4th way
    seen = {}  # Dictionary to store {value: index}

    for i, val in enumerate(sorted_list):
        complement = target_sum - val
        if complement in seen:
            return seen[complement], i  # Found the pair
        
        seen[val] = i  # Store index of the current number

    return None  # No valid pair found


# Задачі на закріплення попередніх технік
# 1) Sliding Window: Find Maximum Sum of a Subarray of Size K
# Task: Given an array and an integer k, find the maximum sum of any contiguous subarray of size k.
# Goal: Learn the sliding window technique to avoid redundant calculations inside loops.
def find_max_sum_of_a_subarr_of_sz_k(arr, k):
    # max_sum = 0
    # sum_current = 0
    # for i in range(len(arr)):
    #     if i < k - 1:
    #         sum_current += arr[i]
    #     elif i == k - 1:
    #         sum_current += arr[i]
    #         max_sum = sum_current
    #     elif i >= k:
    #         sum_current += (arr[i] - arr[i - k])
    #         if sum_current > max_sum:
    #             max_sum = sum_current
    # return max_sum
    
    # if k > len(arr):
    #     return 'number k more then len(arr)'
    # elif k <= 0:
    #     return 'number k less/equal then 0'
    # else:
    #     sum_current = sum(arr[:k])
    #     max_sum = sum_current

    #     for i in range(k, len(arr)):
    #         sum_current += (arr[i] - arr[i - k])
    #         if sum_current > max_sum:
    #             max_sum = sum_current

    #     return max_sum

    if not arr or k <= 0 or k > len(arr):
        return 0  # Handle edge cases

    sum_current = sum(arr[:k])
    max_sum = sum_current

    for i in range(k, len(arr)):
        sum_current += arr[i] - arr[i - k]   # Slide the window
        max_sum = max(max_sum, sum_current)  # Update max_sum if needed

    return max_sum


# 2) 2️⃣ Remove Duplicates from a Sorted Array (In-Place)
# Task: Given a sorted array, remove duplicates in-place and return the number of unique elements.
# Goal: Practice two-pointer techniques for modifying arrays without extra space
def remove_duplcts_from_a_sorted_arr(sorted_arr):
    # set_nums = set()
    # for i in range(len(sorted_arr)):
    #     if sorted_arr[i] not in set_nums:
    #         set_nums.add(sorted_arr[i])
    #     elif sorted_arr[i] in set_nums:
    #         set_nums.pop()

    # return len(set_nums)

    # sorted_arr.sort()
    # count = 0
    # left, right = 0, len(sorted_arr) - 1
    
    # while left < right:
    #     if sorted_arr[left] != sorted_arr[left + 1]:
    #         count += 1
    #     else:
    #         count -= 1
    #     left += 1
        
    #     if sorted_arr[right] != sorted_arr[right - 1]:
    #         count += 1
    #     else:
    #         count -= 1
    #     right -= 1
    
    # return count

    if not sorted_arr:
        return 0  # Handle empty list edge case
    
    write_index = 1  # Position to overwrite duplicates

    for read_index in range(1, len(sorted_arr)):
        if sorted_arr[read_index] != sorted_arr[read_index - 1]:  # Found a new unique element
            sorted_arr[write_index] = sorted_arr[read_index]      # Overwrite duplicate
            write_index += 1   # Move write pointer
    
    return write_index   # Number of unique elements

# !!!
# Спершу розберись, як саме працює алгоритм, котрий вище!


# 3) Find the First Non-Repeating Element
# Task: Given a list, return the first element that appears only once. If all elements repeat, return None.
# Goal: Learn efficient frequency counting with dictionaries.
def find_first_non_repeating_element(arr: list[int]) -> int | None:
    if not arr:
        return None
    
    # for i in range(1, len(arr)):
    #     if (arr[i] != arr[i - 1]) and (arr[i] != arr[i + 1]):
    #         return arr[i]
        
    # freq_count_dict = {}
    # for i in range(len(arr)):
    #     if arr[i] in freq_count_dict:
    #         return arr[i]
    #     elif arr[i] not in freq_count_dict:
    #         freq_count_dict[arr[i]] = 1

    freq_count_dict = {}
    for num in arr:  #  More Pythonic way to build frequency dictionary
        freq_count_dict[num] = freq_count_dict.get(num, 0)

    for num in arr:   # Correctly finds the first non-repeating element
        if freq_count_dict[num] == 1:
            return num
    
    return None   # If all elements repeat, return None
 

# 4) Find the Longest Consecutive Sequence
# Task: Given an unsorted list of integers, find the length of the longest consecutive sequence
# (e.g., [100, 4, 200, 1, 3, 2] → 4 because 1, 2, 3, 4 is the longest sequence).
# Goal: Learn set-based lookup to solve problems efficiently
def find_longest_consecutive_sequence(arr: list[int]) -> list[int]:
    if not arr:
        return None

    arr.sort()

    len_arr_1 = len(arr) - 1
    l, r = 0, len_arr_1
    len_l, len_r, max_len = 0, 0, 0
    delta_l = arr[1] - arr[0]
    delta_r = arr[len_arr_1] - arr[len_arr_1 - 1]

    while l < r:
        if arr[l + 1] - arr[l] == delta_l:
            # l += 1
            print(f'l += 1 == {l}')
        else:
            len_l = l + 1
            delta_l = arr[l + 2] - arr[l + 1]
            if max_len < len_l:
                max_len = len_l
        l += 1

        if arr[r] - arr[r - 1] == delta_r:
            # r -= 1
            print(f'r -= 1 == {r}')
        else:
            len_r = r - 2
            delta_r = arr[r - 1] - arr[r - 2]
            if max_len < len_r:
                max_len = len_r
        r -= 1
    
    # print(f'set(arr) == {set(arr)}')
    # print(f'arr.sort() == {arr.sort()}')
    return max_len


def main():
    # my_arr = [2,6,4,3,5,3]
    # sum_items = get_sum_list(my_arr)
    # min_arr, max_arr = get_max_min_arr(my_arr)
    # # print(f'sum_items == {sum_items}')
    # print(f'min_arr == {min_arr}\nmax_arr == {max_arr}')

    # arr = get_reverse_an_arr(my_arr)
    # print(f'arr == {arr}')

    # find_num = 3
    # count = get_count_elem(my_arr, find_num)
    # print(f'count == {count}')

    # arr_new = get_prefix_sum(my_arr)
    # print(f'arr_new == {arr_new}')

    # arr_new = shift_elems_in_arr(my_arr)
    # print(f'arr_new == {arr_new}')

    # num = 2
    # arr_new = find_ind_of_target_elem(my_arr, num)
    # print(f'arr_new == {arr_new}')

    # my_arr = [2,6,4,3,5,3]
    # my_arr = [6,7,3,6,4,2,2,4,1,5,8,3,5,3,34,6,2]
    # arr_new = find_duplicates_in_arr(my_arr)
    # print(f'arr_new == {arr_new}')

    # # my_arr = [0, 1, 0, 3, 12]
    # my_arr = [1,3,0,5,0,0,8]
    # arr_new = move_all_zeros_to_the_end(my_arr)
    # print(f'arr_new == {arr_new}')

    # sorted_list = [5,3,5,2,4,43,6,3,6]
    # sorted_list = [3,3,6,7,8,11,12,15,15,23]
    # num = 15
    # i, j = find_pair_with_target_sum(sorted_list, num)
    # print(f'i, j == {i}, {j}')

    # # my_list = [3,3,6,7,8,11,12,15,15,23]
    # my_list = [5,3,5,2,4,43,6,3,6]
    # k = 1
    # sum_max = find_max_sum_of_a_subarr_of_sz_k(my_list, k)
    # print(f'arr = {my_list}\nk = {k}\n')
    # print(f'sum_max == {sum_max}')

    # # sorted_arr = [3,3,6,7,8,11,12,15,15,23]
    # sorted_arr = [1,1,2,3,4,4,5]
    # count_els = remove_duplcts_from_a_sorted_arr(sorted_arr)
    # print(f'sorted_arr == {sorted_arr}\ncount_els == {count_els}')

    # # sorted_arr = [3,3,6,7,8,11,12,15,15,23]
    # sorted_arr = [1,1,2,3,4,4,5]
    # first_no_repeat_elem = find_first_non_repeating_element(sorted_arr)
    # print(f'sorted_arr == {sorted_arr}\nfirst_no_repeat_elem == {first_no_repeat_elem}')

    # sorted_arr = [3,3,6,7,8,11,12,15,15,23]
    # sorted_arr = [1,1,2,3,4,4,5]
    sorted_arr = [100, 4, 200, 1, 3, 2]
    longest_consecutive_sequence = find_longest_consecutive_sequence(sorted_arr)
    # print(f'sorted_arr == {sorted_arr}')
    print(f'sorted_arr == {sorted_arr}\nlongest_consecutive_sequence == {longest_consecutive_sequence}')

    # # list_unsort = rnd.sample(range(1, 100), rnd.randint(10, 20))
    # list_unsort = [3, 7, 2, 9, 1, 0, 4, 8, 6, 5]
    # len_list = len(list_unsort)

    # print(list_unsort)
    # # print(bubble_sort(list_unsort))
    # # print(bubble_sort_recursive(list_unsort))
    # print(selection_sort(list_unsort, len_list))


if __name__ == '__main__':
    main()