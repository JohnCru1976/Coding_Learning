/*
    SETS
    Whereas lists are ordered and allow duplicate items, 
    sets are unordered and only store unique items.
    As sets are unordered, you can't access an item at a particular index.
 */
 
fun main(){
    // Read-only set
    val readOnlyFruit = setOf("apple", "banana", "cherry", "cherry")
    // Mutable set with explicit type declaration
    val fruit: MutableSet<String> = mutableSetOf("apple", "banana", "cherry", "cherry")

    println(readOnlyFruit)
    // [apple, banana, cherry]

    // To prevent unwanted modifications, 
    // you can create a read-only view of a mutable set 
    // by assigning it to a Set:
    val fruitLocked: Set<String> = fruit

    // *** Count function ***
    println("This set has ${readOnlyFruit.count()} items")
    // This set has 3 items

    // *** in operator (returns true-false) ***
    println("banana" in readOnlyFruit)
    // true

    // *** add-remove ***
    fruit.add("dragonfruit")    // Add "dragonfruit" to the set
    println(fruit)              // [apple, banana, cherry, dragonfruit]

    fruit.remove("dragonfruit") // Remove "dragonfruit" from the set
    println(fruit)              // [apple, banana, cherry]
}
