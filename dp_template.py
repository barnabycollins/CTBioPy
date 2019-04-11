#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

def score(i, j):
    b1 = seq1[i-1]
    b2 = seq2[j-1]
    last = scores[i-1][j-1]
    if (b1 == b2):
        if (b1 == "A"):
            biggest = 4 + last
        elif (b1 == "C"):
            biggest = 3 + last
        elif (b1 == "G"):
            biggest = 2 + last
        elif (b1 == "T"):
            biggest = 1 + last

    else:
        biggest = -3 + last
    
    back = [-1, -1]
    
    p = scores[i-1][j] - 2
    if (p > biggest):
        biggest = p
        back = [-1, 0]
    
    p = scores[i][j-1] - 2
    if (p > biggest):
        biggest = p
        back = [0, -1]

    return biggest, back


def populateMatrices():
    x = len(scores[0])
    y = len(scores)
    
    for i in range(1, x):
        scores[0][i] = -2*i
        backtrack[0][i] = [0,-1]
    
    for i in range(1, y):
        scores[i][0] = -2*i
        backtrack[i][0] = [-1, 0]
        for j in range(1, x):
            scores[i][j], backtrack[i][j] = score(i, j)

def show():
    for i in scores:
        for j in i:
            print(f'{j:3d}', end=' ')
        print()
        
    print()
    for i in backtrack:
        print(i)

def getAlignments():
    cur = [len(scores)-1, len(scores[0])-1]
    best_alignment = ['','']
    val = backtrack[cur[0]][cur[1]]
    while val != [0, 0]:
        if (val == [-1, -1]):
            al = [seq2[cur[1]-1], seq1[cur[0]-1]]
        
        elif (val == [-1, 0]):
            al = [" ", seq1[cur[0]-1]]
            
        else:
            al = [seq2[cur[1]-1], " "]
        
        for i in range(2):
            best_alignment[i] = al[i] + best_alignment[i]
            cur[i] += val[i]
        
        val = backtrack[cur[0]][cur[1]]
    
    return best_alignment

# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 


scores = [[0 for i in range(len(seq2)+1)] for i in range(len(seq1)+1)]
backtrack = [[[0,0] for i in range(len(seq2)+1)] for i in range(len(seq1)+1)]
populateMatrices()
#show()
best_score = scores[-1][-1]
best_alignment = getAlignments()

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start
# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

