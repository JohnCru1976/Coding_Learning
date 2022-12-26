main :: IO()
main = do
    print (firstOfThree (1,2,3))
    print (pairFromFour(1,2,3,4))

-- First example with tuples
firstOfThree :: (a,b,c) -> a
firstOfThree (x,_,_) = x

-- Another example
pairFromFour :: (a,b,c,d) -> (b,d)
pairFromFour (_,x,_,y) = (x,y)

