main::IO()
main = do
    print(myTake 2 [1,2,3,4])
    print(myTake 0 [1,2,3,4])
    print(myTake 2 [0])

-- Implementation of take function by recursion
myTake _ [] = []
myTake 0 _ = []
myTake n (x:xs) = x:myTake (n-1) xs  