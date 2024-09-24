/*
MAPS
- Every key in a map must be unique so that Kotlin 
    can understand which value you want to get.
- You can have duplicate values in a map.
*/

fun main(){
    // *** Read-only map ***
    val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(readOnlyJuiceMenu)
    // {apple=100, kiwi=190, orange=100}

    // *** Mutable map with explicit type declaration ***
    val juiceMenu: MutableMap<String, Int> = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(juiceMenu)
    // {apple=100, kiwi=190, orange=100}

    // To prevent unwanted modifications, 
    // you can create a read-only view 
    // of a mutable map by assigning it to a Map
    val juiceMenuLocked: Map<String, Int> = juiceMenu

    // *** ACCESS Indexed Access Operator []***
    // To access a value in a map, use the indexed access operator [] with its key:
    // Read-only map
    println("The value of apple juice is: ${readOnlyJuiceMenu["apple"]}")
    // The value of apple juice is: 100

    // If you try to access a key-value pair with a key 
    // that doesn't exist in a map, you see a null value:
    // Read-only map
    println("The value of pineapple juice is: ${readOnlyJuiceMenu["pineapple"]}")
    // The value of pineapple juice is: null

    // *** ADD ***
    juiceMenu["coconut"] = 150 // Add key "coconut" with value 150 to the map
    println(juiceMenu)
    // {apple=100, kiwi=190, orange=100, coconut=150}

    // *** REMOVE ***
    juiceMenu.remove("orange")    // Remove key "orange" from the map
    println(juiceMenu)
    // {apple=100, kiwi=190}

    // *** COUNT ***
    // Read-only map
    println("This map has ${readOnlyJuiceMenu.count()} key-value pairs")
    // This map has 3 key-value pairs

    // *** CHECK KEY ***
    println(readOnlyJuiceMenu.containsKey("kiwi"))
    // true
}

