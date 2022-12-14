#! /bin/bash
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

# More complex example from https://ryanstutorials.net/linuxtutorial/scripting.php
#!/bin/bash
# Backs up a single project directory
# Ryan 14/12/2022
 
if [ $# != 1 ]
then
    echo Usage: A single argument which is the directory to backup
    exit
fi
if [ ! -d ~/projects/$1 ]
then
    echo 'The given directory does not seem to exist (possible typo?)'
    exit
fi
date=`date +%F`
 
# Do we already have a backup folder for todays date?
if [ -d ~/projectbackups/$1_$date ]
then
    echo 'This project has already been backed up today, overwrite?'
    read answer
    if [ $answer != 'y' ]
    then
        exit
    fi
else
    mkdir ~/projectbackups/$1_$date
fi
cp -R ~/projects/$1 ~/projectbackups/$1_$date


