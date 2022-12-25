main :: IO()
main = do
  -- Normal functions
  print (ifEvenInc 2)
  print (ifEvenDouble 2)
  print (ifEvenSquare 2)
  -- Functions that receive a function as parameter (first-class functions)
  print (ifEven inc 2)
  print (ifEven double 2)
  print (ifEven square 2)
  -- We can pass a lambda too
  print (ifEven (+1) 2) -- (+1) represents the lambda (\x -> x + 1)
  -- We could use the function INC --- (inc x) is equal to (x + 1)
  print (ifEven (*2) 2) -- (*2) represents the lambda (\x -> x * 2)
  print (ifEven (^2) 2) -- (^2) represents the lambda (\x -> x ^ 2)
 
-- Here we use three different functions with similar structure
ifEvenInc x = if even x
              then x + 1
              else x
ifEvenDouble x = if even x
                 then x * 2
                 else x
ifEvenSquare x = if even x
                 then x ^ 2
                 else x
-- We found the common expressions on the three functions and going to make an abstraction
-- The new function is this:
ifEven myFunction x = if even x
                      then myFunction x
                      else x
-- Now we can pass a function with the necessary operations
-- Here we are defining the three operations of the begining
inc x = x + 1
double x = x * 2
square x = x ^ 2
-- Now I can pass these functions to the ifeven function (these are firs-class functions)
-- Examples at the main-do