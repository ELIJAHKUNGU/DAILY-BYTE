//======================== First Order Functions ============================
const morning_message = (morning_text) =>{
   return ` ${morning_text}`;
}
console.log(morning_message('Good morning'))

//========================= High order functions=============================
const greetings =(name) => {
    return function greetings_message (message, compliment ){
        console.log(`Hi !! ${message} ${name} ${compliment}` )
        
    }

}
const salamuheavy = greetings('ELIJAh')
console.log(salamuheavy("Good Morning", "Today you look awesome"))
// ================ OR ===================
const salamuByName = (name) => {
    return `${name}`

}
const salamu_Message = (salamuByName, salamumessage, salamu_compliment, name) => {
    console.log(`${salamumessage} ${salamuByName(name)} ${salamu_compliment}`)

}
salamu_Message(salamuByName, 'Good Morning', "Today you look lovely", "KIM")

//============================ Unary functions ======================================
const Unaryfunction = (a) => console.log(a + 10)
// =========================== Currying Functions ===================================
const multiarg = (a, b, c) => a + b + c 
console.log(multiarg(1, 2, 3));
const CurryingFunction = (a) =>  (b) =>  (c) => a => b => c
console.log(CurryingFunction(1)); // returns a function 1 + b +c
console.log(CurryingFunction(1) (2)); // returns a function c = 3 +c
console.log(CurryingFunction(1)(2)(3)); // returns a number 

// =========================== Pure Functions =======================================
// IMPURE
const numArr = []
const impurefunction = (number) => numArr.push(number)

//PURE FUNCTIONS
const pureFunction = (number) => (ArrNumItems) => ArrNumItems.concat([number])

//Display the results
console.log('impure fun',impurefunction(6)); // returns 1
console.log(numArr); // returns [6]
console.log(pureFunction(7)(numArr)); // returns [6, 7]
console.log(numArr); // returns [6]


// ============================================
// What is IIFE(Immediately Invoked Function Expression)
// ===========================================
// IIFE (Immediately Invoked Function Expression) is a JavaScript function that runs as soon as it is defined. 
// The signature of it would be as below,

(function iifeFunction() {
    var message = "IIFE";
  console.log(message);
    
}) () ;

// The primary reason to use an IIFE is to obtain data privacy because any variables declared within the IIFE cannot be accessed by the outside world. i.e, If you try to access variables with
//  IIFE then it throws an error as below,