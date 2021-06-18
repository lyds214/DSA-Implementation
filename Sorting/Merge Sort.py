def mergeSort(arr):
    if len(arr) == 1:
        return arr 
    
    mid = len(arr) // 2
    right = arr[mid:]
    left = arr[:mid]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0 

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1 
        else:
            result.append(right[right_index])
            right_index += 1 
    
    return result + left[left_index] + right[right_index]