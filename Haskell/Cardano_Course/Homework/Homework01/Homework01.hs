main :: IO()
main = do
    print (prodBy3 6)
    print (circleArea 5)
    print (cylinderVolume 2.8 2.4)
    print (if (2.4 * circleArea 2.6) >= 42.0
    then "The volume of the cylinder is equal to or greater than 42"
    else "The volume of the cylinder is lesser than 42")
-- Question 1
-- Write a multiline comment below.
{-
This is a multiline
comment 
-}

-- Question 2
-- Define a function that takes a value and multiplies it by 3.
prodBy3 :: Int -> Int
prodBy3 x = x * 3

-- Question 3
-- Define a function that calculates the area of a circle.
circleArea :: Floating a => a -> a
circleArea r = pi * r^2

-- Question 4
-- Define a function that calculates the volume of a cylinder by composing the previous function together with the height of the cylinder. 
cylinderVolume :: Floating a => a -> a -> a
cylinderVolume h r = h * circleArea r

-- Question 5
-- Define a function that takes the height and radius of a cylinder and checks if the volume is greater than or equal to 42.
cylinderVolGt42 :: (Ord a, Floating a) => a -> a -> String
cylinderVolGt42 h r = if (h * circleArea r) >= 42.0 
    then "The volume of the cylinder is equal to or greater than 42" 
    else "The volume of the cylinder is lesser than 42"