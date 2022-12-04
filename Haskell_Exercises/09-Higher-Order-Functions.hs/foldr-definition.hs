{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}

main::IO()
main = do
    print (myFoldr (-) 0 [1,2,3,4])
    print (foldr (-) 0 [1,2,3,4])
    print ((-)1((-)2((-)3((-)4 0)))) -- It would be the result of the recursion
    print ((-)4 0) -- Step 1: 4-0 = 4
    print ((-)3((-)4 0)) -- Step 2: 3-4=-1
    print ((-)2((-)3((-)4 0))) -- Step 3: 2-(-1)=3
    print ((-)1((-)2((-)3((-)4 0)))) -- Step 4: 1-3=-2
    -- Mathematic principle: 
    -- d-c-b-a = a-(b-(c-d))

-- FOLDR it to the same that foldl. The left fold compacts the list into
-- the left argument (init), and the right fold into the right argument (xs)
-- DEFINITION of foldr
myFoldr f init [] = init
myFoldr f init (x:xs) = f x rightResult
   where rightResult = myFoldr f init xs

-- I reproduce here myFoldl function ir order to compare
-- IMPLEMENTING foldl 
myFoldl f init [] = init -- Base case 
myFoldl f init (x:xs) = myFoldl f newInit xs -- Recursive case
    where newInit = f init x 

-- Both perfonmance and computational differences exist between foldl and foldr.