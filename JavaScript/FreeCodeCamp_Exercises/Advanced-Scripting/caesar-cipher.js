/*
Caesars Cipher
One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. 
In a shift cipher the meanings of the letters are shifted by some set amount.
A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places.
Thus A ↔ N, B ↔ O and so on.
Write a function which takes a ROT13 encoded string as input and returns a decoded string.
All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), 
but do pass them on.
*/

//PERSONAL SOLUTION 1
function rot13(str) {
    const splitStr = str.split("");
    return splitStr.map(elem => {
      let ascii = elem.charCodeAt(0);
      if (ascii >= 65 && ascii <= 90){
        if(ascii+13>90){
         return String.fromCharCode(65+(13-(91-ascii)));
        }else{
          return String.fromCharCode(ascii+13);
        }
      }else{
        return elem;
      }
    }).join("");
  }
  
  console.log(rot13("SERR CVMMN!"));

  //PERSONAL SOLUTION 2
  function rot13(str) {
    const ROT_NUMBER = 13;
    const splitStr = str.split("");
    return splitStr.map(elem => {
      let ascii = elem.charCodeAt(0);
      if (ascii >= 65 && ascii <= 90){
        if(ascii+ROT_NUMBER>90){
         return String.fromCharCode(ascii-ROT_NUMBER);
        }else{
          return String.fromCharCode(ascii+ROT_NUMBER);
        }
      }else{
        return elem;
      }
    }).join("");
  }
  
  console.log(rot13("SERR PBQR PNZC"));