/*
Smallest Common Multiple
Find the smallest common multiple of the provided parameters 
that can be evenly divided by both, as well as by all sequential 
numbers in the range between these parameters.
The range will be an array of two numbers that will not necessarily be in numerical order.
For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 
that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.
*/

// PERSONAL SOLUTION
function smallestCommons(arr) {
    //Sorting both numbers
    arr.sort((a,b)=>a-b);
    //Initial Number candidate to be SCM
    let numSCM = arr[1];
    // Function returning true if the number
    // acomplish the requisits
    function isDivisible (num){    
      for(let i = arr[0]; i <= arr[1];i++){
        if(num % i != 0){return false;}
      }
      return true;
    }
    //Loop that tests until the numSCM acomplish
    // the requisits
    while(!isDivisible(numSCM)){
      numSCM++
    }
    
    return numSCM;
  }
  
  console.log(smallestCommons([2, 12]));

  // SOLUTION 1
  function smallestCommons(arr) {
    // Setup
    const [min, max] = arr.sort((a, b) => a - b);
    const numberDivisors = max - min + 1;
    // Largest possible value for SCM
    let upperBound = 1;
    for (let i = min; i <= max; i++) {
      upperBound *= i;
    }
    // Test all multiples of 'max'
    for (let multiple = max; multiple <= upperBound; multiple += max) {
      // Check if every value in range divides 'multiple'
      let divisorCount = 0;
      for (let i = min; i <= max; i++) {
        // Count divisors
        if (multiple % i === 0) {
          divisorCount += 1;
        }
      }
      if (divisorCount === numberDivisors) {
        return multiple;
      }
    }
  }
  
  smallestCommons([1, 5]);

  // SOLUTION 2
  function smallestCommons(arr) {
    // Setup
    const [min, max] = arr.sort((a, b) => a - b);
    const range = Array(max - min + 1)
      .fill(0)
      .map((_, i) => i + min);
    // Largest possible value for SCM
    const upperBound = range.reduce((prod, curr) => prod * curr);
    // Test all multiples of 'max'
    for (let multiple = max; multiple <= upperBound; multiple += max) {
      // Check if every value in range divides 'multiple'
      const divisible = range.every((value) => multiple % value === 0);
      if (divisible) {
        return multiple;
      }
    }
  }
  
  smallestCommons([1, 5]);

  // SOLUTION 3
  function smallestCommons(arr) {
    // Setup
    const [min, max] = arr.sort((a, b) => a - b);
    const range = Array(max - min + 1)
      .fill(0)
      .map((_, i) => i + min);
    // GCD of two numbers
    // https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm
    const gcd = (a, b) => (b === 0) ? a : gcd(b, a % b);
    // LCM of two numbers
    // https://en.wikipedia.org/wiki/Least_common_multiple#Using_the_greatest_common_divisor
    const lcm = (a, b) => a * b / gcd(a, b);
    // LCM of multiple numbers
    // https://en.wikipedia.org/wiki/Least_common_multiple#Other
    return range.reduce((multiple, curr) => lcm(multiple, curr));
  }
  
  smallestCommons([1, 5]);

  // SOLUTION 4
  // Find the SCM of a range of numbers
function smallestCommons(arr) {
    let primeFactors = {};
    const [min, max] = arr.sort((a, b) => a - b);
    for (let i = min; i <= max; i++) {
      // Factorize number in range
      let primes = getPrimeFactors(i);
      for (let j in primes) {
        // Add factor to set or update number of occurrences
        if (!primeFactors[j] || primes[j] > primeFactors[j]) {
          primeFactors[j] = primes[j]
        }
      }
    }
    // Build SCM from factorization
    let multiple = 1;
    for (let i in primeFactors) {
      multiple *= i ** primeFactors[i]
    }
    return multiple;
  }
  
  // Compute prime factors of a number
  function getPrimeFactors(num) {
    const factors = {};
    for (let prime = 2; prime <= num; prime++) {
      // Count occurances of factor
      // Note that composite values will not divide num
      while ((num % prime) === 0) {
        factors[prime] = (factors[prime]) ? factors[prime] + 1 : 1;
        num /= prime;
      }
    }
    return factors;
  }
  
  smallestCommons([1, 5]);