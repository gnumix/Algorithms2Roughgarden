from collections import defaultdict


def kosaraju_algorithm(forward, reverse):
    '''
    INPUT: Dictionary, Dictionary
    OUTPUT: DefaultDict, List

    Iterative, rather than recursive, implementation of Kosaraju's algorithm
    for finding the strongly connected components of a directed graph, because
    the recursive implementation flames out when dealing with large graphs.
    '''
    finished = visit_reverse(reverse)
    print('Finished Reverse Depth-First Search\n')

    components = visit_forward(forward, finished)
    print('Finished Forward Depth-First Search\n')

    sizes = [len(nodes) for leader, nodes in components.items()]
    return components, sorted(sizes, reverse=True)


def visit_reverse(reverse):
    '''
    INPUT: Dictionary
    OUTPUT: Dictionary

    Visit, using DFS, the reverse graph. Return the associated finish times.
    '''
    # Set for keeping track of which nodes have been visited at least once.
    visited = set()
    # Dictionary for keeping track of the finish time of visiting each node.
    finished = {}
    time = 0
    for vertex in reverse:
        # Use a LIFO (last-in-first-out) stack to visit nodes in DFS order.
        stack = [vertex]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                # Actually need to visit the node twice to get finish time.
                stack.append(node)
                # Check that the node points to/is the tail of other nodes.
                if node in reverse:
                    for neighbor in reverse[node]:
                        # If head node has not been visited, add to stack.
                        if neighbor not in visited:
                            stack.append(neighbor)
            else:
                # If node has been visited but does not have a finish time.
                if node not in finished:
                    finished[node] = time
                    time += 1
    return finished


def visit_forward(forward, finished):
    '''
    INPUT: Dictionary, Dictionary
    OUTPUT: DefaultDict

    Visit, using DFS, the forward graph in decreasing order of finish time.
    '''
    # Sort the dictionary of nodes and finishing times in descending order.
    finished_sorted = [(node, finished[node]) for node in
                       sorted(finished, key=finished.get, reverse=True)]
    # Set for keeping track of which nodes have been visited at least once.
    visited = set()
    # Use a defaultdict, with list as the default object, to track the SCCs.
    components = defaultdict(list)
    for vertex, time in finished_sorted:
        # Use a LIFO (last-in-first-out) stack to visit nodes in DFS order.
        stack = [vertex]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                # Newly visited nodes belong to to the current leader node.
                components[vertex].append(node)
                # Check that the node points to/is the tail of other nodes.
                if node in forward:
                    for neighbor in forward[node]:
                        # If head node has not been visited, add to stack.
                        if neighbor not in visited:
                            stack.append(neighbor)
    return components


if __name__ == '__main__':
    # While reading the file, create both the forward and the reverse graphs.
    forward, reverse = defaultdict(list), defaultdict(list)
    with open('SCC.txt') as f:
        for line in f:
            v1, v2 = list(map(int, line.strip().split()))
            forward[v1].append(v2)
            reverse[v2].append(v1)
    print('Finished Reading File\n')

    # Run Kosaraju's algorithm on the graphs; return the SCCs and their sizes.
    components, sizes = kosaraju_algorithm(forward, reverse)
    n = min(5, len(sizes))
    print('# Of Strongly Connected Components:\t{}'.format(len(sizes)))
    print('Top {} Strongly Connected Components:\t{}'.format(n, sizes[:n]))
