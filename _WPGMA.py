import time
import networkx as nx
import matplotlib.pyplot as plt

def WPGMA(filename):
    start = time.time()
    lines = []
    printqueue = ''
    matrixfile = open(filename)
    for line in matrixfile:
        printqueue += line
        lines.append(line.split())
    matrixfile.close()

    n = len(lines)-1
    matrix = [[0 for i in range(n)] for j in range(n)]
    species = {}
    for line in range(n):
        species[line] = lines[line+1][0]
        for index in range(line):
            matrix[line][index] = int(lines[line+1][index+1])
    
    spkeys = list(species.keys())
    
    toDo = [i for i in range(n)]
    G = nx.Graph()
    posns = {}
    lv0count = 0

    while (len(toDo) > 1):
        # find minimum
        first = toDo[1]
        second = toDo[0]
        minimum, minloc = matrix[first][second], [first, second]
        for i in toDo:
            for j in toDo:
                if (j >= i):
                    break
                
                cur = matrix[i][j]
                if (cur < minimum):
                    minimum, minloc = cur, [i, j]
        

        toDo.remove(minloc[0])
        toDo.remove(minloc[1])
        
        newidx = len(matrix)
        matrix.append([0 for i in range(newidx)])
        loc1 = minloc[0]
        loc2 = minloc[1]
        for i in toDo:
            if (i > loc1):
                # loc1 always > loc2 therefore no need for a check
                matrix[newidx][i] = (matrix[i][loc1] + matrix[i][loc2])/2

            else:
                if (i > loc2):
                    matrix[newidx][i] = (matrix[loc1][i] + matrix[i][loc2])/2
                
                else:
                    matrix[newidx][i] = (matrix[loc1][i] + matrix[loc2][i])/2
        matrix[newidx].append(0)
        toDo.append(newidx)

        for i in minloc:
            if (i in spkeys):
                G.add_node(i)
                posns[i] = (lv0count, 0)
                lv0count += 1

        species[newidx] = species[loc1]+species[loc2]
        G.add_node(newidx)
        G.add_edges_from([(loc1, newidx), (loc2, newidx)])
        pos1 = posns[loc1]
        pos2 = posns[loc2]
        posns[newidx] = ((pos1[0]+pos2[0])/2, max(pos1[1], pos2[1])+1)
        printqueue += "\n\n{:8} ".format('')
        for i in toDo:
            printqueue += "{:>8} ".format(species[i])
        
        printqueue += "\n"

        for i in toDo:
            printqueue += "{:8} ".format(species[i])
            for j in toDo:
                if (i > j):
                    a = i
                    b = j
                else:
                    a = j
                    b = i
                
                printqueue += "{:8.0f} ".format(matrix[a][b])
            printqueue += "\n"

    print(printqueue)
    nx.draw(G, with_labels=True, labels=species, pos=posns)
    plt.savefig(filename[:-4] + ".png")
    plt.clf()
    end = time.time()
    print("\nTime taken:", end-start)

WPGMA('matrix1.txt')
WPGMA('matrix2.txt')