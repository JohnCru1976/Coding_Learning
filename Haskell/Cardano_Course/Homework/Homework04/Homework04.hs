
import Distribution.Simple.Utils (xargs)
main :: IO()
main = do
    print (getFour nested)
    
    print (remove3 [1,2,3,4,5])
    print (remove3 [2,5,3])
    print (remove3 [2,5])

    print (remove3' [1,2,3,4,5])
    print (remove3' [2,5,3])
    print (remove3' [2,5])

    print (take3 (4,5,8))

    print (checkList [1,2,3,4,5])
    print (checkList [2,5,3])
    print (checkList [])

    print (tail' [1,2,3,4,5])
    print (tail' [2,5,3])
    print (tail' [1])

    print (addOneIfEven 4)
    print (addOneIfEven 3)

-- Question 1
-- Lets say you have the nested values defined bellow. How would you get the value of
-- 4 by using only pattern matching in a function?

nested :: [([Int], [Int])]
nested = [([1,2],[3,4]), ([5,6],[7,8])]
-- This my solution
-- getFour [([_,_],[_,x]),([_,_],[_,_])] = x
-- Correct solution
getFour [(_,[_,x]), _] = x
getFour _ = 0

-- Question 2
-- Write a function that takes a list of elements of any type and, if the list has 3 or more elements, it
-- removes them. Else, it does nothing. Do it two times, one with multiple function definitions and one with
-- case expressions.
{- This was my solution (it doesn't function) 
    remove3 (_:_:_:[xs]) = [xs]
    remove3 _ = []
-}
-- With multiple function definitions
remove3 (_:_:_:xs) = xs -- xs represents a list, it isn't needed to use brackets []
remove3 x = x -- "it does nothing" means that the function returns de same result

-- With case expressions
remove3' list = case list of
    (_:_:_:xs) -> xs
    x -> x

-- Question 3
-- Create a function that takes a 3-element tuple (all of type Integer) and adds (sum) them together
take3 :: (Int, Int, Int) -> Int
take3 (x,y,z) = x+y+z

-- Question 4
-- Implement a function that returns True if a list is empty and False otherwise.
checkList :: [a] -> Bool
checkList [] = True
checkList _ = False

checkList'' :: [a] -> Bool
checkList'' []    =  True
checkList'' (_:_) =  False

-- Question 5
-- Write the implementation of the tail function using pattern matching. But, instead of failing if
-- the list is empty, return an empty list.
tail' :: [a] -> [a]
tail' (x:xs) = xs
tail' [] = []


-- Question 6
-- write a case expression wrapped in a function that takes an Int and adds one if it's even. Otherwise does nothing. 
-- (Use the `even` function to check if the number is even.)
    {- My solution
        addEvenOne x = case mod x 2 /= 0 of
        True -> x + 1
        False -> x
    -}


addOneIfEven :: Int -> Int
addOneIfEven n = case even n of
    True  -> n + 1
    False -> n