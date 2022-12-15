#! /bin/bash
# This script print a random word - n times as parameter
# 2022-12-15 Juan Cru

for (( i=0; i<$1; i++ ))
do
echo `echo $(cat /usr/share/dict/words) | cut -f $RANDOM -d " "`
done