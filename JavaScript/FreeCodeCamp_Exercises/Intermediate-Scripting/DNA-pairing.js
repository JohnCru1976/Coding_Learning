/*  
DNA Pairing
The DNA strand is missing the pairing element. Take each character, get its pair,
and return the results as a 2d array.
Base pairs are a pair of AT and CG. Match the missing element to the provided character.
Return the provided character as the first element in each array.
For example, for the input GCG, return [["G", "C"], ["C","G"], ["G", "C"]]
The character and its pair are paired up in an array, and all the arrays are 
grouped into one encapsulating array.
*/

// PERSONAL SOLUTION
function pairElement(str) {
    const arrayStr = str.split("");
    return arrayStr.map(element=>
      [element,adnPair(element)]
    );
  }
  
  function adnPair(element){
    switch (element){
        case 'A':
          return 'T'
        case 'T':
          return 'A';        
        case 'C':
          return 'G';        
        case 'G':
          return 'C';        
        default:
          return ''
    }
  }
  
  console.log(pairElement("GCG"));

  // SOLUTION 1
  function pairElement(str) {
    // Return each strand as an array of two elements, the original and the pair.
    var paired = [];
  
    // Function to check with strand to pair.
    var search = function(char) {
      switch (char) {
        case "A":
          paired.push(["A", "T"]);
          break;
        case "T":
          paired.push(["T", "A"]);
          break;
        case "C":
          paired.push(["C", "G"]);
          break;
        case "G":
          paired.push(["G", "C"]);
          break;
      }
    };
  
    // Loops through the input and pair.
    for (var i = 0; i < str.length; i++) {
      search(str[i]);
    }
  
    return paired;
  }

  //SOLUTION 2
  function pairElement(str) {
    //create object for pair lookup
    var pairs = {
      A: "T",
      T: "A",
      C: "G",
      G: "C"
    };
    //split string into array of characters
    var arr = str.split("");
    //map character to array of character and matching pair
    return arr.map(x => [x, pairs[x]]);
  }

