/*
Spinal Tap Case
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
spinalCase("This Is Spinal Tap") should return the string this-is-spinal-tap.
*/

// PERSONAL SOLUTION
function spinalCase(str) {
    return str.match(/[A-z][a-z]+/g)
              .join("-")
              .toLowerCase()
              .trim();
}

// SOLUTION 1
function spinalCase(str) {
    // Create a variable for the white space and underscores.
    var regex = /\s+|_+/g;
  
    // Replace low-upper case to low-space-uppercase
    str = str.replace(/([a-z])([A-Z])/g, "$1 $2");
  
    // Replace space and underscore with -
    return str.replace(regex, "-").toLowerCase();
  }

// SOLUTION 2
function spinalCase(str) {
    // Replace low-upper case to low-space-uppercase
    str = str.replace(/([a-z])([A-Z])/g, "$1 $2");
    // Split on whitespace and underscores and join with dash
    return str
      .toLowerCase()
      .split(/(?:_| )+/)
      .join("-");
  }
  
// SOLUTION 3
function spinalCase(str) {
    // "It's such a fine line between stupid, and clever."
    // --David St. Hubbins
  
    return str
      .split(/\s|_|(?=[A-Z])/)
      .join("-")
      .toLowerCase();
  }