def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for key_ind in range(1, len(arr)):
        key_elem = arr[key_ind]
        for item in range(key_ind, 0, -1):
            if arr[item -1] > key_elem:
                arr[item - 1], arr[item] = key_elem, arr[item - 1]
                key_ind = item - 1
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