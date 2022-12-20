/*
Sum All Odd Fibonacci Numbers
Given a positive integer num, return the sum of all odd Fibonacci numbers 
that are less than or equal to num.
The first two numbers in the Fibonacci sequence are 1 and 1.
 Every additional number in the sequence is the sum of the two previous numbers. 
 The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
For example, sumFibs(10) should return 10 because all odd Fibonacci numbers 
less than or equal to 10 are 1, 1, 3, and 5.
*/

// PERSONAL SOLUTION
function sumFibs(num) {
    // Initial list of Fibonacci
    const fibArray = [0,1];
    // Initial sumatory
    let sumOddsFib = 1;
    // In case num greater or equal than 1
    if(num > 1){ 
      // Loop while num lesser or equal than the sum 
      let continueSum = true;    
      while (continueSum){ 
        let fib = newFib(fibArray);  
        // The new fibonacci number is an odd
        if (fib <= num){
          // Adding new fibonacci number to the list
          fibArray.push(fib);
          if (fib % 2 != 0){sumOddsFib += fib;}
        } else {
          continueSum = false;
        }     
      } 
    }
    //console.log(fibArray);
    return sumOddsFib;
  }
  
  function newFib (fibArray){
    return fibArray[fibArray.length-1]+fibArray[fibArray.length-2]
  }
  
  console.log(sumFibs(1000));

  // SOLUTION 1
  function sumFibs(num) {
    let prevNumber = 0;
    let currNumber = 1;
    let result = 0;
    while (currNumber <= num) {
      if (currNumber % 2 !== 0) {
        result += currNumber;
      }
      currNumber += prevNumber;
      prevNumber = currNumber - prevNumber;
    }
  
    return result;
  }
  
  // test here
  sumFibs(4);

  // SOLUTION 2
  function sumFibs(num) {
    // Perform checks for the validity of the input
    if (num <= 0) return 0;
  
    // Create an array of fib numbers till num
    const arrFib = [1, 1];
    let nextFib = 0;
  
    // We put the new Fibonacci numbers to the front so we
    // don't need to calculate the length of the array on each
    // iteration
    while ((nextFib = arrFib[0] + arrFib[1]) <= num) {
      arrFib.unshift(nextFib);
    }
  
    // We filter the array to get the odd numbers and reduce them to get their sum.
    return arrFib.filter(x => x % 2 != 0).reduce((a, b) => a + b);
  }