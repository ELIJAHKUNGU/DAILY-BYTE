const str = "racecar";

const checkPalindrome = (str) => {

    let reversedString = str.split("").reverse().join("")

    return str = reversedString
}


console.log(checkPalindrome(str))
// method two
const checkPalindrome2 = (str) => {
    let reversedString = ""
    for (let i = str.length - 1; i >= 0; i--) {
        reversedString += str[i]
    }
    return str === reversedString
}

console.log(checkPalindrome2(str))

// method three
const checkPalindrome3 = (str) => {
   let reversedString = str.split("").reduce((acc, curr) => {
         let sum =  curr + acc
         console.log(sum)
            return sum
    }
    , "")
    return str === reversedString
}
// r
// ar
// car
// ecar
// cecar
// acecar
// racecar