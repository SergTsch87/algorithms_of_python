def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# # Recursive version
# def bubble_sort_recursive(arr, n = None):
#     if n is None:
#         n = len(arr)

#     if n == 1:
#         return arr

#     # swapped = False    
#     for i in range(n - 1):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#             # swapped = True
        
#     # if not swapped:
#     #     return arr
        
#     return bubble_sort_recursive(arr, n - 1)


def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n <= 1:   # Base case: a single-element list is already sorted
                 # Для уникнення рекурсії на n = 0
        return arr

    for i in range(n - 1):   # Bubble the largest number to the end
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return recursive_bubble_sort(arr, n - 1)   # Recur on the unsorted part