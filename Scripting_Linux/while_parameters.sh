#! /bin/bash
# This an exercise from https://fun.codelearn.es/
# This script go over the parameters with the while structure

while [ ! -z $1 ]; do
  if [ -e "$1" ]; then
    cat $1
  fi
  shift
done