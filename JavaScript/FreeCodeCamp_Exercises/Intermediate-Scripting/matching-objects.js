/* 
Wherefore art thou
Make a function that looks through an array of objects (first argument) 
and returns an array of all objects that have matching name and value pairs (second argument). 
Each name and value pair of the source object has to be present in the object from the collection 
if it is to be included in the returned array.

For example, if the first argument is [{ first: "Romeo", last: "Montague" }, 
{ first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], 
and the second argument is { last: "Capulet" }, then you must return the third object 
from the array (the first argument), because it contains the name and its value, 
that was passed on as the second argument.
*/

// PERSONAL SOLUTION
function whatIsInAName(collection, source) {
    const arr = [];
    // Only change code below this line
    collection.forEach(obj =>{
        let matches = true;
        const sourceLength = Object.keys(source).length;
        for(let i = 0; i < sourceLength; i++){        
          const key = Object.keys(source)[i];
          if(obj.hasOwnProperty(key)){      
            if(obj[key] != source[key]){matches = false};
          }else{
            matches = false;
          }
        }
        if(matches == true)arr.push(obj);     
      });    
  
    // Only change code above this line
    return arr;
  }

  // FIRST SOLUTION
  function whatIsInAName(collection, source) {
    // "What's in a name? that which we call a rose
    // By any other name would smell as sweet.”
    // -- by William Shakespeare, Romeo and Juliet
    var srcKeys = Object.keys(source);
  
    // filter the collection
    return collection.filter(function(obj) {
      for (var i = 0; i < srcKeys.length; i++) {
        if (
          !obj.hasOwnProperty(srcKeys[i]) ||
          obj[srcKeys[i]] !== source[srcKeys[i]]
        ) {
          return false;
        }
      }
      return true;
    });
  }

  // SECOND SOLUTION
  function whatIsInAName(collection, source) {
    // "What's in a name? that which we call a rose
    // By any other name would smell as sweet.”
    // -- by William Shakespeare, Romeo and Juliet
    var srcKeys = Object.keys(source);
  
    return collection.filter(function(obj) {
      return srcKeys.every(function(key) {
        return obj.hasOwnProperty(key) && obj[key] === source[key];
      });
    });
  }

  // THIRD SOLUTION
  function whatIsInAName(collection, source) {
    // "What's in a name? that which we call a rose
    // By any other name would smell as sweet.”
    // -- by William Shakespeare, Romeo and Juliet
    var srcKeys = Object.keys(source);
  
    // filter the collection
    return collection.filter(function(obj) {
      return srcKeys
        .map(function(key) {
          return obj.hasOwnProperty(key) && obj[key] === source[key];
        })
        .reduce(function(a, b) {
          return a && b;
        });
    });
  }