{-# OPTIONS_GHC -Wno-overlapping-patterns #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use list literal pattern" #-}
{-# HLINT ignore "Redundant bracket" #-}
main::IO()
main = do
    print(myReverse [1,2,3,4])
    print(myReverse [1])
    print(myReverse "Hello World")

-- Reverse function using recursion

-- PERSONAL SOLUTION
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

-- BOOK SOLUTION
myReverseV2 [] = []
myReverseV2 (x:[]) = [x]
myReverseV2 (x:xs) = (myReverseV2 xs) ++ [x]
