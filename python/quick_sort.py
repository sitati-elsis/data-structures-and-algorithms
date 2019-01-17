def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers
    pivot = numbers.pop()
    left = []
    right = []
    for item in numbers:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    return left_sorted + left.append(pivot) + right_sorted

    
numbers = [64, 34, 25, 12, 22, 11, 90,78,54]
print(quick_sort(numbers))