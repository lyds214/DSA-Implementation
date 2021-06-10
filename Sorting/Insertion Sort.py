def insertionSort(arr):

    # We're going to start at index 1 which is basically "sorted"
    for x in range(1, len(arr)):

        # This is the element that we're going to insert.
        current_value = arr[x]

        # This is the index of the element that we're going to insert.
        current_position = x 

        # If the previous element is smaller than the current element, we're going to shift the current element
        # to the left. 
        while current_position < 0 and arr[current_position - 1] < current_value:
            arr[current_position] = arr[current_position - 1]
            current_position -= 1 
        
        # Once the shift is done, we're going to insert the current value at its respectful place.
        arr[current_position] = current_value

        
    
    


print(insertionSort([8, 9, 2, 4, 5]))