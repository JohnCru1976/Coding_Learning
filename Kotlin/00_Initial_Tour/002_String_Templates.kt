val customers = 10  // Top level variable

fun main(){
    println("There are $customers customers")
    // There are 10 customers

    println("There are ${customers + 1} customers")
    // There are 11 customers

    // UPPERCASE - LOWERCASE (METHODS)
    val word: String = "Hello"
    println("${word.uppercase()}")
    println("${word.lowercase()}")
}
