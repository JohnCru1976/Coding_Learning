main :: IO()
main = do
    print wordsWithA
    print wordsWithA'
    print wordsWithA''
    print (any biggerThan4 [1..4])
    print (any biggerThan4 [1..6])
    print (any (\x -> x > 4) [1..4])
    print (any (> 4) [1..6])

-- Example with filter
wordsWithA = filter tempFunct ["arbol", "camion", "filo", "coche", "moto", "ascensor"]
    where tempFunct word = 'a' `elem` word
-- Another example
tempFunct word = 'a' `elem` word
wordsWithA' = filter tempFunct ["arbol", "camion", "filo", "coche", "moto", "ascensor"]
-- The same with lambda functions
wordsWithA'' = filter (\word -> 'a' `elem` word) ["arbol", "camion", "filo", "coche", "moto", "ascensor"]

--Example with any
biggerThan4 x = x > 4

