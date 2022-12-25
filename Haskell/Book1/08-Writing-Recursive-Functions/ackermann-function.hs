{-# OPTIONS_GHC -Wno-incomplete-patterns #-}

main::IO()
main = do
    print(ackermann 3 8)

-- Ackermann function by recursion
-- RULES:
-- Two arguments A(m,n)
-- If m = 0, return n + 1
-- If n = 0, then A(m-1,1)
-- If both m != 0 and n != 0, then A(m-1,A(m,n-1))

ackermann 0 n = n + 1
ackermann m 0 = ackermann (m-1) 1
ackermann m n = ackermann (m-1) (ackermann m (n-1))