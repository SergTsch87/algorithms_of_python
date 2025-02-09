def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    # if arr[0] > arr[1]:
    #     arr[0], arr[1] = arr[1], arr[0]

    key_ind = 0
    for i in range(1, n + 1):
        if arr[i] > arr[key_ind]:
            arr[i], arr[key_ind] = arr[key_ind], arr[i]
    
    return arr