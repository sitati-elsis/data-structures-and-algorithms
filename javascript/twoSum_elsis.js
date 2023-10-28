function twoNumberSum(array, targetSum) {
    let result = []
    const pairing = {}
    for (i=0; i <array.length; i++){
      if(array[i] in pairing){
        result = [targetSum - array[i], array[i]]
      }
      pairing[targetSum - array[i]] = array[i]
    }
    return result
  }
  