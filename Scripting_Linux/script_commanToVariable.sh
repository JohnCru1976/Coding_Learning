#!/bin/bash
# A simple demonstration of using backticks
# This is an example from https://ryanstutorials.net/linuxtutorial/scripting.php
# Ryan 14/12/2022

# Here we use backticks to asign the output of a command to a vairable
lines=`cat $1 | wc -l` 
echo The number of lines in the file $1 is $lines