main :: IO ()
main = do
    print(hotterInKelvin 40 100)
    print(hotterInKelvin_Let 40 100)
    print(hotterInKelvin_Where 40 100)

{- 
Let's create a function that takes two temperatures—one in Celsius 
and one in Fahrenheit—and returns the hotter one but in Kelvin. 
Those are quite a few conversions, aren't they?
-}

-- Solution without let-where expression
hotterInKelvin c f =
    if c > ( f - 32 ) * 5 / 9
        then c + 273.16
        else ((f - 32) * 5 / 9) + 273.16

-- Solution with let expression
hotterInKelvin_Let c f =
    let fToC t = (t - 32) * 5 / 9
        cToK t = t + 273.16
        fToK t = cToK (fToC t)
    in 
        if c > fToC f 
            then cToK c 
            else fToK f

-- Solution with where expression
hotterInKelvin_Where c f = 
    if c > fToC f 
        then cToK c 
        else fToK f
    where
        fToC t = (t - 32) * 5 / 9
        cToK t = t + 273.16
        fToK t = cToK (fToC t)