import networkx as nx
import matplotlib.pyplot as plt
import math

def find_height(node):
    return math.floor(math.log((node),2))

def build_binary_tree(num_nodes):
    """return binary tree graph"""
    G=nx.Graph()

    # add root node
    if num_nodes > 0:
        G.add_node(1)
    else:
        return
    
    # set to + 1 to fix python indexing
    num_nodes += 1
    
    # for every index starting at 2 create node and connect it to its parent
    for i in range(2, num_nodes):
        G.add_node(i)
        G.add_edges_from([(i//2, i)])
        
    return G

def print_graph(G, length = 1, width = 1):
    """print graph using networkx and matplotlib. TODO: add axes and axes labels/title/legend, evenly split nodes around middle"""
    pos = {1 : (0,0)}
    pos = {}
    num_nodes = G.number_of_nodes()
    tree_height = find_height(num_nodes)
    level_length = length / (tree_height + 1)
    middle_width = width / 2
    
##    print(find_height(1))
##    print(tree_height)
##    print(level_height)

    # set the x, y position of every node
    for height in range(tree_height + 1):
        nodes = 2 ** height
        for node in range(nodes):
            level_width = ((middle_width) / (nodes))
            x = (node + 1) * (width / (nodes + 1))  # evenly split the width to all nodes + 1
            y = length - (height * level_length)
            pos[node + 2 ** height] = (x, y)
##            if i < height_num_nodes // 2:    # handle nodes on left side
##                # split width into 2 then split each space evenly between all nodes at height
##                pos[i + 2 ** h] = (middle_width - (level_width / i))
##            else:
##                pos[i + 2 ** h] = (middle_width + (level_width / i)) 
                
    nx.draw(G, pos, with_labels=True) # label nodes
    plt.show()

if __name__ == "__main__":
    G = build_binary_tree(15)
    print_graph(G)
