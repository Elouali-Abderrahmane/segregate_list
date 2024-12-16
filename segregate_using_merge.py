def segregate_using_merge(arr, start, end):
    if(start == end):
        return
    
    mid = (start + end) // 2
    segregate_using_merge(arr, start, mid)
    segregate_using_merge(arr, mid + 1, end)

    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left_length = mid - start + 1
    left_arr = [arr[start + i] for i in range(left_length)]

    right_length = end - mid
    right_arr = [arr[mid + 1 + i] for i in range(right_length)]

    i = j = 0
    k = start

    while(i < left_length and left_arr[i] < 0):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while(j < right_length and right_arr[j] < 0):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    while(i < left_length):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while(j < right_length):
        arr[k] = right_arr[j]
        j += 1
        k += 1

arr = [-2, 3, 8, -4, 7, 9, -9, 8]

segregate_using_merge(arr, 0, len(arr) - 1)

print(arr)