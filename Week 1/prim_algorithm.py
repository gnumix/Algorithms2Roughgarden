import networkx as nx
import heapq


def prim_algorithm(graph, start):
    '''
    INPUT: NetworkX Graph, Int
    OUTPUT: Int

    Implement Prim's algorithm: find the MST (minimum spanning tree) for a
    weighted, undirected graph. Return the cost (total weight) of the MST.
    This implementation is very similar to that for Dijkstra's algorithm.
    '''
    cost = 0
    heap = []
    # Set the start node to 'explored', and push its neighbors to the heap.
    graph.node[start]['explored'] = True
    graph, heap = push_heap(graph, heap, start)
    # The min-heap is ordered by the weights between 2 nodes of the graph.
    while heap:
        # Pop from heap to return the node-pair with the smallest weight.
        weight, (node1, node2) = heapq.heappop(heap)
        # First node has been explored, but second node may not have been.
        if not graph.node[node2]['explored']:
            graph.node[node2]['explored'] = True
            cost += weight
            graph, heap = push_heap(graph, heap, node2)
    return cost


def push_heap(graph, heap, node):
    '''
    INPUT: NetworkX Graph, List, Int
    OUTPUT: NetworkX Graph, List

    Use a min-heap to keep track of the weights found, in ascending order.
    '''
    for neighbor in graph[node]:
        # If a neighbor hasn't been explored, add the nodes and the weight.
        if not graph.node[neighbor]['explored']:
            heapq.heappush(heap,
                           (graph[node][neighbor]['weight'], (node, neighbor)))
    return graph, heap


if __name__ == '__main__':
    graph = nx.Graph()
    with open('edges.txt') as f:
        num_nodes, num_edges = map(int, f.readline().split())
        for line in f:
            node1, node2, weight = map(int, line.split())
            graph.add_edge(node1, node2, weight=weight)
    nx.set_node_attributes(graph, 'explored', False)

    start = 1
    print('Minimum Spanning Tree (Weight):\t{}'
          .format(prim_algorithm(graph, start)))
    # Answer = -3612829
