main::IO()
main = do
    print(map collatz [100..120])
    print(collatzList 109)

-- Collatz Conjecture: involves defining a recursive 
-- process given a starting number n
-- If n is 1, you're finished
-- If n is even, repeat with n/2
-- If n is odd, repeat with n * 3 + 1

collatz 1 = 1
collatz n = if even n
            then 1 + collatz (n `div` 2)
            else 1 + collatz (n*3 + 1)

-- This is a personal solution that returns a list with the Collatz conjecture solutions
collatzList 1 = [1]
collatzList n = if even n
                 then n:collatzList (n `div` 2)
                 else n:collatzList (n*3 + 1)