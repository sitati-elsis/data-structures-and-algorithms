def selection_sort(array):
    result = array
    list_size = len(array)
    # go through all elements in the array
    for i in list(range(list_size)):
        minimum_index = i
        for j in list(range(i+1, list_size)):
            if array[minimum_index] > array[j]:
                minimum_index = j

        array[i], array[minimum_index] = array[minimum_index], array[i]

    return result

num = [73,53,33,43,20, 45]
print(selection_sort(num))

