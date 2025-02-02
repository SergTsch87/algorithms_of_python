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
def bubble_sort_recursive(arr, i):
    if i == 0:
        return arr
    else:
        if arr[i] > arr[i + 1] and i < len(arr):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            bubble_sort_recursive(arr, i)
        i += 1

# def bubble_sort_recursive(arr, item_i = 0, item_j = 0):
#     if item_i == 0 and item_j == 0:
#         return arr
#     else:
#         if arr[item_j] > arr[item_j + 1]:
#             arr[item_j], arr[item_j + 1] = arr[item_j + 1], arr[item_j]
#             bubble_sort_recursive(arr, item_i, item_j)
#     # bubble_sort_recursive(arr, item_i, item_j)
#     # for item_i in range(len(arr)):
#     if item_i < len(arr):
#         # for item_j in range(len(arr) - item_i - 1):
#         if item_j < len(arr) - item_i - 1:
#             if arr[item_j] > arr[item_j + 1]:
#                 arr[item_j], arr[item_j + 1] = arr[item_j + 1], arr[item_j]
#                 bubble_sort_recursive(arr, item_i, item_j)
#             else:
#                 return
#             item_j += 1
        
#         item_i += 1
        

def main():
    # list_unsort = rnd.sample(range(1, 100), rnd.randint(10, 20))
    list_unsort = [3, 7, 2, 9, 1, 0, 4, 8, 6, 5]

    print(list_unsort)
    # print(bubble_sort(list_unsort))
    print(bubble_sort_recursive(list_unsort, i = 0))



if __name__ == '__main__':
    main()