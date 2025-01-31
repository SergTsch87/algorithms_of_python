#!usr/bin/env

import random as rnd
# import math


def bubble_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        swapped = False
        for j in range(len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: # якщо масив на якійсь ітерації вже є відсортованим, - тоді не витрачаймо ресурсів на зайві ітерації
            break
    return arr


def main():
    # list_unsort = rnd.sample(range(1, 100), rnd.randint(10, 20))
    list_unsort = [3, 7, 2, 9, 1, 0, 4, 8, 6, 5]

    print(list_unsort)
    print(bubble_sort(list_unsort))



if __name__ == '__main__':
    main()