main::IO()
main = do
    print(inFirstHalf 4 [2,3,4,4,5])

-- EXERCISE Q6.3 Write a function inFirstHalf that returns True if an element 
-- is in the first half of list, and otherwise returns False
inFirstHalf element myList = element `elem` firstHalf
    where listHalfLength = length myList `div` 2 -- div: returns how many times the 
                                                 -- first number can be divided 
                                                 -- by the second one (int)
          firstHalf = take listHalfLength myList