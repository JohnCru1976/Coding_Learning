import Data.Char
main::IO()
main = do
    -- The filter function works by keeping only the elements of the list that pass the test
    -- Examples
    print(filter even [1,2,3,4]) -- [2,4]
    print(filter (\(x:xs) -> x == 'a') ["apple","Banana","avocado"]) -- ["apple","avocado"]
    print(filter (\(x:xs) -> x == toUpper x) ["apple","Banana","avocado"]) -- ["Banana"]
    -- Same examples with myFilter definition
    print(myFilter even [1,2,3,4]) -- [2,4]
    print(myFilter (\(x:xs) -> x == 'a') ["apple","Banana","avocado"]) -- ["apple","avocado"]
    print(myFilter (\(x:xs) -> x == toUpper x) ["apple","Banana","avocado"]) -- ["Banana"]

-- This is the definition of myFilter
-- f is the function that we use as a callback. It is used as a test
myFilter f [] = []
myFilter f (x:xs) = if f x -- If x (the element) pass the function returns true
                    then x:myFilter f xs -- cons x with filtering the rest of the list
                    else myFilter f xs -- x is not consed with the rest of the list
