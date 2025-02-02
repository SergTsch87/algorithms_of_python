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
        

def main():
    # list_unsort = rnd.sample(range(1, 100), rnd.randint(10, 20))
    list_unsort = [3, 7, 2, 9, 1, 0, 4, 8, 6, 5]

    print(list_unsort)
    # print(bubble_sort(list_unsort))
    print(bubble_sort_recursive(list_unsort))



if __name__ == '__main__':
    main()