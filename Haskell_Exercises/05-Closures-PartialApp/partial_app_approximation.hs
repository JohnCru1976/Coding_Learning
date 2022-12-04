{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Avoid lambda" #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Redundant lambda" #-}
main::IO()
main = do
    print(test_v1 4)
    print(test_v2 8)
    print(test_v3 12)
    print(test_v4 25)

-- Without partial application. We need a middle function
binaryPartialApplication f x = (\y-> f x y)
test_v1 = binaryPartialApplication (+) 2

--With partial application. We can omit binaryPartialApplication
test_v2 = (+) 2
test_v3 = (2 +)
test_v4 = (/5)
