def quicksort(listToSort, lowIndex, highIndex):
    # if we have more than one item in the list
    if ((highIndex - lowIndex) > 0):
        p = partition(listToSort, lowIndex, highIndex)
        # sort the lower end of the partition 
        quicksort(listToSort, lowIndex, p-1)
        # sort the higher end of the partition 
        quicksort(listToSort, p+1, highIndex)


def partition(listToSort, lowIndex, highIndex):
    divider = lowIndex
    pivot = highIndex
    for i in range(lowIndex, highIndex):
        if (listToSort[i] < listToSort[pivot]):
            # swapping the two elements in the list
            listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]
            # increment divider to point to the next element in the list
            divider += 1
    # swap the pivot with where the divider is right now
    listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]

    return divider

testcase1 = [1,4,6,7,89,43,23,45,65,3]
testcase2 = [54,23,26,32,67,99,1,4,5]
quicksort(testcase1, 0, 9)
print(testcase1)
quicksort(testcase2, 0, 8)
print(testcase2)
