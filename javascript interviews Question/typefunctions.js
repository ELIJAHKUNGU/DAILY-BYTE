// First Order Functions
const morning_message = (morning_text) =>{
   return ` ${morning_text}`;
}
console.log(morning_message('Good morning'))

// High order functions
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