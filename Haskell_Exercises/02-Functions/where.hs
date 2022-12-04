main :: IO()
main = do    
    print(calcChange 200 100)
    print(lambdaCalChange 100 200)

calcChange owed given = if change  > 0
                        then change 
                        else 0
    where change = given - owed
-- The if structure always must have an else
-- This is because a function always must return a value (or function)

lambdaCalChange = (\owed given ->
                    if given - owed > 0
                    then given - owed
                    else 0)
-- This is the same function in lambda form