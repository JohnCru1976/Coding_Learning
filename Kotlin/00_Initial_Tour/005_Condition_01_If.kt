/*
If you have to choose between IF and WHEN, we recommend using when because it:
Makes your code easier to read.
Makes it easier to add another branch.
Leads to fewer mistakes in your code.
*/

fun main(){
    // *** IF ***
    val d: Int
    val check = true

    if (check) {
        d = 1
    } else {
        d = 2
    }

    println(d)
    // 1

    // There is NO TERNARY OPERATOR condition ? then : else in Kotlin.
    val a = 1
    val b = 2

    println(if (a > b) a else b) // Returns a value: 2
}
