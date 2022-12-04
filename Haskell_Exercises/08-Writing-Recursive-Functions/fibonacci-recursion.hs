import GHC.Float (float2Int)

main::IO()
main = do
    print(map fibonacciV2 [1..10])
    print(map binet [11..20])
    print(map fastFibV2 [21..30])

-- Calculate fibonacci function by recursion

-- PERSONAL SOLUTION
fibonacciV1 a
  | a <= 2 = 1
  | otherwise = fibonacciV1 (a-1) + fibonacciV1 (a-2)

-- BOOK SOLUTION WITH PATTERN MATCHING
fibonacciV2 0 = 0
fibonacciV2 1 = 1
fibonacciV2 n = fibonacciV2 (n-1) + fibonacciV2 (n-2)

-- BINET FUNCTION --- NO RECURSION
-- https://steemit.com/spanish/@nenio/una-formula-cerrada-para-los-numeros-de-fibonacci
binet n = float2Int (((1 + sqrt 5)^n - (1 - sqrt 5)^n) / ((2^n) * sqrt 5))

-- Book solution with recursion
fastFib _ _ 0 = 0
fastFib _ _ 1 = 1
fastFib _ _ 2 = 1
fastFib a b 3 = a + b
fastFib a b n = fastFib (a + b) a (n - 1)
-- Partial Application
fastFibV2 = fastFib 1 1 
