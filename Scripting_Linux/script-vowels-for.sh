#! /bin/bash
# This an exercise from https://fun.codelearn.es/ (Sheell 5)

# First: I need control the input
# https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php

vowelsCount=0
consCount=0

echo -n 'Insert word: '
read word
echo -n 'Insert word length: '
read wordLength

# Second: I need make a loop for the variable word (string)
#https://www.cyberciti.biz/faq/bash-for-loop-array/
#https://stackoverflow.com/questions/10551981/how-to-perform-a-for-loop-on-each-character-in-a-string-in-bash
for (( i=0; i<$wordLength; i++ ));
do
    # Third: I need to detect vowels and consonants
    # https://www.networkworld.com/article/2693361/unix-tip-using-bash-s-regular-expressions.html
    if [[ ${word:$i:1} =~ [aeiou] ]]; then
        #https://linuxize.com/post/bash-increment-decrement-variable/
        ((vowelsCount++))
    else
        ((consCount++))
    fi
done

#https://tldp.org/LDP/abs/html/comparison-ops.html
if [[ $vowelsCount -eq $consCount ]]; then
    echo "The word $word has the same number of vowels than consonants"
fi
if [[ $vowelsCount -gt $consCount ]]; then
    echo "The word $word has fewer consonants than vowels"
fi
if [[ $vowelsCount -lt $consCount ]]; then
    echo "The word $word has more consonants than vowels"
fi
