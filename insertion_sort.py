def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

# # 1-й спосіб:
#     for i in range(1, n):
#         key_ind = i
#         for j in range(key_ind, 0, -1):
#             if arr[j - 1] > arr[j]:
#                 arr[j - 1], arr[j] = arr[j], arr[j - 1]

# 2-й спосіб:
    for step in range(1, n):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key

    return arr


def recursive_insertion_sort(arr):
    return arr


# def main():
#     arr = [9,5,1,4,3]
#     arr_new = insertion_sort(arr)
#     print(arr_new)


# if __name__ == '__main__':
#     main()