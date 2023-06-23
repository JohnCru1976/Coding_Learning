// Anything following double slashes is an English-language comment.
// Read the comments carefully: they explain the JavaScript code.

// A variable is a symbolic name for a value.
// Variables are declared with the let keyword:
let x;   // Declared a variable named x.

// Values can be assigned to variables with an = sign
x = 0;   // Now the variable x has the value 0
x        // => 0: A variable evaluates to its value.

// JavaScript supports several types of values
x = 1;   // Numbers
x = 0.01 // Numbers can be integers or reals
x = "hello world";   // Strings of text in quotation marks.
x = 'JavaScript';   // Single quote marks also delimit strings.
x = true;   // A Boolean value
x = false;  //  The other Boolean value
x = null;   // Null is a special value that means "no value"
x = undefined;   // Undefined is another special value like null

// JavaScript's most important datatype is the object.
// An object is a collection of name/value pairs, or a string to value map.
let book = {    // Objects are enclosed in curly braces
   topic: "JavaScript",   // The property "topic" has value "JavaScript"
   edition: 7   // The property "edition" has value 7
};   // The curly brace marks the end of the object

// Access the properties of an object with . or []
book.topic  // => "JavaScript"
book["edition"]  // => 7 another way to access property values
book.author = "Flanagan"  // Create new properties by assignemt
book.contents = {};   // {} is an empty object with no properties

// Conditionally access properties with ? (ES2020)
book.contents?.ch01?.sect1  // => undefined: book.contents has no ch01 property
// JavaScript also supports arrays (numerically indexed lists) of values
let primes = [2, 3, 5, 7]  // An array of 4 values, delimited with [ and ]
primes[0]   // => 2: the first element (index 0) of the array
primes.lenght    // => 4: how many elements in the array
primes[primes.length-1]  // => 7: the las element of the array
primes[4] = 9;   // Add a new alement by assignment
primes[4] = 11;   // Or alter an existing element by assignment
let empty = [];  // [] is an empty array with no elements
empty.length   // => 0

// Arrays anf objects can hold other arrays and objects:
let points = [  // An array with 2 elements
   {x: 0, y: 0},  // Each element is an object
   {x: 1, y: 1}
];
let data = {  // An object with 2 properties
   trial1: [[1,2],[3,4]], // The value of each property is an array
   trial2: [[2,3],[4,5]]  // The elements of the arrays are arrays
};

// Operators act on values (the operands) to produce a new value
// Arithmetic operators are some of the simplest:
3 + 2  // => 5: addition
3 - 2  // => 1: subtraction
3 * 2  // => 6: multiplication
3 / 2  // => 1.5: division
points[1].x - points[0].x  // => 1: more complicated operands also work
"3" + "2"   // "32":  + adds numbers, concatenates strings

// JavaScript defines some shorthand arithmetic operators
let count = 0;   // Define a variable
count++;   // Increment the variable
count--;   // Decrement the variable
count += 2;  // Add 2: same as count = count + 2
count *= 3;  // Multiply by 3: sames as count = count * 3;
count  // => 6: variable names are expressions, too

// Equality and relational operators test whether two values are equal,
// unequal, less than, greater than, and so on. They evaluate to true or false.
let x = 2, y = 3;   // These = signs are assignment, not equality tests
x === y   // => false: equality
x !== y   // => true: inequality
x < y   // => true: less-than
x <= y   // => true: less-than or equal
x > y   // => false: greater-than
x >= y   // => false: greater-than or equal
"two" === "three"  // => false: the two strings are different
"two" > "three"  // => true: "tw" is alphabetically greater than "th"
false === (x > y)   // => true: false is equal to false

// Logical operators combine or invert boolean values
(x === 2) && (y === 3)  // => true: both comparisons are true. && is AND
(x > 3) || (y < 3)  // => false: neither comparison is true. || is or
!(x === y)   // => true: ! inverts a boolean value
