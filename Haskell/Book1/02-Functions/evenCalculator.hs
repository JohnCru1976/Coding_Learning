main :: IO()
main = do
  print(isEven 4)
  print(isEven 4)

isEven n = if (n `mod` 2) == 0
           then n - 2
           else 3*n + 1
-- Example of the function MOD. In this case is preferable to use EVEN.

isEven2 :: Integral a => a -> a
isEven2 n = if even n
            then n - 2
            else 3*n + 1