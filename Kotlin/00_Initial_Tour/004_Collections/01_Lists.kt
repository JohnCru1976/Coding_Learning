/*
Lists store items in the order that they are added.
Allow for duplicate items.
 */

fun main(){
    // *** Read only list (listOf) ***
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println(readOnlyShapes)
    // [triangle, square, circle]

    // *** Mutable list with explicit type declaration ***
    val shapes: MutableList<String> = mutableListOf("circle", "square", "triangle")
    println(shapes)
    // [triangle, square, circle]

    // To prevent unwanted modifications, 
    // you can create a read-only view 
    // of a mutable list by assigning it to a List:
    val shapesLocked: List<String> = shapes
    println(shapesLocked)

    // *** Access to elements ***
    println("The second item in the list is: ${readOnlyShapes[1]}")
    // The first item in the list is: square

    // *** first - last methods (extension functions according the manual) ***
    println("The first item in the list is: ${shapesLocked.first()}")
    // The last item in the list is: circle
    println("The last item in the list is: ${shapesLocked.last()}")
    // The last item in the list is: triangle

    // *** count method ***
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println("This list has ${readOnlyShapes.count()} items")
    // This list has 3 items

    // *** in operator (returns true-false) ***
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println("circle" in readOnlyShapes)
    // true

    // *** Add - Remove ***
    // *** Add "pentagon" to the list *** 
    shapes.add("pentagon") 
    println(shapes)  
    // [triangle, square, circle, pentagon]

    // *** Remove the first "pentagon" from the list ***
    shapes.remove("pentagon") 
    println(shapes)  
    // [triangle, square, circle]
}