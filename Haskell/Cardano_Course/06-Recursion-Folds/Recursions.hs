main :: IO()
main = do
    print (sum' [1,2,3,4,5])
    print (product' [1,2,3,4,5])

sum' :: [Int] -> Int
sum' [] = 0 -- Base case
sum' (x:xs) = x + sum' xs
{- Recursive process. This is how Haskell evaluates the function
sum' [1,2,3,4,5] = 1 + sum' [2,3,4,5] 
                 = 1 + 2 + sum' [3,4,5]
                 = 1 + 2 + 3 + sum' [4,5]
                 = 1 + 2 + 3 + 4 + sum' [5]
                 = 1 + 2 + 3 + 4 + 5 + sum' []
                 = 1 + 2 + 3 + 4 + 5 + 0
                 = 15
-}

product' :: [Int] -> Int
product' [] = 1 -- Base case
product' (x:xs) = x * product' xs

