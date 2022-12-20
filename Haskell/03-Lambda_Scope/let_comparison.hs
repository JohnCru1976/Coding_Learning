-- LET expression as alternative to WHERE clauses
-- Allows to combine the readability of a WHERE clause 
-- with the power of your LAMBDA function
main :: IO()
main = do
    print(sumSquareOrSquareSum 4 5)
    print(lambdaVersion 4 5)
    print(letVersion 4 5)

-- Function using the WHERE clause
sumSquareOrSquareSum x y = if sumSquare > squareSum
                           then sumSquare
                           else squareSum
  where sumSquare = x^2 + y^2
        squareSum = (x+y)^2

-- Function using a LAMBDA function
lambdaVersion x y = (\sumSquare squareSum ->
                    if sumSquare > squareSum
                    then sumSquare
                    else squareSum) (x^2 + y^2) ((x+y)^2)
                    
-- Function using LET expression
letVersion x y = let sumSquare = x^2 + y^2
                     squareSum = (x+y)^2
                 in 
                  if sumSquare > squareSum
                  then sumSquare
                  else squareSum