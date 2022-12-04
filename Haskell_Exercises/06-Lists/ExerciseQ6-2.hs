main::IO()
main = do
    print(subseq_v1 2 5 [1 .. 10]) -- Returns [3,4,5]
    print(subseq_v1 2 7 "a puppy") -- Returns "puppy"
    print(subseq_v2 2 5 [1 .. 10]) -- Returns [3,4,5]
    print(subseq_v2 2 7 "a puppy") -- Returns "puppy"

-- EXERCISE Q6.2 Write a function subseq that takes three arguments: a start position,
-- an end position, and a list. The function should return the subsequence 
-- between the start and end

-- PERSONAL SOLUTION
subseq_v1 start end myList = drop start (take end myList)

-- BOOK SOLUTION
subseq_v2 start end myList = take difference (drop start myList)
    where difference = end - start
