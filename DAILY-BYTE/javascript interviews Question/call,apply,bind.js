const employee1 = {firstname:"Elijah", lastname:"Kungu"}
const employee2 = {firstname:"Joseph", lastname:"Michelle"}


function salamu  (greetings1, greetings2) {
    console.log(
        greetings1+ " "+ this.firstname + " " + this.lastname + " " + greetings2
    )

}
// Call method
salamu.call(employee1, "Hello", "How are you")

// Appply method

salamu.apply(employee2, ["Hello", "How are you?"])


// Bind method

const salamunewmethod = salamu.bind(employee2)
salamunewmethod("Hello", "How are you")