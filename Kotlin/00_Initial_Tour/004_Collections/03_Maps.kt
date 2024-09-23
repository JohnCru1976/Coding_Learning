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

    // *** ACCESS ***
    // To access a value in a map, use the indexed access operator [] with its key:
    // Read-only map
    println("The value of apple juice is: ${readOnlyJuiceMenu["apple"]}")
    // The value of apple juice is: 100
}

