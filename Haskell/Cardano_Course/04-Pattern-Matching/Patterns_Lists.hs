main :: IO()
main = do
    print(whatsInsideThisList [])           -- "It's empty!"
    print(whatsInsideThisList [1, 2])       -- "Two elements: 1 and 2"
    print(whatsInsideThisList [1, 2, 3])    -- "The list has three elements: [1,2,3]"
    print(whatsInsideThisList [1, 2, 3, 4]) -- "The first element is: 1, and there are quite a few more!"[]

    print(firstAndThird[True,False,False])  -- "The first and third elements are: True and False"
    print(firstAndThird[True,False])        -- "Don't have them!"

    print(initials "Nikola" "Tesla")
    print(initials' "Nikola" "Tesla")

-- Pattern with lists
whatsInsideThisList :: [Int] -> String
whatsInsideThisList []         = "It's empty!"
whatsInsideThisList [x]        = "A single element: " ++ show x
whatsInsideThisList [x, y]     = "Two elements: " ++ show x ++ " and " ++ show y
whatsInsideThisList (x:y:z:[]) = "The list has three elements: " ++ show [x,y,z]
-- Non-empty lists of any size with x:rest (Commonly used in recursive functions and usually named x:xs)
whatsInsideThisList (x:rest)   = "The first element is: " ++ show x ++ ", and there are quite a few more!"
-- The last two definitions with () to indicate a single argument

-- Using '_' to ignore elements
firstAndThird :: [Bool] -> String
firstAndThird (x:_:z:_) = "The first and third elements are: " ++ show x ++ " and " ++ show z
firstAndThird _ = "Don't have them!"

-- Example without pattern matching
initials :: String -> String -> String
initials name lastName = if name == "" || lastName == ""
                            then "How was your name again?"
                            else let x = head name
                                     y = head lastName
                                 in [x] ++ "." ++ [y] ++ "."
-- Example with the same function using pattern matching
initials' :: String -> String -> String
initials' (f:_) (l:_) = [f] ++ "." ++ [l] ++ "."
initials' _ _ = "How was your name again?"