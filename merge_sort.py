def merge_sort(arr: list[int]) -> list[int]:
    # if not arr:
    #     return arr
    
    n = len(arr)
    if n <= 1:
        return arr