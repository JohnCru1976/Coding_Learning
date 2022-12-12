#! /bin/bash
# This an exercise from https://fun.codelearn.es/
# Test with files  -e (exist) -d (directory) -f (file)
# -r (is readable?) -w (writeable?) -x (exeecutable?)
if [ -e $1 ]; then
  if [ -d $1 ]; then
    echo $1 is a directory
  fi
  if [ -f $1 ]; then
    echo $1 is a file
  fi
else
  echo $1 does not exist
fi
