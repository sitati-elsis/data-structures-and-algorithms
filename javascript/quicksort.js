function quickSort(numbers_array){
    // base case
    if (numbers_array.length < 2) {
        return numbers_array
    }

    let pivot = numbers_array.pop()
    let leftArray = []
    let rightArray = []
    for (i = 0; i < numbers_array.length; i++){
        if (numbers_array[i]< pivot){
            leftArray.push(numbers_array[i])
        }
        else{
            rightArray.push(numbers_array[i])
        }
    }
    let leftSorted = quickSort(leftArray)
    let righSorted = quickSort(rightArray)
    
    return leftSorted.concat(pivot, righSorted)
}

numbers = [64, 34, 25, 12, 22, 11, 90,78,54]
console.log(quickSort(numbers))
