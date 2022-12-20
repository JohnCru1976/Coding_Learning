{-# OPTIONS_GHC -Wno-incomplete-patterns #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}
import Distribution.Simple.Setup (trueArg)
main::IO()
main = do
    print(sayAmountCase 3) -- "a bunch"
    print(sayAmountPattern 1) -- 1
    print(sayAmountPattern 2) -- 2
    print(sayAmountPattern 3) -- "a bunch"
    print(isEmpty []) -- true
    print(isEmpty [2,35,6]) -- false
    print(myHead [2,35,6]) -- 2
    print(myTail [2,35,6] ) -- [35,6]
    print(myGCD 24 5)
    

-- First we are going to use case rather than pattern matching
sayAmountCase n = case n of
    1 -> "one"
    2 -> "two"
    _ -> "a bunch"

-- This is the pattern matching version
sayAmountPattern 1 = "one"
sayAmountPattern 2 = "two"
sayAmountPattern n = "a bunch"

-- You can use patter matching to check whether a list 
-- is empty by matching against []
isEmpty [] = True
isEmpty _ = False

-- Other version of head
-- This incorporates an error message when the list is empty

myHead (x:xs) = x
myHead [] = error "No head"


-- Other version of tail with pattern matching

myTail (_:xs) = xs
myTail [] = []


-- myGCD Greates Common Divisor
-- Using pattern matching
myGCD a 0 = a
myGCD a b = myGCD b (a `mod` b)

-- Exercise Q7.2 Previous version myGCD
myGCD_previous a b = if remainder == 0 -- 1) Goal condition
            then b            -- 2) Goal state
            else myGCD_previous b remainder -- 4) Rinse and repeat
    where remainder = a `mod` b
