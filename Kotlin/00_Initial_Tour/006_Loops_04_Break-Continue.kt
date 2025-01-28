/*
    28-01-2025
    Break - Continue - @ Annotation
 */

 fun main(){
    breakExample()
 }

// BREAK
 fun breakExample(){
    println("BREAK EXAMPLE")
    var j=10

    for(i in 0..100){
        j+=j

        if(j>100){
            break
        }
    }

    println("j=$j")
 }

 // CONTINUE
 fun continueExample(){
    println("CONTINUE EXAMPLE")
    var i = 1

    while(i<20){
        i+=1

        if(i % 2 != 0){ // Odd number
            continue // Continue if odd
        }

        println("i = $i") // Only even numbers
    }
 }

 // BREAK AND CONTINUE LABELS
 fun labelsExample(){
    println("LABES EXAMPLE")

    outerloop@ for(i in 1..100){
        println("Outer loop i=$i")

        for(j in 1..100){
            println("Inner loop j=$j")
            if(j==10) break@outerloop            
        }
    }
 }