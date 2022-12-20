/*
Steamroller
Flatten a nested array. You must account for varying levels of nesting.
*/

// PERSONAL SOLUTION
let emptyArr = [];

function steamrollArray(arr) {
  if(!Array.isArray(arr)){    
    emptyArr.push(arr)    
  }else if (arr.length > 1){    
    steamrollArray(arr[0]);
    steamrollArray(arr.slice(1));
  }else if(arr.length === 1){
    steamrollArray(arr[0]);
    
  }
  return emptyArr;
}

console.log(steamrollArray([1, [2], [3, [[4]]]]));

// SOLUTION 1
function steamrollArray(arr) {
    const flat = [].concat(...arr);
    return flat.some(Array.isArray) ? steamrollArray(flat) : flat;
  }

  // SOLUTION 2
  function steamrollArray(val,flatArr=[]) {
    val.forEach(item => {
      if (Array.isArray(item)) steamrollArray(item, flatArr);
      else flatArr.push(item);
    });
    return flatArr;
  }

