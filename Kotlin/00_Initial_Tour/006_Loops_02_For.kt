/* 
*** FOR ***
Use FOR to iterate over a range of values and perform an action. 
Use WHILE to continue an action until a particular condition is satisfied.
 */

 fun main(){
    // *** FOR ***
    for (number in 1..5) { 
    // number is the iterator and 1..5 is the range
    print(number)
    }
    // 12345

    // COLLECTION ITERATIONS
    val cakes = listOf("carrot", "cheese", "chocolate")
    for (cake in cakes) {
        println("Yummy, it's a $cake cake!")
    }
    // Yummy, it's a carrot cake!
    // Yummy, it's a cheese cake!
    // Yummy, it's a chocolate cake!

    
 }