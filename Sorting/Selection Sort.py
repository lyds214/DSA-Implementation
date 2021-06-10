def selectionSort(arr):
    for x in range(len(arr)):
        min_num = x

        for y in range(x + 1, len(arr)):
            if arr[min_num] > arr[y]:
                min_num = y 
        
        arr[min_num], arr[x] = arr[x], arr[min_num]

    return arr




print(selectionSort([6, 7, 3, 4, 7, 8, 10]))
print(selectionSort([-1, 2, 3, -10, 4, 12, 39]))