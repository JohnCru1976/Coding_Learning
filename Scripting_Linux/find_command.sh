#! /bin/bash
echo Number of parameters inserted\: $#

while [ ! -z $1 ]
do
  echo $1
  find .// -name "*.$1"
  shift
done