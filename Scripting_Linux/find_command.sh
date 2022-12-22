#! /bin/bash
# Shows the files with the suffix passed as parameters
echo Number of parameters inserted\: $#

while [ ! -z $1 ]
do
  echo $1
  find .// -name "*.$1"
  shift
done