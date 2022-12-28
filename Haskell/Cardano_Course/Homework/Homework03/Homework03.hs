-- Question 1
-- Write a function that checks if the monthly consumption of an electrical device is bigger, equal, or smaller than the maximum allowed and
-- returns a message accordingly. 
-- The function has to take the hourly consumption of an electrical device, the hours of daily use, and the maximum monthly consumption allowed.
-- (Monthly usage = consumption (kW) * hours of daily use (h) * 30 days).
checkConsumptionMax consump hours max
        | monthlyConsump > max = "Monthly consumption is bigger than the maximum allowed"
        | monthlyConsump == max = "Monthly consumption is equal to the maximum allowed"
        | monthlyConsump < max = "Monthly consumption is smaller than the maximum allowed"
    where monthlyConsump = consump * hours * 30


-- Question 2
-- Prelude:
-- We use the function `show :: a -> String` to transform any type into a String.
-- So `show 3` will produce `"3"` and `show (3 > 2)` will produce `"True"`.

-- In the previous function, return the excess/savings of consumption as part of the message.
checkConsumptionMax' consump hours max
        | monthlyConsump > max = "Monthly consumption is bigger than the maximum allowed: " ++ show difference ++ "KW excessed"
        | monthlyConsump == max = "Monthly consumption is equal to the maximum allowed"
        | monthlyConsump < max = "Monthly consumption is smaller than the maximum allowed: " ++ show difference ++ "KW saved"
    where monthlyConsump = consump * hours * 30
          difference = abs (max - monthlyConsump)


-- Question 3
-- Write a function that showcases the advantages of using let expressions to split a big expression into smaller ones.
-- Then, share it with other students in Canvas.

secondGradeEquation :: (Ord b, Show b, Floating b) => b -> b -> b -> String
secondGradeEquation a b c =
    let discriminant = b^2 - 4*a*c
        denom = 2*a
        pos = (negate b + sqrt discriminant)/denom
        neg =  (negate b - sqrt discriminant)/denom
    in 
        if discriminant < 0 
            then "Without result" 
            else show (pos,neg)



-- Question 4
-- Write a function that takes in two numbers and returns their quotient such that it is not greater than 1.
-- Return the number as a string, and in case the divisor is 0, return a message why the division is not
-- possible. To implement this function using both guards and if-then-else statements.  


quotient x y =
    if y == 0 
        then "The divisor can't be 0" 
        else             
            show (x/y)
                
quotient' x y
    | y == 0 = "The divisor can't be 0"
    | otherwise = show (x/y)      
        
        
    
-- Question 5
-- Write a function that takes in two numbers and calculates the s

-- of those numbers. Write the function such that you use a where block inside a let expression and a
-- let expression inside a where block. 

-- SOLUTION (I WASN'T ABLE TO SOLVE)
invertedConstructions :: Double -> Double -> Double
invertedConstructions a b = let sqrtProd = sqrt abProd where abProd = a * b
                            in sqrtProd + sqrtQuot
                            where sqrtQuot = let abQuot = a / b in sqrt abQuot

    

