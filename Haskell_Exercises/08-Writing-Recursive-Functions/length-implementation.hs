{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}
main::IO()
main = do
    print(myLength [])
    print(myLength [1,1.5..10])

-- Implementing length function
myLength [] = 0
myLength (x:xs) = 1 + myLength xs
