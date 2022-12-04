main::IO()
main = do
    print(take 5 (myCycle_v1 [1,2,4,5]))
    print(take 5 (myCycle_v2 [1,2,4,5]))

-- Implementation of cycle by using recursive function
--PERSONAL SOLUTION
myCycle_v1 [] = []
myCycle_v1 (x:xs) = x:xs ++ myCycle_v1 (x:xs)

-- BOOK SOLUTION
myCycle_v2 [] = []
myCycle_v2 (x:xs) = x:myCycle_v2(xs++[x])

