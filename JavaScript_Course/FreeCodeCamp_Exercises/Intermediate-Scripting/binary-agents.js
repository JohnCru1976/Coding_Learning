/*
Binary Agents
Return an English translated sentence of the passed binary string.
The binary string will be space separated.
*/

// PERSONAL SOLUTION
function binaryAgent(str) {   
    function binToDecimal (str){
      let sum=0;
      for(let i = str.length - 1; i >= 0 ; i--){      
        sum += parseInt(str[str.length-1-i])*(2**i);
      }
      return sum;
    } 
  
    return str.split(" ")
              .map(function(elem){
                  return String.fromCharCode(binToDecimal(elem));
               })
              .join("");
  }
  
  console.log(binaryAgent("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001"));

  // SOLUTION 1
  function binaryAgent(str) {
    var biString = str.split(" ");
    var uniString = [];
  
    /*using the radix (or base) parameter in parseInt, we can convert the binary
        number to a decimal number while simultaneously converting to a char*/
  
    for (var i = 0; i < biString.length; i++) {
      uniString.push(String.fromCharCode(parseInt(biString[i], 2)));
    }
  
    // we then simply join the string
    return uniString.join("");
  }
  
  // test here
  binaryAgent(
    "01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"
  );

  // SOLUTION 2
  function binaryAgent(str) {
    // Separate the binary code by space.
    str = str.split(" ");
    var power;
    var decValue = 0;
    var sentence = "";
  
    // Check each binary number from the array.
    for (var s = 0; s < str.length; s++) {
      // Check each bit from binary number
      for (var t = 0; t < str[s].length; t++) {
        // This only takes into consideration the active ones.
        if (str[s][t] == 1) {
          // This is quivalent to 2 ** position
          power = Math.pow(2, +str[s].length - t - 1);
          decValue += power;
  
          // Record the decimal value by adding the number to the previous one.
        }
      }
  
      // After the binary number is converted to decimal, convert it to string and store
      sentence += String.fromCharCode(decValue);
  
      // Reset decimal value for next binary number.
      decValue = 0;
    }
  
    return sentence;
  }
  
  // test here
  binaryAgent(
    "01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"
  );