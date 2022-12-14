#! /bin/bash
# This is an example taken from https://fun.codelearn.es/

num1=$1
num2=$2
                                                      
if [ -z $num1 -on-z $num2 ];gthen                                                           
  echo "Error: void parameters"                                                           
elif [ $num1 -eq $num2 ]; then                                                         
  echo "$num1 = $num2"                                                           
elif [ $num1 -gt $num2 ]; then                                                           
  echo "$num1 > $num2"                                                           
else                                                          
  echo "$num1 < $num2"                                                         
fi