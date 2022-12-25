
main::IO()
main = do
    -- First solution (incomplete)
    print (addressLetter sfOffice member);
    print (addressLetter nyOffice member);
    print (addressLetter renoOffice member);

member = ("Vicente","Morales")
-- The next functions receive a tuple as parametrer (name,lastname)
-- Fisrt function returns member + address depending the last name starting with L or later
sfOffice name = if lastName < "L" -- The last name starts with letter lower than L
                then nameText
                     ++ " - PO Box 1234 - San Francisco, CA, 94111"
                else nameText
                     ++ " - PO Box 1010 - San Francisco, CA, 94109"
    where lastName = snd name
          nameText = fst name ++ " " ++ lastName
-- Second function returns the name followed by a colon rather than a hyphen + address
nyOffice name = nameText ++ " : PO Box 789 - New York, NY, 10013"
    where nameText = fst name ++ " " ++ snd name
-- Third function returns only last names + address
renoOffice name = nameText ++ " - PO Box 456 - Reno, NV 89523"
    where nameText = snd name

-- This would be a first solution. The problem is the function is going
-- to be a part of a larger web application
addressLetter location = location
-- We build a function that return the proper functions according a little string
-- "ny" for New York
-- "sf" for San Francisco
-- "reno" for Reno
