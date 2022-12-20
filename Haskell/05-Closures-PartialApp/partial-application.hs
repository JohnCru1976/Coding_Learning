{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Avoid lambda" #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Redundant lambda" #-}
main::IO()
main = do
    -- Function call with lambda closure
    print(test1 5 6 7)
    -- Function call with PARTIAL APPLICATION
    print(test1 5 6 7)

-- Here we create the initial function
add4 a b c d = a + b + c + d
-- Here we create a closure with a lambda function
addXto3 x = (\b c d -> add4 x b c d)
test1 = addXto3 4

-- This is another way to create a closure
-- This way is called PARTIAL APPLICATION
-- So it isn't needed an intermediate function
test2 = add4 4 -- PARTIAL APPLICATION
-- Not only has partial appliation saved you from using a lambda funtion, 
-- but you don't even need to define the awkwaedly named addXto3