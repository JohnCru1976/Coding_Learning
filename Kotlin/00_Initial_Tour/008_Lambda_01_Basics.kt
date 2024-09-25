/*
Lambda expressions can be used in a number of ways. You can:
- Pass a lambda expression as a parameter to another function
- Return a lambda expression from a function
- Invoke a lambda expression on its own 
*/

// FirstExample
fun firstExample() {
    // Lambda expression
    val upperCaseString = { text: String -> text.uppercase() }
    println(upperCaseString("hello"))
    // HELLO
}

// Lambda as parameter to another function with FILTER
fun lambdaAsParameterFilter () {
    val numbers = listOf(1, -2, 3, -4, 5, -6)

    // The .filter() function accepts a lambda expression as a predicate:
    // Takes each element of the list and returns only those that are positive
    val positives = numbers.filter ({ x -> x > 0 })

    // Takes each element of the list and returns only those that are negative
    val isNegative = { x: Int -> x < 0 }
    val negatives = numbers.filter(isNegative)

    println(positives)
    // [1, 3, 5]
    println(negatives)
    // [-2, -4, -6]
}

// Lambda as parameter to another function with MAP
fun lambdaAsParameterMap () {
    val numbers = listOf(1, -2, 3, -4, 5, -6)
    val doubled = numbers.map { x -> x * 2 }

    val isTripled = { x: Int -> x * 3 }
    val tripled = numbers.map(isTripled)

    println(doubled)
    // [2, -4, 6, -8, 10, -12]
    println(tripled)
    // [3, -6, 9, -12, 15, -18]
}

// *** DEFINING FUNCTION TYPES ***
fun functionTypes(){

    val upperCaseString: (String) -> String = { text -> text.uppercase() }

    println(upperCaseString("hello"))
    // HELLO
}

// *** RETURN FROM A FUNCTION ***
// Lambda expressions can be returned from a function. 
// So that the compiler understands what type the lambda expression returned is, 
// you must declare a function type.
// EXAMPLE
fun toSeconds(time: String): (Int) -> Int = when (time) {
    "hour" -> { value -> value * 60 * 60 }
    "minute" -> { value -> value * 60 }
    "second" -> { value -> value }
    else -> { value -> value }
}

fun main() {
    val timesInMinutes = listOf(2, 10, 15, 1)
    val min2sec = toSeconds("minute")
    val totalTimeInSeconds = timesInMinutes.map(min2sec).sum()
    println("Total time is $totalTimeInSeconds secs")
    // Total time is 1680 secs
}

