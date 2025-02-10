#!usr/bin/env

# import random as rnd
# import math


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


def main():
    my_arr = [2,6,4,3,5,3]
    # sum_items = get_sum_list(my_arr)
    # min_arr, max_arr = get_max_min_arr(my_arr)
    # # print(f'sum_items == {sum_items}')
    # print(f'min_arr == {min_arr}\nmax_arr == {max_arr}')

    # arr = get_reverse_an_arr(my_arr)
    # print(f'arr == {arr}')

    find_num = 3
    count = get_count_elem(my_arr, find_num)
    print(f'count == {count}')

    # # list_unsort = rnd.sample(range(1, 100), rnd.randint(10, 20))
    # list_unsort = [3, 7, 2, 9, 1, 0, 4, 8, 6, 5]
    # len_list = len(list_unsort)

    # print(list_unsort)
    # # print(bubble_sort(list_unsort))
    # # print(bubble_sort_recursive(list_unsort))
    # print(selection_sort(list_unsort, len_list))



if __name__ == '__main__':
    main()