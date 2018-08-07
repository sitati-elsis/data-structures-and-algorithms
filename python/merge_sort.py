# define method to merge the arrays

def merge(left, right):
    # final merged array
    result = []
    # i and j represent indexes for left and arrays
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1

    # if you have elements remaining in the left array
    result += left[i:]
    # if you have result remaining in the right array
    result +=  right[j:]
    return result

def mergesort(lst):
    # if the list is already sorted
    if len(lst) <= 1:
        return lst
    # if we have more than one item in the list
    midpoint = int(len(lst)/2)
    left = mergesort(lst[:midpoint])
    right = mergesort(lst[midpoint:])
    return merge(left, right)

# items = [2, 45, 65, 87, 67, 4, 25, 98, 45, 15, 87, 99, 98]
items = [5,4,3,2,1]
print(mergesort(items))