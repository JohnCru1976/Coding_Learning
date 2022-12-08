#!/bin/bash
function File {
    # think you are inside the file
    echo $#
}

# Do not change anything
# !(negacion)  S#(Numero Argumentos) -lt(less than) 
if ! [ $# -lt 1 ]; then
    File $*
    exit 0
else
    echo "There aren't arguments"
fi

# change here
# here you can pass the arguments
#bash prog.sh Shell is fun