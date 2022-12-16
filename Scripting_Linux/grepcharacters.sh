#! /bin/bash
# This script prints the words with $1 characters
# 2022-12-16 Juan Cru

cat /usr/share/dict/words | egrep ^.{$1}$