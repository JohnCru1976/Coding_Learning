main :: IO()
main = do
    print (sumEven 1233456)

-- SUMEVEN - TODIGITS
-- ******************
-- This function takes an integral and returns a list with it digits
toDigits :: Integral a => a -> [a]
toDigits n 
    | n < 1 = []
    | otherwise = toDigits (div n 10) ++ [mod n 10]
-- Taking advantaged of toDigits we sum the evens with sumEven
sumEven n = sum .filter even $ toDigits n