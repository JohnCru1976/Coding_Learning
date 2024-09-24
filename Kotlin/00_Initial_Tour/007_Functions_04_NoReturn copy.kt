/* If your function doesn't return a useful value then its return type is Unit. 
Unit is a type with only one value – Unit. 
You don't have to declare that Unit is returned explicitly in your function body. 
This means that you don't have to use the return keyword or declare a return type */

fun printMessage(message: String) {
    println(message)
    // `return Unit` or `return` is optional
}

fun main() {
    printMessage("Hello")
    // Hello
    println(printMessage(""))
    // kotlin.Unit
}