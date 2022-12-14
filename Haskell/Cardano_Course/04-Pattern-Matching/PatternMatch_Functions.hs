main :: IO ()
main = do
    print (specialBirthday 60)
    print (specialBirthday' 34)

-- This is the if-then-else form
specialBirthDay'' :: Int -> [Char]
specialBirthDay'' age =
  if age == 1
    then "First birthday!"
    else
      if age == 18
        then "You're an adult!"
        else
          if age == 60
            then "Finally, I can stop caring about new lingo!"
            else "Nothing special, you're just " ++ show age

-- This is a simple pattern match (with non-exhaustive patterns)
-- If we pass a number that there isn't in the pattern
-- the compiler will launch an exception
specialBirthday :: Int -> [Char]
specialBirthday 1 = "First birthday!"
specialBirthday 18 = "You're an adult"
specialBirthday 60 = "Finally, I can stop caring about new lingo!"

-- Example with catch-all patterns (in this case it will be like else)
specialBirthday' :: Int -> [Char]
specialBirthday' 1 = "First birthday!"
specialBirthday' 18 = "You're an adult"
specialBirthday' 60 = "Finally, I can stop caring about new lingo!"
specialBirthday' age = "Nothing special, you're just " ++ show age

