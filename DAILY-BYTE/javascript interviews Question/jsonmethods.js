const jsonObject = {
    "name":"Elijah",
    "age":"30"
}

// Convert the json object to  a string

const jsonString = JSON.stringify(jsonObject)
console.log(jsonString)

// Convert the json string to json object

const jsonNewObject = JSON.parse(jsonString)
console.log(jsonNewObject)