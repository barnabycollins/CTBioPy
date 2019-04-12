import time
import networkx as nx
import matplotlib as mpl

def WPGMA(filename):
    start = time.time()
    lines = []

    matrixfile = open(filename)
    for line in matrixfile:
        print(line, end="")
        lines.append(line.split())
    matrixfile.close()

    n = len(lines)-1
    matrix = [[0 for i in range(n)] for j in range(n)]
    species = {}
    for line in range(n):
        species[line] = lines[line+1][0]
        for index in range(n):
            matrix[line][index] = int(lines[line+1][index+1])

    print("\n", matrix, "\n", species)
    
    toDo = [i for i in range(n)]

    while (len(toDo) > 0):
        # find minimum
        for i in toDo:
            wack

        # update graph
        
        # add column & row

    """ matrix = {}
    dists = set()
    for line in lines[1:]:
        matrix[line[0]] = {}
        for index in range(1, len(line)):
            val = int(line[index])
            matrix[line[0]][lines[0][index]] = val
            dists.add(val) """
    
    


    end = time.time()
    print("\nTime taken:", end-start)

WPGMA('matrix1.txt')