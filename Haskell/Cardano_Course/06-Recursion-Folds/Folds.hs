import Data.Text.Internal.Builder.Int.Digits (digits)
main :: IO()
main = do
    print (foldr'' (+) 0 [1,2,3,4,5,6]) -- It does the same that sum'
    print (sum' [1,2,3,4,5,6]) -- sum' using partial applications with foldr
    print (foldr'' (*) 1 [1,2,3,4,5,6]) -- It does the same that prod'
    print (prod' [1,2,3,4,5,6]) -- prod' using partial applications with foldr
    print (foldr'' (&&) True [True, False, True, True]) -- It does the same that add'
    print (add' [True, False, True, True])
    print (sumEven 12345678) -- add' using partial applications with foldr


-- FOLDR' -- PRIMITIVE RECURSION PATTERN - We're folding the list from the right
-- *************************************
-- Parameters: a function (callback), the base value and a list 
foldr'' :: (a -> b -> b) -> b -> [a] -> b
foldr'' _ b [] = b                        -- If the list is empty it returns the base value
foldr'' f b (x:xs) = f x (foldr'' f b xs) -- Recursion
{- Recursive process. This is how Haskell evaluates the function
foldr'' (+) [1,2,3] = (+) 1 (foldr'' (+) 0 [2,3]])
                        = (+) 1 ((+) 2 (foldr'' (+) 0 [3]))
                        = (+) 1 ((+) 2 ((x+) 3 (foldr'' (+) 0 []))) -- Here is the base case  
                        = (+) 1 ((+) 2 ((x+) 3 0))                  -- Final recursion
                        = 6
-}
-- Partial applications using foldr
sum' :: [Int] -> Int
sum' = foldr (+) 0
prod' :: [Int] -> Int
prod' = foldr (*) 1
add' :: [Bool] -> Bool
add' = foldr (&&) True



