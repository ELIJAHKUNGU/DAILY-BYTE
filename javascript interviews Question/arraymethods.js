const newArr = [1, 2,3, 4,5]
// Slice method (start, end)
// Note: Slice method won't mutate the original array but it returns the subset as a new array.
console.log(newArr.slice(0, 3))

//  splice method
// splice(Index, No of items to be deleted from original array)
console.log(newArr)
console.log(newArr.splice(0,2)) //returns = [1,2] original arr [3,4,5]
console.log(newArr.splice(0,1, 'a', 'b', 'c'))    // returns =  [1] original_arr =  [a, b,c, 4,5]