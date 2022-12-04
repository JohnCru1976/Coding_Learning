main :: IO()
main = do
    print(overWrite 3) -- Print '8'

overWrite x = let x = 2
              in 
               let x = 4
               in
                let x = 6
                in
                 x+2

-- This is useless, but could remind the way to redefine variables in GHCi