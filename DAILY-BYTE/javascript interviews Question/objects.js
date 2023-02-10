// Possible way to create objects in javascript
// 1. Object Constructor
var object = new Object();
// 2. Object'S CREATE METHOD
var object = Object.create(null);
// 3. Object Literal
var obj = {
    name: "John",
    age: 30,
};
// 4. Fuctional Constructor
function Person(name){
    this.name = "Funnction name"
    this.age = 30
}
    var objectF = new Person()
    console.log(objectF);
// 5.Function constructor with prototype:
    function Person() {}
    Person.prototype.name = "JOHN"
    var objectP = new Person();
    console.log(objectP);
// 6. ES6 Class syntax:
class Person {
    constructor(name) {
      this.name = name;
    }
  }
  
  var object = new Person("ELIJAH ");

// 7. Singleton pattern:
// A Singleton is an object which can only be instantiated
//  one time. Repeated calls to its constructor return 
var object = new (function () {
    this.name = "ELIJAH ";
  })();

