#!/bin/bash
# This is an example from https://ryanstutorials.net/linuxtutorial/scripting.php
# Backs up a single project directory
# Ryan 14/12/2022
 
date=`date +%F`
mkdir ~/projectbackups/$1_$date
cp -R ~/projects/$1 ~/projectbackups/$1_$date
echo Backup of $1

# This is my own solution
#! /bin/bash
date=`date +%F`

if [ -e $1 ]; then
  cp -r $1 $1_$date
  echo It\'s done
else
  echo $1 doesn\'t exists
fi


