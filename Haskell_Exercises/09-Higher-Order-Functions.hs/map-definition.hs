{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Use map" #-}
{-# HLINT ignore "Use section" #-}
main::IO()
main = do
    -- First example using the addAnA function
    print(myMap addAnA ["dog", "banana", "car"])
    -- In these examples I'm passing the function directly
    print(myMap ((++) "a ") ["dog", "banana", "car"])
    print(myMap reverse ["hola mundo"])
    print(myMap ((^) 2) [2,4,7,8])

-- This is the definition of map function
-- Map higher-order function is an abstraction of this pattern
-- f is a first-class function - a callback
myMap f [] = []
myMap f (x:xs) = (f x):myMap f xs

-- Here I'm making an example of a function that I'll call later, in the main section
addAnA = (++) "a "