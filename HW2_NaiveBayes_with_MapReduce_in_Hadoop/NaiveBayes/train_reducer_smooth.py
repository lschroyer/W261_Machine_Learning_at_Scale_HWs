#!/usr/bin/env python

import os
import sys                                                  
import numpy as np  

#################### YOUR CODE HERE ###################

# Mapper format
#A  !line_counter  1  3
#A  !part_counter  3  8
#A  !total         0  11
#A  beijing        0  1
#A  chinese        0  1
#A  chinese        0  1


# Loop over the data to get the unique word count
#initialize
current_word = None
unique_word_counter = 0
total_counter = 0
line_counter_ham, line_counter_spam = 0,0
part_counter_ham, part_counter_spam = 0,0


for line in sys.stdin:
    key, word, col_3, col_4 = line.split('\t')
    col_3 = int(col_3)
    col_4 = int(col_4)
    if word != current_word and word != "!total" and word != "!line_counter" and word != "!part_counter":
        unique_word_counter += 1
    current_word = word
    
    if word == "!total":
        total_counter += col_4
    elif word == "!line_counter":
        line_counter_ham += col_3   
        line_counter_spam += col_4   
    elif word == "!part_counter":
        part_counter_ham += col_3   
        part_counter_spam += col_4 
    else:
        print(f'{key}\t{word}\t{col_3}\t{col_4}')

print(f'{key}\t!!unique_words\t0\t{unique_word_counter}')
print(f'{key}\t!total\t0\t{total_counter}')
print(f'{key}\t!line_counter\t{line_counter_ham}\t{line_counter_spam}')
print(f'{key}\t!part_counter\t{part_counter_ham}\t{part_counter_spam}')



#################### (END) YOUR CODE ###################