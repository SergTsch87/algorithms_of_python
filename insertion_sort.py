def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(1, n):
        key_ind = i
        for j in range(key_ind, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    
    return arr


# def main():
#     arr = [9,5,1,4,3]
#     arr_new = insertion_sort(arr)
#     print(arr_new)


# if __name__ == '__main__':
#     main()