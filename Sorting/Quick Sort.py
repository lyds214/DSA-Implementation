def quickSort(array, left, right):
    if left < right:
        pivot = right
        index = partition(array, pivot, left, right)

        quickSort(array, left, index - 1)
        quickSort(array, index + 1, right)
    
    return array 

def partition(array, pivot, left, right):
    pivot_value = array[pivot]
    index = left 

    for x in range(left, right):
        if array[x] < pivot_value:
            swap(array, x, index)
            index += 1 
    
    swap(array, right, index)
    return index 

def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp 

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quickSort(numbers,0,len(numbers)-1))