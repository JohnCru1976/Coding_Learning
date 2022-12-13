#! /bin/bash
# This is an example taken from https://fun.codelearn.es/
clear
key=$1
case $key in
    [a-z,A-Z,ñ]) echo "Alpha" ;;
    [0-9]) echo "Number" ;;
    *) echo "Special" ;;
esac