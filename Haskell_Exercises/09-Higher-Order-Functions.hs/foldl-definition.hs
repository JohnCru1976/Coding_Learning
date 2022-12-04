{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
import System.Win32 (COORD(x))
{-# HLINT ignore "Eta reduce" #-}
{-# HLINT ignore "Use product" #-}
{-# HLINT ignore "Use sum" #-}
{-# HLINT ignore "Use concat" #-}

main::IO()
main = do
    -- The most common use of foldl is to sum a list
    print(foldl (+) 0 [1,23,4]) -- It can be reduce to: sum [1,23,4]
    
-- FOLDL (the l stands for left) takes a list and reduces it to a single value.
-- The function takes three arguments: a binary function, an initial value, and a list.

-- Here we write the function myProduct, which calculates the product of a list of numbers.
myProduct xs = foldl (*) 1 xs -- Already exist a function 'product xs'

-- Here we construct a function that joins all string in a list
concatAll xs = foldl (++) "" xs 

-- Is common to use foldl and map togheter
-- This function sums all the squares of the numbers in a list
sumOfSquares xs = foldl (+) 0 (map (^2) xs)

-- A remarkable use of foldl is to reverse a list. 
-- We'll use an auxiliar binary function rcons
rcons x y = y:x
myReverse xs = foldl rcons [] xs

-- IMPLEMENTING foldl 
myFoldl f init [] = init -- Base case 
myFoldl f init (x:xs) = myFoldl f newInit xs -- Recursive case
    where newInit = f init x 