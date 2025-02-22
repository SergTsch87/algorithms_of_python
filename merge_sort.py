from heapq import merge



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Treat each element as a sorted subarray of size 1
    queue = [[x] for x in arr]

    while len(queue) > 1:
        new_queue = []
        for i in range(0, len(queue) - 1, 2):
            new_queue.append(list(merge(queue[i], queue[i + 1])))
        
        if len(queue) % 2 == 1:   # Handle odd-length case
            new_queue.append(queue[-1])
        
        queue = new_queue

    return queue[0] if queue else []
  

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2

#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
    
#     return merge(left_half, right_half)


# def merge(left, right):
#     result = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:  # Maintain stability
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:]) # Append remaining elements
#     result.extend(right[j:])
    
#     return result