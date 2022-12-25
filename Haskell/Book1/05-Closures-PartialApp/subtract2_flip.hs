{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant lambda" #-}
main :: IO()
main = do
    print(subtract2_v1 4)
    print(subtract2_v2 6)
    print(subtract2_v2 8)
subtract2_v1 = \x -> x - 2
subtract2_v2 = \x -> (-) x 2
-- This is a partial application
-- This would be a prefix function (-) 2 x
-- We use flip to let x be on first place
subtract2_v3 = flip (-) 2
