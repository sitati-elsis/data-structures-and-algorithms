function insertionsort(numArray){
    // The outer loop goes through the unsorted part of the array
    // i represents the position of the sorted elements
    // the first element is already sorted
    for (let i=1; i<numArray.length; i++){
        // the inner loop goes through the sorted elements in the array
        for (let j=0; j<i; j++){
            if (numArray[i] < numArray[j]){
                const insertionElement = numArray.splice(i, 1)
                numArray.splice(j, 0, insertionElement[0])
            }
        }
    }
    return numArray
}

let numbers = [64, 34, 25, 12, 22, 11, 90]
console.log(insertionsort(numbers))