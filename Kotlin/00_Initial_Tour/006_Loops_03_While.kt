/*
*** WHILE ***
while can be used in two ways:
-To execute a code block while a conditional expression is true. (WHILE)
-To execute the code block first and then check the conditional expression. (DO-WHILE)
 */

 fun main(){
    // *** WHILE ***
    var cakesEaten = 0
    while (cakesEaten < 3) {
        println("Eat a cake")
        cakesEaten++
    }
    // Eat a cake
    // Eat a cake
    // Eat a cake

    // *** DO-WHILE ***
    var cakesBaked = 0
    do {
        println("Bake a cake")
        cakesBaked++
    } while (cakesBaked < cakesEaten)
    // Bake a cake
    // Bake a cake
    // Bake a cake
 }