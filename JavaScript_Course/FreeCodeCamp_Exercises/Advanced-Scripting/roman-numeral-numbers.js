/*
Roman Numeral Converter
Convert the given number into a roman numeral.
All roman numerals answers should be provided in upper-case.
*/

//PERSONAL SOLUTION
function convertToRoman(num) {
    //Convert to string and reverse
    const numStrReverse = num.toString().split("").reverse();
    //Sets of roman numerals
    const setRomans = [["I","V","X"],["X","L","C"],["C","D","M"],["M","~V","~X"]];
    //Function that converts the numeral acording its position
    const convertNumeral = function(num,pos){
      switch (num){
        case 1:
          return setRomans[pos][0];
          break;
        case 2:
          return setRomans[pos][0]+setRomans[pos][0];
          break;
        case 3:
          return setRomans[pos][0]+setRomans[pos][0]+setRomans[pos][0];
          break;
        case 4:
          return setRomans[pos][0]+setRomans[pos][1];
          break;
        case 5:
          return setRomans[pos][1]
          break;
        case 6:
          return setRomans[pos][1] + setRomans[pos][0];
          break;
        case 7:
           return setRomans[pos][1]+setRomans[pos][0]+setRomans[pos][0];
          break;
        case 8:
          return setRomans[pos][1]+setRomans[pos][0]+setRomans[pos][0]+setRomans[pos][0];
          break;
        case 9:
          return setRomans[pos][0]+setRomans[pos][2];
          break;
      }
    };
   return numStrReverse
          .map((elem,id)=>convertNumeral(parseInt(elem),id))
          .reverse()
          .join("");
  }
  
  console.log(convertToRoman(3999));

  
