{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Use infix" #-}
{-# HLINT ignore "Use repeat" #-}
{-# HLINT ignore "Use replicate" #-}
-- Data.list module: is where all list functions are.
-- https://hackage.haskell.org/package/base-4.16.0.0/docs/Data-List.html

main::IO()
main = do
    -- !! operator: access a particular element of a list by its index
    print([1,2,3]!!1) -- Returns 2
    print("puppies" !! 3) -- Returns 'p'
    print((!!) [1,2,3] 1) -- Returns '2' (use as infix function)
    print(infixExample1 3) -- Partial application, returns 'l'
    print(infixExample2 3) -- Partial application, returns 'l'
    print(infixExample3 "hello") -- Partial application, returns 'l'
    -- LENGTH
    print(length[1..20]) -- Returns 20
    print(length "hello") -- Returns 5
    -- REVERSE
    print(reverse [1,2,3])  -- Returns [3,2,1]
    print(reverse "cheese") -- Returns "eseehc"
    print(isPalindrome "cheese") -- Returns false
    print(isPalindrome "racecar") -- Returns true
    print(isPalindrome  [1,2,1]) -- Returns true
    -- ELEM Takes a value and a list and checks whether the value is in the list
    print(13 `elem` [0,13..100]) -- Returns true
    print('p' `elem` "cheese") -- Returns false
    print((elem) 'p' "cheese") -- Use of infix - Not recommended
    -- TAKES returns the n first elements of a list
    print(take 5 "wonderful") -- Returns "wonde"
    print(take 3 [1,5..100]) -- Returns [1,5,10]
    print(take 8 "hello") -- Returns "hello"  - Parameter is bigger than the length
    print(reverse(take 3 (reverse "hello"))) -- Returns "llo" - Take Reverse combination
    -- DROP Removes the first n elements of a list
    print(drop 5 "wonderful") -- Returns "rful"
    print(drop 3 [1,2..10]) -- Returns [6,8,10]
    print(drop 8 "hello") -- Returns ""  - Parameter is bigger than the length
    -- ZIP combine two lists into tuple pairs
    print(zip [1,2,3] [2,4,6]) -- Returns [(1,2),(2,4),(3,6)]
    print(zip "dog" "rabbit") -- Returns [('d','r'), ('o','a'),('g','b')]
    print(zip ['a' .. 'd'] [1 ..]) -- Returns [('a',1),('b',2),('c',3),('d',4)]
    -- CYCLE Given a list, cycle repeats that list endlessly
    print(ones 6 2) -- Returns [1,2,1,2,1,2]
    -- REPEAT Given a list, cycle repeats that list endlessly
    print(ones 6 2) -- Returns [1,2,1,2,1,2]


-- Use of PARTIAL APPLICATION with INFIX OPERATORS
infixExample1 = (!!) "hello" -- Partial application
infixExample2 = ("hello" !!) -- This is called section
infixExample3 = (!! 3) -- This is called a section

-- PALINDROME FUNCTION EXAMPLE (REVERSE)
isPalindrome word = word == reverse word

-- CYCLE Given a list, cycle repeats that list endlessly
--Example 1
ones x n = take x (cycle[1..n]) 
--REPEAT do the same as CYCLE (it seems at least)
ones_v2 x n = take x (repeat[1..n])
