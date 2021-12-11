#!/usr/bin/env python
"""
Reducer to calculate precision and recall as part
of the inference phase of Naive Bayes.
INPUT:
    ID \t true_class \t P(ham|doc) \t P(spam|doc) \t predicted_class
OUTPUT:
    precision \t ##
    recall \t ##
    accuracy \t ##
    F-score \t ##
         
Instructions:
    Complete the missing code to compute these^ four
    evaluation measures for our classification task.
    
    Note: if you have no True Positives you will not 
    be able to compute the F1 score (and maybe not 
    precision/recall). Your code should handle this 
    case appropriately feel free to interpret the 
    "output format" above as a rough suggestion. It
    may be helpful to also print the counts for true
    positives, false positives, etc.
"""
import sys
import numpy as np

# initialize counters
FP = 0.0 # false positives
FN = 0.0 # false negatives
TP = 0.0 # true positives
TN = 0.0 # true negatives
# current_docID = None
doc_num = 0
docID_list = []

# read from STDIN
for line in sys.stdin:
    # parse input
    docID, class_, pHam, pSpam, pred = line.split()
    # emit classification results first
    print(line[:-2], class_ == pred)
    
    # then compute evaluation stats
#################### YOUR CODE HERE ###################
#     print(docID, class_, pHam, pSpam, pred)
    if class_ == pred and int(class_) == 1:
#         print("TP")
        TP += 1
    elif class_ == pred and int(class_) == 0:
#         print("TN")
        TN += 1
    elif int(class_) == 1 and int(pred) == 0:
#         print("FN")
        FN += 1
    elif int(class_) == 1 and int(pred) == 0:
#         print("FP")
        FP += 1
    #if the prediction fails
    else:
        FP += 1
        FN += 1
        
    if len(docID) == 0:
        doc_num += 1
        docID_list.append(docID)       
    
    elif docID not in docID_list:
        doc_num += 1
        docID_list.append(docID)       
    
    
P = TP/(TP + FP)    
R = TP/(TP + FN)
A = (TP+TN)/(TP+FP+FN+TN)
F1 = TP/(TP + 0.5*(FP + FN))

print("Documents:", doc_num, sep = "\t")
print("True Positives:", TP, sep = "\t")
print("True Negatives:", TN, sep = "\t")
print("False Positives:", FP, sep = "\t")
print("False Negatives:", FN, sep = "\t")
print("Accuracy:", A, sep = "\t")
print("Precision:", P, sep = "\t")
print("Recall:", R, sep = "\t")
print("F-Score:", F1, sep = "\t")



















#################### (END) YOUR CODE ###################
    