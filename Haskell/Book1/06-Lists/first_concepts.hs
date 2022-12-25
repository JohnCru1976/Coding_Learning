{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use list literal" #-}
{-# HLINT ignore "Redundant bracket" #-}
main::IO()
main = do
    -- HEAD AND TAIL
    print(head[1,2,3]) -- Returns 1
    print(head[[1,2],[3,4],[5,6]]) -- Returns [1,2]
    print(tail[1,2,3]) -- Returns [2,3]
    print(tail[3]) -- Returns []
    -- CONSING
    print(1:[]) -- : (cons - construct) this an infix operator
    print(1:2:3:4:[]) -- Returns [1,2,3,4]    
    print ((1,2):(3,4):(5,6):[]) -- Returns [(1,2),(3,4),(5,6)]
    -- BY DETIFINITION a LIST is always a value consed with another list
    -- (which can also be an empty list)
    print(1:[2,3,4]) -- Returns [1,2,3,4]
    -- STRINGS
    print(['h','e','l','l','o'])  -- Returns "hello"
    print('h':'e':'l':'l':'o':[]) -- Returns "hello"
    print ('h':"ello")            -- Returns "hello"
    -- If you want to combine two lists you need to concatenate them
    print("he" ++ "llo") -- Returns "hello"
    print([1,2]++[3,4])  -- Returns [1,2,3,4]
    -- QUICKLY GENERATION OF RANGES
    print([1..10])   -- Returns [1,2,3,4,5,6,7,8,9,10]
    print([1,3..10]) -- Returns [1,3,5,7,9]
    print([1.0,1.5..3]) -- Returns [1.0,1.5,2.0,2.5,3.0]
    print([1,0 .. -10]) -- Returns [1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

-- LAZY EVALUATION EXAMPLE
simple x = x
longList = [1 ..] -- This is an unending list
stillLongList = simple longList -- We can assing the unending list to a variable (lazy evaluation)
-- In LAZY EVALUATION no code is evaluated until it's needed


