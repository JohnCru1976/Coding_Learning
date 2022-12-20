/*
You will be provided with an initial array (the first argument in the destroyer function), 
followed by one or more arguments. Remove all elements from the initial array that are of
the same value as these arguments.
Note: You have to use the arguments object.
*/

// PERSONAL SOLUTION
function destroyer(arr, ...args) {
    let tempArray = [];
    args.forEach(elemArgs => {    
      arr.forEach(elemArr =>{
        if (elemArr != elemArgs){tempArray.push(elemArr);}
      });
      arr = tempArray.slice();
      tempArray = tempArray.splice();
    });
    
    return arr;
  }
  
  // SOLUTION 1
  function destroyer(arr) {
    let valsToRemove = Object.values(arguments).slice(1);
  
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < valsToRemove.length; j++) {
        if (arr[i] === valsToRemove[j]) {
          delete arr[i];
        }
      }
    }
    return arr.filter(item => item !== null);
  }

   // SOLUTION 2
   function destroyer(arr) {
    var valsToRemove = Array.from(arguments).slice(1);
    return arr.filter(function(val) {
      return !valsToRemove.includes(val);
    });
   }

    // SOLUTION 3
    function destroyer(arr, ...valsToRemove) {
        return arr.filter(elem => !valsToRemove.includes(elem));
    }