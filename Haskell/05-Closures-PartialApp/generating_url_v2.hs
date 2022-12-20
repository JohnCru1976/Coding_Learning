main::IO()
main = do
    -- These are examples of use of functions built with PARTIAL APPLICATIONS
    print(exampleUrlBuilder "8473jAvaScr1pt" "book" "1234")
    print(myExampleUrlBuilder "book" "1234")

-- This is a new version of generating URL with closures PARTIAL APPLICATION
getRequestUrl host apiKey resource id = host ++
                                        "/" ++
                                        resource ++
                                        "/" ++
                                        id ++
                                        "?token=" ++
                                        apiKey

exampleUrlBuilder = getRequestUrl "http://example.com" -- PARTIAL APPLICATION
myExampleUrlBuilder = exampleUrlBuilder "1337hAsk3ll" -- PARTIAL APPLICATION

