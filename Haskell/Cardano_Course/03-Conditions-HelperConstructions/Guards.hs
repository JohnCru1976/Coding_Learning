main :: IO ()
main = do
    -- Using if-then-else without guards
    print(specialBirthday 18)
    -- Using if-then-else without guards
    print(specialBirthday_Guards 60)


-- If-then-else expression without guards
specialBirthday age =
    if age == 1
        then "First birthday!"
        else
            if age == 18
                then "You're an adult!"
                else
                    if age == 60
                        then "Finally, I can stop caring about new lingo!"
                        else "Nothing special"

-- If expression with guards
specialBirthday_Guards :: Int -> [Char]
specialBirthday_Guards age
    | age == 1 = "First birthday!"
    | age == 18 = "You're an adult!"
    | age == 60 = "Finally, I can stop caring about new lingo!"
    | otherwise = "Nothing special"