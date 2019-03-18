def quick_sort(numbers):
    # base case
    if len(numbers) < 2:
        return numbers

    pivot = numbers.pop()
    left_array = []
    right_array = []
    for i in list(range(len(numbers))):
        if numbers[i] < pivot:
            left_array.append(numbers[i])
        else:
            right_array.append(numbers[i])
    sorted_left = quick_sort(left_array)
    sorted_right = quick_sort(right_array)
    return sorted_left + sorted_right

numbers = [64, 34, 25, 12, 22, 11, 90,78,54]
print(quick_sort(numbers))
