-- This code is an example of use SORT and SORTBY functions
-- Special values GT (Greater Than), LT (Less Than), EQ (Equal)
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use guards" #-}
import Data.List -- Module that contains sort and sortby functions among others
main :: IO()

main = do
    print(sort names) -- We use SORT to sort by the first element of each tuple
    -- [("Bernard","Sumner"),("Ian","Curtis"),("Peter","Hook"),("Stephen","Morris"),("Vicent","Sumner")]
    print(sortBy compareLastNames names) -- We use SORTBY to sort according to a passed function
    -- [("Ian","Curtis"),("Peter","Hook"),("Stephen","Morris"),("Bernard","Sumner"),("Vicent","Sumner")]


-- This is an array of tuples we are sorting
names = [("Ian","Curtis"),("Bernard","Sumner"), ("Vicent","Sumner"),("Peter","Hook"),("Stephen","Morris")]

-- This is a function to sort by last names
compareLastNames name1 name2 = if lastName1 > lastName2
                              then GT      -- Greater Than
                              else if lastName1 < lastName2 -- else if
                                  then LT  -- Less Than
                                  else if firstName1 > firstName2
                                      then GT 
                                      else if firstName1 < firstName2
                                         then LT
                                         else EQ  -- Equal
  where lastName1 = snd name1
        lastName2 = snd name2 
        firstName1 = fst name1
        firstName2 = fst name2                                     