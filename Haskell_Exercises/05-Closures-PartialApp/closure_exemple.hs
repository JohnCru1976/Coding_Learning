main :: IO()
-- CLOSURE: a value (parameter) captured inside a lambda function
main = do
  -- Solution 1 without closure
  print (ifEven double 2)
  -- Solution 2 without closure
  print (ifEvenDouble 2)
  -- Solution with closure
  print (ifEvenDouble2 2)


-- THIS IS A PREVIOUS EXAMPLE
ifEven myFunction x = if even x
                      then myFunction x
                      else x
-- Now we can pass a function with the necessary operations

-- Here we are defining the three operations of the begining
inc x = x + 1
double x = x * 2
square x = x ^ 2

-- Here we build three specific functions
ifEvenInc = ifEven inc
ifEvenDouble = ifEven double
ifEvenSquare = ifEven square

-- In the previous functions we found a pattern  funcName [x] = ifEven f [x]
genIfEven = ifEven -- This is the same that the next line 
-- (I don't know if this makes any sense) Doubts
-- genIfEven f = (\x -> ifEven f x) -- The f parameter is a CLOSURE

-- Now we build the three specific funtions
ifEvenInc2 = genIfEven inc
ifEvenDouble2 = genIfEven double
ifEvenSquare2 = genIfEven square
