main :: IO()
main = do
    print (sum' [1,2,3,4,5])
    print (product' [1,2,3,4,5])
    print (and' [True, False, True, True])
    print (length' [1,2,3,4,5])
    print (length' ['a'..'z'])
    print (reverse' ['a'..'z'])
    print (drop' (-2) ['a'..'z'])
    print (take' 13 ['a'..'z'])
    print (take' 1 ['a'..'z'])
    print (take' (-2) ['a'..'z'])

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
{- Recursive process. This is how Haskell evaluates the function
product' [1,2,3,4,5] = 1 * product' [2,3,4,5] 
                 = 1 * 2 * product' [3,4,5]
                 = 1 * 2 * 3 * product' [4,5]
                 = 1 * 2 * 3 * 4 * product' [5]
                 = 1 * 2 * 3 * 4 * 5 * product' []
                 = 1 * 2 * 3 * 4 * 5 * 0
                 = 120
-}

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
                            = False
-}

-- LENGTH' : a function that returns the length of a list
length' :: [a] -> Int
length' [] = 0
length' (_:xs) = 1 + length' xs
{- Recursive process. This is how Haskell evaluates the function
length' 4 [1,2,3,4,5,6] = 1 + length' xs -- xs = [2,3,4,5,6]
                        = 1 + 1 + length' xs -- xs = [3,4,5,6]
                        = 1 + 1 + 1 + length' xs -- xs = [4,5,6]
                        = 1 + 1 + 1 + 1 + length' xs -- xs = [5,6]
                        = 1 + 1 + 1 + 1 + 1 + length' xs -- xs = [6]
                        = 1 + 1 + 1 + 1 + 1 + 1 + 0 -- xs = []
                        = 6
-}

-- REVERSE' : a function that reverses a list
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]
{- Recursive process. This is how Haskell evaluates the function
reverse' [1,2,3,4,5,6] = reverse' [2,3,4,5,6] ++ [1]
                       = reverse' [3,4,5,6] ++ [2] -- Is reverse [2,3,4,5,6]
                       = reverse' [4,5,6] ++ [3]   -- Is reverse [3,4,5,6]
                       = reverse' [5,6] ++ [4]     -- Is reverse [4,5,6]
                       = reverse' [6] ++ [5]       -- Is reverse [5,6]
                       = [] ++ [6]                 -- Is reverse [6]
                       -- By substitution bottom-up 
                       = [] ++ [6] ++ [5] ++ [4] ++ [3] ++ [2] ++ [1]
                       = [6,5,4,3,2,1] 
-}

-- DROP' : remove the first n elements from a list
drop' :: Int -> [a] -> [a]
drop' _ [] = []
drop' n xs | n <= 0 = xs
drop' n (_:xs) = drop' (n-1) xs
{- Recursive process. This is how Haskell evaluates the function
drop' 4 [1,2,3,4,5,6] = drop' 3 [2,3,4,5,6]
                      = drop' 2 [3,4,5,6]
                      = drop' 1 [4,5,6]
                      = [4,5,6]   -- drop' 0 [4,5,6]
-}

-- TAKE' : take (and return) the firts n elements from a list
take' :: Int -> [a] -> [a]
take' _ [] = []
take' n _ | n <= 0 = []
take' n (x:xs) = x : take' (n-1) xs
{- Recursive process. This is how Haskell evaluates the function
take' 3 [1,2,3,4,5,6] = 1 : take' 2 [2,3,4,5,6]
                      = 1 : 2 : take' 1 [3,4,5,6]
                      = 1 : 2 : 3 : [] -- take' 0 [4,5,6]
                      = [1,2,3]
-}

-- MAP' : a higher-order function that applies a function to every element on a list

