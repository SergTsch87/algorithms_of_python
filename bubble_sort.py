def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False   # Track swaps
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   # if no swaps, array is sorted
            break
    return arr