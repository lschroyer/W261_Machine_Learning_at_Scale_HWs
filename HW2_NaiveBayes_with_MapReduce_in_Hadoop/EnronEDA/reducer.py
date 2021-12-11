#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########    
    
    if current_word == word:    
        if int(is_spam) == 0:
            ham_count += int(count)
        else:
            spam_count += int(count)
    
    elif current_word == None:
        if int(is_spam) == 0:
            ham_count += int(count)
        else:
            spam_count += int(count)
        current_word = word
    
    else:
        print(f'{current_word}\t0\t{ham_count}')
        ham_count = int(count)
        print(f'{current_word}\t1\t{spam_count}')
        spam_count = int(count)
        current_word = word

#Final print
if int(is_spam) == 0:
    print(f'{word}\t0\t{ham_count}')
    print(f'{word}\t1\t0')            

else:
    print(f'{word}\t1\t0')            
    print(f'{word}\t1\t{spam_count}')            


############ (END) YOUR CODE #########