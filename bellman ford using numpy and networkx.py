import networkx as nx
import numpy as np

def bellman_ford(graph, start_node):
    """
    return predecessors and shortest path lengths on shortest paths in weighted graphs
    https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.shortest_paths.weighted.bellman_ford.html
    """
    A = np.array(graph)
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

    try:
        predescesor, distance = nx.bellman_ford(G, start_node)
    except:
        #if there is a negative cycle then return all bunnies
        return [x for x in range(len(graph)-2)]
    return predescesor, distance

def all_pairs_shortest_paths(graph):
    """
    return 2d array of all_pairs_shortest_paths of directed weighted graph.
    Simply runs bellman_ford starting at each vertex.
    e.g. [0][1] = 2 means shortest distance between nodes 0 and 1 is 2
    """
    A = np.array(graph)
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

    apsp=[]
    for i in range(len(graph)):
        try:
            pred, dist = nx.bellman_ford(G, i)
            apsp.append(list(dist.values()))
        except:
            #if there is a negative cycle then return all bunnies
            return [x for x in range(len(times)-2)]
    return apsp

graph = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
graph = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]

print(bellman_ford(graph, 0))
#print(all_pairs_shortest_paths(graph))
