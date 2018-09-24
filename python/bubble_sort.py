

def bubble_sort(array):
    list_size = len(array)
    # loop through the list n times
    for count in list(range(list_size)):
        # go throught the list until the sorted part
        # swap if the element found is greater than the next element
        for item in list(range(list_size - count - 1)):
            if array[item] > array[item + 1]:
                array[item], array[item +1 ] = array[item + 1], array[item]
        
    return array

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))