/*
Drop it
Given the array arr, iterate through and remove each element 
starting from the first element (the 0 index) until the function func 
returns true when the iterated element is passed through it.
Then return the rest of the array once the condition is satisfied, 
otherwise, arr should be returned as an empty array.
*/

// PERSONAL SOLUTION
function dropElements(arr, func) {
    let isReached = false;
    return arr.map(function(elem){
      if (func(elem) || isReached){
        isReached = true;
        return elem;
      }
    })
    .filter(elem => elem != undefined);
    
  }
  
  // TEST
  console.log(dropElements([0, 1, 0, 1], function(n) {return n === 1;}));

  // SOLUTION 1
  function dropElements(arr, func) {
    while (arr.length > 0 && !func(arr[0])) {
      arr.shift();
    }
    return arr;
  }
  
  // SOLUTION 2
  function dropElements(arr, func) {
    let sliceIndex = arr.findIndex(func);
    return arr.slice(sliceIndex >= 0 ? sliceIndex : arr.length);
  }
  
  // SOLUTION 3 RECURSION
  function dropElements(arr, func, i = 0) {
    return i < arr.length && !func(arr[i])
      ? (dropElements(arr.slice(i + 1), func, i))
      : arr;
  }

  // SOLUTION 4 RECURSION WITH PERSONAL MODIFICATION (Without i=0 parameter)
  function dropElements(arr, func) {
    return arr.length > 0 && !func(arr[0])
      ? (dropElements(arr.slice(1), func))
      : arr;
  }
  

