def merge_sort(arr: list[int]) -> list[int]:
    # if not arr:
    #     return arr
    
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = len(arr) // 2

    result = []
    left_half = arr[:mid]
    right_half = arr[mid:]

    result.extend(right_half)
    result.extend(left_half)
    
    return result