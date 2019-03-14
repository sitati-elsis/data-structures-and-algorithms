function mergeSort(numbers){
    // base case for the recursion
    // the array is sorted if it only has one element
    if (numbers.length < 2){
        return numbers
    }
    let arrayItems = numbers.length
    let midpoint = Math.floor(arrayItems/2)
    let leftArray = numbers.slice(0, midpoint)
    let rightArray = numbers.slice(midpoint)
    let leftSorted = mergeSort(leftArray)
    let rightSorted = mergeSort(rightArray)

    return merge(leftSorted, rightSorted)

}

function merge(leftArray, rightArray){
    let sortedArray = []
    // This loop should execute as long as we have elements in both arrays
    while (leftArray.length && rightArray.length){
        if (leftArray[0] <= rightArray[0]){
            sortedArray.push(leftArray.shift())
        }
        else{
            sortedArray.push(rightArray.shift())
        }  
    }
    // it is possible that we could have elements remaining in either of the arrays
    return sortedArray.concat(leftArray, rightArray)

}

numbers = [64, 34, 25, 12, 22, 11, 90,78,54]
console.log(mergeSort(numbers))
