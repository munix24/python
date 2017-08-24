import itertools
import sys

def all_pairs_shortest_paths(graph):
    """
    return 2d array of all_pairs_shortest_paths of directed weighted graph.
    e.g. [0][1] = 2 means shortest distance between nodes 0 and 1 is 2
    """
    rows = len(graph)
    cols = len(graph[0])
    apsp = [[0 for a in range(cols)] for b in range(rows)]
    for a in range(rows):
        for b in range(cols):
            if a == 0:
                for c in range(cols):
                    apsp[b][c] = sys.maxsize
                apsp[b][b] = 0  #node to itself = 0 
            for c in range(rows):
                for d in range(cols):
                    if apsp[b][c] != sys.maxsize and apsp[b][c] + graph[c][d] < apsp[b][d]:
                        apsp[b][d] = apsp[b][c] + graph[c][d]
    return apsp

##times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
graph = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]

print(all_pairs_shortest_paths(graph))
