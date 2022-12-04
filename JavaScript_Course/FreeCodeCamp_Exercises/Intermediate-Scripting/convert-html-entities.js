/*
Convert HTML Entities
Convert the characters &, <, >, " (double quote),
and ' (apostrophe), in a string to their corresponding HTML entities.
*/

//PERSONAL SOLUTION
const characters = {
    38: "&amp;",
    60: "&lt;",
    62: "&gt;",
    34: "&quot;",
    39: "&apos;"
};

function convertHTML(str) {
 
 const finalArray = []; 
 for(let i = 0; i < str.length; i++){
   if(characters.hasOwnProperty(str.charCodeAt(i))){
     finalArray.push(characters[str.charCodeAt(i)]);
   }else{
     finalArray.push(str[i]);
   }
 }
 return finalArray.join("");
}

console.log(convertHTML('Stuff in "quotation marks"'));

// SOLUTION 1
function convertHTML(str) {
    // Split by character to avoid problems.
  
    var temp = str.split("");
  
    // Since we are only checking for a few HTML elements, use a switch
  
    for (var i = 0; i < temp.length; i++) {
      switch (temp[i]) {
        case "<":
          temp[i] = "&lt;";
          break;
        case "&":
          temp[i] = "&amp;";
          break;
        case ">":
          temp[i] = "&gt;";
          break;
        case '"':
          temp[i] = "&quot;";
          break;
        case "'":
          temp[i] = "&apos;";
          break;
      }
    }
  
    temp = temp.join("");
    return temp;
  }
  
  //test here
  convertHTML("Dolce & Gabbana");

  // SOLUTION 2
  function convertHTML(str) {
    // Use Object Lookup to declare as many HTML entities as needed.
    const htmlEntities = {
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&apos;"
    };
    // Using a regex, replace characters with it's corresponding html entity
    return str.replace(/([&<>\"'])/g, match => htmlEntities[match]);
  }
  
  // test here
  convertHTML("Dolce & Gabbana");

  // SOLUTION 3
  function convertHTML(str) {
    // Use Object Lookup to declare as many HTML entities as needed.
    const htmlEntities = {
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&apos;"
    };
    //Use map function to return a filtered str with all entities changed automatically.
    return str
      .split("")
      .map(entity => htmlEntities[entity] || entity)
      .join("");
  }
  
  // test here
  convertHTML("Dolce & Gabbana");