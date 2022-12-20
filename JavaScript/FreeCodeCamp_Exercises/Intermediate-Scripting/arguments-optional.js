/*
Arguments Optional
Create a function that sums two arguments together. 
If only one argument is provided, then return a function that expects one argument and returns the sum.
For example, addTogether(2, 3) should return 5, and addTogether(2) should return a function.
Calling this returned function with a single argument will then return the sum:
var sumTwoAnd = addTogether(2);
sumTwoAnd(3) returns 5.
If either argument isn't a valid number, return undefined.
*/

// PERSONAL SOLUTION
function addTogether(...args) {
    const numbers = [...args]
    if(numbers.length == 2){
      if(typeof numbers[0] === "number" 
        && typeof numbers[1] === "number"){
           return numbers[0] + numbers[1];
        }   
    }else if (numbers.length == 1){
       if(typeof numbers[0] === "number"){
         return num2 =>{
           if (typeof num2 === "number"){
             return numbers[0] + num2;
           }    
         } 
       }
    } 
  }
  
 console.log(addTogether(2,3)); // Returns 5  
  var sumTwoAnd = addTogether(2);
  console.log(sumTwoAnd(5)); // Returns 7  
  console.log(addTogether(2)(8)) // Returns 10  
  console.log(addTogether(2)([8])) // Returns undefined

  // SOLUTION 1
  function addTogether() {
    const [first, second] = arguments;
    if (typeof(first) !== "number")
      return undefined;
    if (second === undefined)
      return (second) => addTogether(first, second);
    if (typeof(second) !== "number")
      return undefined;
    return first + second;
  }

  // SOLUTION 2
  function addTogether() {
    const [first, second] = arguments;
    // First argument is not a number
    if (typeof(first) !== "number") {
      return undefined;
    }
    // First argument is a number
    //  and second argument is not defined
    else if (second === undefined) {
      function addSecond(second) {
        // New argument is not a number
        if (typeof(second) !== "number") {
          return undefined;
        }
        // New argument is a number
        else {
          return first + second;
        }
      }
      // Note: returning a *function*
      return addSecond;
    }
    // First argument is a number
    //  and second argument is not a number
    else if (typeof(second) !== "number") {
      return undefined;
    }
    // First argument is a number
    //  and second argument is a number
    else {
      return first + second;
    }
  }