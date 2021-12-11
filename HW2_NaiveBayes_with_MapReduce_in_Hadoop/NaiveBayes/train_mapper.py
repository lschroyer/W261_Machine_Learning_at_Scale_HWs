#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.
INPUT:                                                    
    DocID \t true_class \t subject \t body                
OUTPUT:                                                   
    partitionKey \t word \t class0_partialCount,class1_partialCount       
    

Instructions:
    You know what this script should do, go for it!
    (As a favor to the graders, please comment your code clearly!)
    
    A few reminders:
    1) To make sure your results match ours please be sure
       to use the same tokenizing that we have provided in
       all the other jobs:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
       
Partitioning:
    In order to send the totals to each reducer, we need to implement
    a custom partitioning strategy.
    
    We will generate a list of keys based on the number of reduce tasks 
    that we read in from the environment configuration of our job.
    
    We'll prepend the partition key by hashing the word and selecting the
    appropriate key from our list. This will end up partitioning our data
    as if we'd used the word as the partition key - that's how it worked
    for the single reducer implementation. This is not necessarily "good",
    as our data could be very skewed. However, in practice, for this
    exercise it works well. The next step would be to generate a file of
    partition split points based on the distribution as we've seen in 
    previous exercises.
    
    Now that we have a list of partition keys, we can send the totals to 
    each reducer by prepending each of the keys to each total.
       
"""

import re                                                   
import sys                                                  
import numpy as np      

from operator import itemgetter
import os

#################### YOUR CODE HERE ###################
if os.getenv('mapreduce_job_reduces') == None:
    N = 1
else:
    N = int(os.getenv('mapreduce_job_reduces'))


# helper functions - hash map 
def makeIndex(key, num_reducers = N):
    """
    Mimic the Hadoop string-hash function.
    
    key             the key that will be used for partitioning
    num_reducers    the number of reducers that will be configured
    """
    byteof = lambda char: int(format(ord(char), 'b'), 2)
    current_hash = 0
    for c in key:
        current_hash = (current_hash * 31 + byteof(c))
    return current_hash % num_reducers

# helper function
def makeKeyFile(num_reducers = N):
    KEYS = list(map(chr, range(ord('A'), ord('Z')+1)))[:num_reducers]
    partition_keys = sorted(KEYS, key=lambda k: makeIndex(k,num_reducers))

    return partition_keys


# call your helper function to get partition keys
pKeys = makeKeyFile()
# print("pKeys:")
# print(pKeys)

def makePartitionFile():
    # returns a list of split points
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


pFile = makePartitionFile()

# print("pFile")
# print(pFile)

#initialize
spam_line_counter = 0
ham_line_counter = 0
spam_word_counter = 0
ham_word_counter = 0
TOTAL_WORDS = 0        
        
# read from standard input
for line in sys.stdin:
    # parse input
    docID, _class, subject, body = line.split('\t')
    _class = int(_class)
    
    # tokenize
    words = re.findall(r'[a-z]+', subject.lower() + ' ' + body.lower())
    keys = re.findall(r'[0-9]+', docID)[0]
    
    
    if _class == 1:
        ham = 0
        spam = 1
        spam_line_counter += 1
        
    elif _class == 0:
        ham = 1
        spam = 0
        ham_line_counter += 1
    
    # emit words and increment total counter
    
    #Prepend the approriate key by finding the bucket, and using the index to fetch the key. reverse hash
    for idx in range(N):
#         print("pFile[idx]:")
#         print(pFile[idx])
#         print("keys:", keys)
        if int(keys) < pFile[idx]:
            pkey = pKeys[idx]
#             print(str(pKeys[idx])+"\t"+keys+"\t"+", ".join(words))
            break
    
    
    
    
    for idx, word in enumerate(words):
        TOTAL_WORDS += 1
#         pkey = getPartitionKey(docID)
#         print(idx)
#         pkey = pKeys[idx]
#         print(str(pKeys[idx])+"\t"+docID+"\t"+word)
#         print(str(pkey)+"\t"+docID+"\t"+word)

        
        if _class == 1:
            ham = 0
            spam = 1
            spam_word_counter += 1
        
        elif _class == 0:
            ham = 1
            spam = 0
            ham_word_counter += 1
    
        print(f"{pkey}\t{word}\t{ham}\t{spam}")

# print("Pkeys:", pkey)
for key in pkey:
    print(f'{key}\t!total\t{_class}\t{TOTAL_WORDS}')
    print(f'{key}\t!line_counter\t{ham_line_counter}\t{spam_line_counter}')
    print(f'{key}\t!part_counter\t{ham_word_counter}\t{spam_word_counter}')

    

#################### (END) YOUR CODE ###################