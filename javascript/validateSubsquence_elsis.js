function isValidSubsequence(array, sequence) {
    let arrIndex = 0
    let sqIndex = 0
    while (arrIndex < array.length && sqIndex < sequence.length){
      if (array[arrIndex] === sequence[sqIndex]){
        sqIndex += 1
      }
      arrIndex += 1
    }
  
    return sqIndex === sequence.length
  }
  