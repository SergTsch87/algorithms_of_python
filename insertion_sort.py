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
#     return arr

# # 2-й спосіб:
#     for step in range(1, n):
#         key = arr[step]
#         j = step - 1

#         # Compare key with each element on the left of it until an element smaller than it is found
#         # For descending order, change key<array[j] to key>array[j].
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1

#         # Place key at after the element just smaller than it.
#         arr[j + 1] = key

#     return arr

# 3-й спосіб
    # if arr[0] > arr[1]:
    #     arr[0], arr[1] = arr[1], arr[0]
    
    # key_sort = arr[0]
    # if key_sort > arr[1]:
    #     arr[0], arr[1] = arr[1], key_sort
    
    key_sort = arr[len(arr) - 1]
    # for num in range(1, len(arr)):
    #     if key_sort > arr[1]:
    #         arr[0], arr[1] = arr[1], key_sort
    print(f'Begin arr == {arr}')
    for item in range(len(arr) - 1, 0, -1):
        print(f'item == {item}')
        if key_sort < arr[item - 1]:
            arr[item], arr[item - 1] = arr[item - 1], key_sort
        else:
            break

    return arr


def recursive_insertion_sort(arr, n=None, step=1):
    if n is None:
        n = len(arr)

    print(f'\nBegin of new iter\nstep == {step}, n == {n}\n')
    if step >= n - 1:
        print(f'step == {step}, n == {n}\nNext code: return arr')
        print(f'arr == {arr}\n')
        return arr
    
    key = arr[step]
    j = step - 1
    print(f'key == {key}, step == {step}, arr[step] == {arr[step]}, j == {j}')

    while j >= 0 and key < arr[j]:
        print(f'\nInside While loop\nj == {j}, key == {key}, arr[j] == {arr[j]}, arr[j + 1] == {arr[j + 1]}\n')
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    print(f'\nkey == {key}, j + 1 == {j + 1}, arr[j + 1] == {arr[j + 1]}\nThe End of iter')
    # step += 1
    
    # if arr[0] > arr[1]:
    #     arr[0], arr[1] = arr[1], arr[0]
    return recursive_insertion_sort(arr, n - 1, step + 1)


def main():
    # arr = [9,5,1,4,3]
    arr = [2,5,9,4,1]
    # arr_new = recursive_insertion_sort(arr)
    arr_new = insertion_sort(arr)
    print(arr_new)


if __name__ == '__main__':
    main()