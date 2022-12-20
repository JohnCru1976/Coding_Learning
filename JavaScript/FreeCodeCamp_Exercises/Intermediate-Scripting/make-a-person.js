/*
Make a Person
Fill in the object constructor with the following methods below:
getFirstName()
getLastName()
getFullName()
setFirstName(first)
setLastName(last)
setFullName(firstAndLast)
Run the tests to see the expected output for each method. 
The methods that take an argument must accept only one argument and it has to be a string. 
These methods must be the only available means of interacting with the object.
*/

// PERSONAL SOLUTION
const Person = function(firstAndLast) {
    // Only change code below this line
    // Complete the method below and implement the others similarly
    this.getFullName = function() {    
      return firstAndLast ;
    };
    this.getFirstName = function(){
      let regExp = /^\w+/i;    
      return firstAndLast.match(regExp)[0];
    }
    this.getLastName = function(){
      let regExp = /(\w+)$/i;    
      return firstAndLast.match(regExp)[0];
    }
    this.setFirstName = function(first){
      let regExp = /^\w+/i;
      firstAndLast = firstAndLast.replace(regExp,first);
    }
    this.setLastName = function(last){
      let regExp = /(\w+)$/i;
      firstAndLast = firstAndLast.replace(regExp,last);
    }
    this.setFullName = function(total){
      let regExp = /.+/gi;
      firstAndLast = firstAndLast.replace(regExp,total);
    }
  };
  
  const bob = new Person('Bob Ross');
  console.log(Object.keys(bob).length);
  bob.setLastName("Cru");
  console.log(bob.getFullName());
  console.log(bob.getFirstName());
  console.log(bob.getLastName());
  

  // FREECODECAMP SOLUTION
  var Person2 = function(firstAndLast) {
    let fullName = firstAndLast;
  
    this.getFirstName = function() {
      return fullName.split(" ")[0];
    };
  
    this.getLastName = function() {
      return fullName.split(" ")[1];
    };
  
    this.getFullName = function() {
      return fullName;
    };
  
    this.setFirstName = function(name) {
      fullName = name + " " + fullName.split(" ")[1];
    };
  
    this.setLastName = function(name) {
      fullName = fullName.split(" ")[0] + " " + name;
    };
  
    this.setFullName = function(name) {
      fullName = name;
    };
  };
  