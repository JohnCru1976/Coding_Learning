#!/bin/bash
# Example from https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php
# Make a php copy of any html files

for value in $1/*.html
do
  cp $value $1/$( basename -s .html $value ).php
done