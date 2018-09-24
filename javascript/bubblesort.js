function bubblesort(numbers_array){
    // go through the array n times
    for (i = 0;  i < numbers_array.length; i++){
        // go through the array until the sorted parent
        // if item found is greater that the next item swap them
        for (j = 0; j < numbers_array.length - i - 1; j++){
            if (numbers_array[j] > numbers_array[j+1]){
                const temp = numbers_array[j]
                numbers_array[j] =  numbers_array[j+1]
                numbers_array[j+1] = temp 
            }
        }
    }
    return numbers_array
}

numbers = [64, 34, 25, 12, 22, 11, 90]
console.log(bubblesort(numbers))