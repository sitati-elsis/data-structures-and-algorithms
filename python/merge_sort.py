def merge_sort(numbers):
    # base case for the recursion
    if len(numbers) < 2 :
        return numbers

    midpoint = int(len(numbers)/2)
    left_array = numbers[:midpoint]
    right_array = numbers[midpoint:]
    left_sorted = merge_sort(left_array)
    right_sorted = merge_sort(right_array)

    return merge(left_sorted, right_sorted)

def merge(left_array, right_array):
    sorted_array = []
    # perfom this loop as long as we have elements in both arrays
    while(len(left_array) and len(right_array)):
        if left_array[0] < right_array[0]:
            sorted_array.append(left_array.pop(0))
        else:
            sorted_array.append(right_array.pop(0))

    # it is possible that an array may still be left with elements after the loop is done executing
    sorted_array = sorted_array + left_array + right_array
    return sorted_array
    
numbers = [64, 34, 25, 12, 22, 11, 90,78,54]
print(merge_sort(numbers))