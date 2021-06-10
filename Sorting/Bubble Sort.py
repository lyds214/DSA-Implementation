def bubbleSort(arr):
    for x in range(len(arr)): # 0, 1, 2, 3, 4
        for y in range(len(arr) - x - 1):
            if arr[y] > arr[y + 1]:
                arr[y + 1], arr[y] = arr[y], arr[y + 1]

    return arr





print(bubbleSort([7, 8, 3, 4, 5]))
print(bubbleSort([3, 4, 1, 2, 7, 4, 6, 12]))