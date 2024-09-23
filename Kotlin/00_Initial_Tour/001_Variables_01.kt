// Val - Read Only
// Var - Mutable
/* Variables can be declared outside the main() function 
at the beginning of your program. Variables declared in 
this way are said to be declared at top level. */

val popcorn = 5    // There are 5 boxes of popcorn
val hotdog = 7     // There are 7 hotdogs
var customers = 10 // There are 10 customers in the queue

fun main(){
    // Some customers leave the queue
    customers = 8
    println(customers)
    // 8
}