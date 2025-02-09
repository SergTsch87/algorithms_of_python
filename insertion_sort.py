def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    
    return arr