/*
Map the Debris
Return a new array that transforms the elements' average altitude 
into their orbital periods (in seconds).
The array will contain objects in the format {name: 'name', avgAlt: avgAlt}.
You can read about orbital periods on Wikipedia.
The values should be rounded to the nearest whole number. 
The body being orbited is Earth.
The radius of the earth is 6367.4447 kilometers, and the GM value of earth is 398600.4418 km3s-2.
*/

// PERSONAL SOLUTION
function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    return arr.map(elem =>{
      let obj = {};
      obj.name = elem.name;
      obj.orbitalPeriod = Math.round(Math.sqrt(Math.pow(earthRadius+elem.avgAlt,3)/GM)*2*Math.PI);
      return obj;
    });
  }
  
  console.log(orbitalPeriod([{name: "iss", avgAlt: 413.6}, {name: "hubble", avgAlt: 556.7}, {name: "moon", avgAlt: 378632.553}]));

  // SOLUTION 1
  function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    const a = 2 * Math.PI;
    const newArr = [];
  
    const getOrbPeriod = function(obj) {
      const c = Math.pow(earthRadius + obj.avgAlt, 3);
      const b = Math.sqrt(c / GM);
      const orbPeriod = Math.round(a * b);
      // create new object
      return {name: obj.name, orbitalPeriod: orbPeriod};
    };
  
    for (let elem in arr) {
      newArr.push(getOrbPeriod(arr[elem]));
    }
  
    return newArr;
  }

  // SOLUTION 2
  function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    const newArr = [];
  
    //Looping through each key in arr object
    for (let elem in arr) {
      //Rounding off the orbital period value
      const orbitalPer = Math.round(
        2 * Math.PI * Math.sqrt(Math.pow(arr[elem].avgAlt + earthRadius, 3) / GM)
      );
      //Adding new object with orbitalPeriod property
      newArr.push({name: arr[elem].name, orbitalPeriod: orbitalPer});
    }
  
    return newArr;
  }

  // SOLUTION 3
  function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    // Create new array to prevent modification of the original
    const newArr = JSON.parse(JSON.stringify(arr));
    // Loop through each item in the array arr
    newArr.forEach(function(item) {
      // Calculate the Orbital period value
      const tmp = Math.round(
        2 * Math.PI * Math.sqrt(Math.pow(earthRadius + item.avgAlt, 3) / GM)
      );
      //Delete the avgAlt property
      delete item.avgAlt;
      //Add orbitalPeriod property
      item.orbitalPeriod = tmp;
    });
  
    return newArr;
  }

  // SOLUTION 4
  function orbitalPeriod(arr) {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    return arr.map(({ name, avgAlt }) => {
      const earth = earthRadius + avgAlt;
      const orbitalPeriod = Math.round(2 * Math.PI * Math.sqrt(Math.pow(earth, 3)/GM));
      return { name, orbitalPeriod };
    });
  }
  