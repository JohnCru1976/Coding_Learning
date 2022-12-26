main :: IO()
main = do
    print(checkForZeroes (0,2,3))
    print(checkForZeroes' (3,0,2))
    print(checkForZeroes'' (1,3,0))

-- Example with case
checkForZeroes :: (Int,Int,Int) -> String
checkForZeroes tuple3 = case tuple3 of
    (0,_,_) -> "The first one is a zero"
    (_,0,_) -> "The second one is a zero"
    (_,_,0) -> "The third one is a zero"
    _       -> "We're good"

-- That code is interchangable with this other one
checkForZeroes' :: (Int, Int, Int) -> String
checkForZeroes' (0, _, _) = "The first one is a zero!"
checkForZeroes' (_, 0, _) = "The second one is a zero!"
checkForZeroes' (_, _, 0) = "The third one is a zero!"
checkForZeroes' _         = "We're good!"

-- We can use the case expression in other places
-- For example as string
checkForZeroes'' :: (Int,Int,Int) -> String
checkForZeroes'' tuple3 = "The " ++ show tuple3 ++ " has " ++
    case tuple3 of
        (0, _, _) -> "a zero as its first element"
        (_, 0, _) -> "a zero as its second element"
        (_, _, 0) -> "a zero as its third element"
        _         -> "no zeroes!"
        
    ++ " ... and so on"