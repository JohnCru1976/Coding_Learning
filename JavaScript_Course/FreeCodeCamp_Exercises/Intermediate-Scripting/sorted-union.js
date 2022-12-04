/*
Sorted Union
Write a function that takes two or more arrays and returns a new array 
of unique values in the order of the original provided arrays.
In other words, all values present from all arrays should be included
 in their original order, but with no duplicates in the final array.
The unique numbers should be sorted by their original order, but the 
final array should not be sorted in numerical order.
*/

//PERSONAL SOLUTION
function uniteUnique(...arr) {  
    const finalArray = [];
    arr.map(elemArray =>{    
      elemArray.map(elem =>{
        if(!finalArray.includes(elem)){
          finalArray.push(elem);
        }
      });
    });
    return finalArray;
  }
  // Test here
  console.log(uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]));

//SOLUTION 1
function uniteUnique(arr1, arr2, arr3) {
    var newArr;
    //Convert the arguments object into an array
    var args = Array.prototype.slice.call(arguments);
    //Use reduce function to flatten the array
    newArr = args.reduce(function(arrA, arrB) {
      //Apply filter to remove the duplicate elements in the array
      return arrA.concat(
        arrB.filter(function(i) {
          return arrA.indexOf(i) === -1;
        })
      );
    });

//SOLUTION 2
//jshint esversion:6

function uniteUnique(...arrays) {
    //make an array out of the given arrays and flatten it (using the spread operator)
    const flatArray = [].concat(...arrays);
  
    // create a Set which clears any duplicates since it's a regular set and not a multiset
    return [...new Set(flatArray)];
  }
  
  // test here
  uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);