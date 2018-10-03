def insertion_sort(array):
    # The outer loop goes through the unsorted part of the array
    # i represents the position of the sorted elements
    # the first element is already sorted
    for i in list(range(len(array))):
        # the inner loop goes through the sorted elements
        for j in list(range(len(array[:i]))):
            if array[i] < array[j]:
                element = array[i]
                del array[i]
                array.insert(j, element)

    return array

numbers = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(numbers))