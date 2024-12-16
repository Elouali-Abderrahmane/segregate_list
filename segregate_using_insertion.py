def segregate_using_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        if (key < 0):
            j = i - 1
            while(j >=0 and arr[j] >= 0):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

arr = [-2, 3, 8, -4, 7, 9, -9, 8]

segregate_using_insertion(arr)

print(arr)