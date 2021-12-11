#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    <specify record format here>
OUTPUT:
    <specify record format here>
    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
"""
##################### YOUR CODE HERE ####################

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#initialize
current_word = None

grand_total = 0
ham_line_count, spam_line_count = 0, 0
ham_partial_count, spam_partial_count = 0, 0
class0_partialCount, class1_partialCount = 0, 0
unique_words = 0

# read input key-value pairs from standard input
for line in sys.stdin:
    
    key, word, col_3, col_4 = line.split('\t')
    col_3 = int(col_3) #ham counter
    col_4 = int(col_4) #spam counter
    
    
    if word == "!total":
        grand_total += col_4
    elif word == "!line_counter":
        ham_line_count += col_3
        spam_line_count += col_4
    elif word == "!part_counter":
        ham_partial_count += col_3
        spam_partial_count += col_4    
    elif word == "!!unique_words":
        unique_words = int(col_4)
        
#     if word == "!total":
#         grand_total = col_4
#     elif word == "!line_counter":
#         ham_line_count = col_3
#         spam_line_count = col_4
#     elif word == "!part_counter":
#         ham_partial_count = col_3
#         spam_partial_count = col_4    
#     elif word == "!!unique_words":
#         unique_words = int(col_4)
    
    #--------Reduce for non-laplace smoothing---------
    if unique_words == 0 and word != "!total" and word != "!line_counter" and word != "!part_counter" and word != "!!unique_words":
#     elif col_3 == 1:
        if col_3 == 1:
            if word == current_word:
                class0_partialCount += col_3
            else:
                if current_word:
                    pc_ham = class0_partialCount/ham_partial_count
                    pc_spam = class1_partialCount/spam_partial_count
                    print(f'{current_word}\t{class0_partialCount},{class1_partialCount},{pc_ham},{pc_spam}')

                    class0_partialCount, class1_partialCount = 0,0
                current_word, class0_partialCount = word, col_3

        else:
            if word == current_word:
                class1_partialCount += col_4
            else:
                if current_word:
                    pc_ham = class0_partialCount/ham_partial_count
                    pc_spam = class1_partialCount/spam_partial_count
                    print(f'{current_word}\t{class0_partialCount},{class1_partialCount},{pc_ham},{pc_spam}')

                    class0_partialCount, class1_partialCount = 0,0
                current_word, class1_partialCount = word, col_4
    
    
    #-------Reduce for laplace smoothing ----------
    elif unique_words > 0 and word != "!total" and word != "!line_counter" and word != "!part_counter" and word != "!!unique_words":

        if col_3 == 1:
            if word == current_word:
                class0_partialCount += col_3
            else:
                if current_word:
                    pc_ham = (class0_partialCount + 1)/(ham_partial_count + unique_words)
                    pc_spam = (class1_partialCount + 1)/(spam_partial_count + unique_words)
                    print(f'{current_word}\t{class0_partialCount},{class1_partialCount},{pc_ham},{pc_spam}')

                    class0_partialCount, class1_partialCount = 0,0
                current_word, class0_partialCount = word, col_3

        else:
            if word == current_word:
                class1_partialCount += col_4
            else:
                if current_word:
                    pc_ham = (class0_partialCount + 1)/(ham_partial_count + unique_words)
                    pc_spam = (class1_partialCount + 1)/(spam_partial_count + unique_words)
                    print(f'{current_word}\t{class0_partialCount +1},{class1_partialCount+1},{pc_ham},{pc_spam}')

                    class0_partialCount, class1_partialCount = 0,0
                current_word, class1_partialCount = word, col_4        
            

#Final print for non-smoothing:            
if unique_words == 0 and word != "!total" and word != "!line_counter" and word != "!part_counter" and word != "!!unique_words":
    pc_ham = class0_partialCount/ham_partial_count
    pc_spam = class1_partialCount/spam_partial_count
    print(f'{current_word}\t{class0_partialCount},{class1_partialCount},{pc_ham},{pc_spam}')

#Final smoothing print    
elif unique_words > 0 and word != "!total" and word != "!line_counter" and word != "!part_counter" and word != "!!unique_words":
    pc_ham = (class0_partialCount + 1)/(ham_partial_count + unique_words)
    pc_spam = (class1_partialCount + 1)/(spam_partial_count + unique_words)
    print(f'{current_word}\t{class0_partialCount+1},{class1_partialCount+1},{pc_ham},{pc_spam}')

#calculating class priors:
#of spam docs/total docs or ham docs/total docs
print(f'ClassPriors\t{ham_line_count},{spam_line_count},{ham_line_count/(spam_line_count + ham_line_count)},{spam_line_count/(spam_line_count + ham_line_count)}')


##################### (END) CODE HERE ####################