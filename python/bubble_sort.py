

def bubble_sort(array):
    result = array
    list_size = len(array)
    # loop trough all elements of the array
    for i in list(range(list_size)):
        for j in list(range(list_size-i-1)):
            # go through the array until the last sorted element
            # swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                # array[j], array[j+1] = array[j+1], array[j]
    return result

    
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))