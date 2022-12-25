{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Avoid lambda" #-}
{-# HLINT ignore "Redundant bracket" #-}
{-# HLINT ignore "Redundant lambda" #-}
main :: IO()
main = do
    -- In this first example we use a closure of the host argument
    print(exampleUrlBuilder1 "1337hAsk3ll" "book" "1234")
    -- In this second example we use a closure of the host and the apiKey argument
    print(exampleUrlBuilder2 "1234")

-- Here is a basic getRequestURL
-- The argumens are order from most to least general
getRequestURL host apiKey resource id = host ++
                                        "/" ++
                                        resource ++
                                        "/" ++
                                        id ++
                                        "?token=" ++
                                        apiKey

-- A closure could be needed if we repeat, for example, the host
-- Here can capture the host argument into a closure
genHostRequestBuilder host = (\apiKey resource id ->
                               getRequestURL host apiKey resource id)
-- This way we store "http://example" waiting for the rest of the arguments in advance
exampleUrlBuilder1 = genHostRequestBuilder "http://example.com"
-- Now we can build a closure of the "apikey" and "resource" arguments
genApiRequestBuilder hostBuilder apiKey resource= (\id ->
                                            hostBuilder apiKey resource id)
-- Here we store the exampleUrlBuilder and the apiKey "1337hAsk3ll" and the resource "book"
exampleUrlBuilder2 = genApiRequestBuilder exampleUrlBuilder1 "1337hAsk3ll" "book"