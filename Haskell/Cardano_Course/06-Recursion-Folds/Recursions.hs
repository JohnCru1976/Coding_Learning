main :: IO()
main = do
    print (sum' [1,2,3,4,5])
    print (product' [1,2,3,4,5])
    print (and' [True, False, True, True])
    print (length' [1,2,3,4,5])
    print (length' ['a'..'z'])

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

-- RECURSION EXAMPLES
-- AND' : a function that returns True if and only if all the elements of the list are True
and' :: [Bool] -> Bool
and' [] = True
and' (x:xs) = x && and' xs
{- Recursive process. This is how Haskell evaluates the function
and' [True,False,True,True] = True && and' [False,True,True]
                            = True && False && and' [True, True]
                            = True && False && True && and' [True]
                            = True && False && True && True && and' []
                            = True && False && True && True && True
-}

-- LENGTH' : a function that returns the length of a list
length' :: [a] -> Int
length' [] = 0
length' (_:xs) = 1 + length' xs

-- REVERSE' : a function that reverses a list
