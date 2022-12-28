
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
{-
    Signatures prevent us to make mistakes using values of a different type,
    thus the compiler launches an exception when we tray to do so.
    Signature let other and ourselves to know how many paramenters has tha function,
    their type, and the typy of the value the functin returns.
-}

-- Question 3
-- Why should you define type signatures for variables? How can they help you?
{-
    I think this is because we can use complex expressions in the definition not being
    clear what kind of type it returns. The signature permits a quick glance of the definition type. 
-}

-- Question 4
-- Are there any functions in Haskell that let you transform one type to the other? Try googling for the answer.
{-
    Yes, we can convert a type to an another with functions. For example:
    (Int to Double) fromIntegral x :: Double
    (Double to Int) round x
    (String to Int) read s :: Int
    (String to Double) read s :: Double
    (Int/Double.. to String) show x
-}

-- Question 5
-- Can you also define in Haskell list of lists? Did we showed any example of that? How would you access the inner
-- most elements?
{- 
    Yes, we can define the variable l = [[1,2,3],[4,5,6],[7,8,9]]
    I don't think so we have used any example of list of lists, at least than we consider
    unitary elements as lists of one elements.
    Example to acces to inner elements: [[1,2,3],[4,5,6],[7,8,9]] !! 1 !! 0 ---> 4
-}

