#!/bin/bash
# This example was taken from https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php
# A simple menu system

names='Kyle Cartman Stan Quit'
PS3='Select character: '

select name in $names
do
  if [ $name == 'Quit' ]
  then
    break
  fi
  echo Hello $name
done

echo Bye