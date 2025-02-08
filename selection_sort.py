def selection_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n - 1):
        m_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[m_index]:
                m_index = j  # Знайшли індекс найменшого елменту...
        arr[i], arr[m_index] = arr[m_index], arr[i]   # ...і поміняли його місцями з першим елементом поточної ітерації
    return arr


def recursive_selection_sort(arr, n=None):
    if n is None:
        n = len(arr)
        i = 0
    
    if n <= 1:
        return arr
    
    # for i in range(n - 1):
    m_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[m_index]:
        m_index = j
    
    arr[i], arr[m_index] = arr[m_index], arr[i]
    i += 1
            
    return recursive_selection_sort(arr, n-1)