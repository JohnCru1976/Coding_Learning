#!/bin/bash
# Example taken from https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php
# Setting a return value to a function
lines_in_file () {
  cat $1 | wc -l
}
num_lines=$( lines_in_file $1 )
echo The file $1 has $num_lines lines in it.


# Another example made from myself
#! /bin/bash

function test {
 echo "Parameter inside the function: $1" | grep 'Parameter'
}

var=$( test $2 )

echo "Parameter outside the function: $1"
echo $var
