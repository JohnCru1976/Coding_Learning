{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Use camelCase" #-}
{-# HLINT ignore "Use repeat" #-}
{-# HLINT ignore "Use uncurry" #-}
import           Data.Char
{-# HLINT ignore "Use null" #-}
{-# HLINT ignore "Use any" #-}
main::IO()
main = do
    print (myElem 4 [1,2,3,4])
    print (isPalindrome "A man a plan a canal Panama")
    print (harmonic 5)
    print (harmonic_book 5)

-- Q9.1 Use filter and length to re-create the elem function
myElem a xs = not (length xs == 0 || filter (== a) xs /= [])

-- Q9.2 Your isPalindrome function from lesson 6  doesn't handle sentences with spaces or capitals.
--      Use 'map' and 'filter' to make sure the phrase "A man a plan a canal Panama" is recognized as
--      a palindrome.
isPalindrome text = lowerText == reverse lowerText
   where noSpacesText = filter (/=' ') text
         lowerText = map toLower noSpacesText

-- Q9.3 In mathematics, the harmonic series is the sum of 1/1+1/2+1/3+1/4...
--      Write a function 'harmonic' that takes an argument 'n' and calculates 
--      the sum of the series to 'n'. Make sure to use lazy evaluation.
-- PERSONAL SOLUTION
harmonic :: (Fractional a, Enum a) => Int -> a
harmonic n = sum fractionList
    where fractionList = map (1 /) (take n [1..])
-- BOOK SOLUTION
harmonic_book n = sum (take n seriesValues)
  where seriesPairs = zip (cycle [1.0]) [1.0,2.0 ..]
        seriesValues = map (\pair -> (fst pair)/(snd pair)) seriesPairs