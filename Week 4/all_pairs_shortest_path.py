import numpy as np
import networkx as nx
from time import time


def floyd_warshall(graph, num_nodes):
    '''
    INPUT: NetworkX Graph, Int
    OUTPUT: None or Float

    Use the Floyd-Warshall algorithm to calculate the shortest path amongst all
    pairs of vertices in a directed graph. If a negative cycle is found, return
    'None'. Otherwise, return the shortest distance found, of all the paths.
    '''
    # Base Case
    A = np.zeros((num_nodes, num_nodes)) + float('inf')
    np.fill_diagonal(A, 0)
    for node1, node2 in graph.edges():
        A[node1 - 1, node2 - 1] = graph[node1][node2]['weight']
    # A[i, j, k] = min( A[i, j, k - 1],
    #                   A[i, k, k - 1] + A[k, j, k - 1] )
    for k in range(num_nodes):
        # To calculate the latter expression (above), use Numpy broadcasting.
        # A = B_T[:, k] + C[k, :] ==> A[i, j] = B[i, k] + C[k, j]
        B = A[:, k, np.newaxis] + A[k, :]  # Add an axis, to take transpose.
        A = np.minimum(A, B)  # Returns the element-wise minimum of 2 arrays.
    # If diagonal contains a negative number, then a negative cycle was found.
    if np.any(np.diag(A) < 0):
        return None
    # Otherwise, return the shortest path distance amongst all the node pairs.
    return np.min(A)


def read_file(filename):
    '''
    INPUT: String
    OUTPUT: NetworkX Graph, Int, Int

    Read the given file. The first line contains the number of nodes and the
    number of edges. Each subsequent line corresponds to an edge, given by its
    tail, its head, and its weight, respectively. Save as a NetworkX graph.
    When done reading, return the graph, number of nodes, and number of edges.
    '''
    graph = nx.DiGraph()
    with open(filename) as f:
        num_nodes, num_edges = map(int, f.readline().split())
        for line in f:
            node1, node2, weight = map(int, line.split())
            graph.add_edge(node1, node2, weight=weight)
    print('Finished Reading {}\n'.format(filename))
    return graph, num_nodes, num_edges


if __name__ == '__main__':
    divider = '\n{}\n'.format('-' * 60)
    # filenames = ['g{}.txt'.format(i + 1) for i in range(3)]
    filenames = ['large.txt']
    distances = []

    for filename in filenames:
        graph, num_nodes, num_edges = read_file(filename)
        time_0 = time()
        distance = floyd_warshall(graph, num_nodes)
        time_1 = time()
        distances.append(distance)
        print('\n{} - Minimum Distance:\t{}'.format(filename, distance))
        print('Time Required (Seconds):\t{}'.format(time_1 - time_0))
        print(divider)

    min_distance = float('inf')
    changed = False
    for distance in distances:
        if distance is not None and distance < min_distance:
            min_distance = distance
            changed = True
    if not changed:
        min_distance = None
    print('Minimum Distance (Overall):\t{}'.format(min_distance))
    # Answer = -19
