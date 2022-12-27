
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use :" #-}
{-# HLINT ignore "Redundant ==" #-}
-- Question 1
-- Add the type signatures for the functions below and then remove the comments and try to compile.
-- (Use the types presented in the lecture.)

--f1 :: a -> b -> c -> d (my answer)
f1 x y z = x ** (y/z)

-- f2 Floating a => a -> a -> a -> a (my answer)
f2 x y z = sqrt (x/y - z)

-- f3 :: Bool -> Bool -> [Bool, Bool] (my answer)
f3 x y = [x == True] ++ [y]

-- f4 :: a -> a -> a -> Bool (my answer)
f4 x y z = x == (y ++ z)


-- Question 2
-- Why should we define type signatures of functions? How can they help you? How can they help others?


-- Question 3
-- Why should you define type signatures for variables? How can they help you?


-- Question 4
-- Are there any functions in Haskell that let you transform one type to the other? Try googling for the answer.


-- Question 5
-- Can you also define in Haskell list of lists? Did we showed any example of that? How would you access the inner
-- most elements?
