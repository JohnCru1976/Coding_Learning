#! /bin/bash
# Script thar calcutates the number of iterations to get the parameter number

maxRandom=101
let "div=32767/$maxRandom"
let "random=$RANDOM / $div"
let "resto=(32767 % $maxRandom) + 1"
line=0

while [ $random != $1 ]
do
let "random= ($RANDOM - $resto) / $div"
((line++))
echo $line. $random
done
