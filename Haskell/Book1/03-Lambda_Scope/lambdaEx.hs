main :: IO()
main = do  
  print(sumSquareOrSquareSum 4 5)
  print(lambdaVersion 4 5)

-- In this exercise both functions show the same result
-- The first is using WHERE
sumSquareOrSquareSum x y = if sumSquare > squareSum
                           then sumSquare
                           else squareSum
  where sumSquare = x^2 + y^2
        squareSum = (x+y)^2

-- The second is using a LAMBDA function
lambdaVersion x y = (\sumSquare squareSum ->
                    if sumSquare > squareSum
                    then sumSquare
                    else squareSum) (x^2 + y^2) ((x+y)^2)

                   