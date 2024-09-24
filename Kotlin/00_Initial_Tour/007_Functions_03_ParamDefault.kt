// The second parameter is set by default with the string "Info"
fun printMessageWithPrefix(message: String, prefix: String = "Info") {
    println("[$prefix] $message")
}

fun main() {
    // Function called with both parameters
    printMessageWithPrefix("Hello", "Log") 
    // [Log] Hello
    
    // Function called only with message parameter
    printMessageWithPrefix("Hello")        
    // [Info] Hello
    
    // Named parameter
    printMessageWithPrefix(prefix = "Log", message = "Hello")
    // [Log] Hello
}

/* You can skip specific parameters with default values, 
rather than omitting them all. However, after the first skipped parameter, 
you must name all subsequent parameters. */