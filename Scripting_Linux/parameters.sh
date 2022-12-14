#!/bin/bash
echo "File name is "$0 # holds the current script
echo $3 # $3 holds banana
Data=$5
echo "A $Data costs just $6."
echo $#

#Executing the script on terminal as
#bash my_shopping.sh apple 5 banana 8 "Fruit Basket" 15
#output is
#File name is script_parameters.sh
#banana
#A Fruit Basket costs just 15
#6
#The variable $# holds the number of arguments passed to the script
#The variable $@ holds a space delimited string of all arguments passed to the script