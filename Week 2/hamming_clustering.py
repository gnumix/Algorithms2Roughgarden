import networkx as nx
from collections import Counter
from itertools import combinations


def hamming_clustering(nodes, num_bits, min_distance):
    '''
    INPUT: Counter, Int, Int
    OUTPUT: Int

    Return the number of clusters such that the distance between any 2 nodes
    that are in different clusters is at least the given Hamming distance.
    '''
    num_clusters = len(nodes)
    unionfind = nx.utils.UnionFind()
    for distance in range(1, min_distance):
        for node1, node2 in distance_pairs(nodes, num_bits, distance):
            if unionfind[node1] != unionfind[node2]:
                unionfind.union(node1, node2)
                num_clusters -= 1
    return num_clusters


def distance_pairs(nodes, num_bits, distance):
    '''
    INPUT: Counter, Int, Int
    OUTPUT: Set

    Return a set of all pairs of nodes that have the given Hamming distance.

    Note: The ^ (caret) operator applies the bitwise XOR operation to 2 ints.
    For example:
    >>> 5 ^ 9
    12

    0101  # 2^0 + 2^2 = 1 + 4 = 5
    1001  # 2^0 + 2^3 = 1 + 8 = 9
    ----  # Apply XOR Vertically
    1100  # 2^2 + 2^3 = 4 + 8 = 12
    '''
    pairs = set()
    for permutation in distance_permutations(num_bits, distance):
        for node in nodes:
            node_xor = node ^ permutation
            if node_xor in nodes:
                pairs.add((node, node_xor))
    return pairs


def distance_permutations(num_bits, distance):
    '''
    INPUT: Int, Int
    OUTPUT: Set

    Return a set of all possible places where 2 (binary) numbers might differ,
    given the desired Hamming distance. Also convert the distances to base 10.
    '''
    distances = set()
    for indices in combinations(range(num_bits), distance):
        distances.add(sum(2 ** i for i in indices))
    return distances


if __name__ == '__main__':
    nodes = Counter()
    with open('clustering_big.txt') as f:
        num_nodes, num_bits = map(int, f.readline().split())
        for line in f:
            # Convert the given binary string to a base-10 int before saving.
            nodes[int(line.replace(' ', ''), 2)] += 1

    min_distance = 3
    num_clusters = hamming_clustering(nodes, num_bits, min_distance)
    print('Minimum Distance:\t{}'.format(min_distance))
    print('Number Of Clusters:\t{}'.format(num_clusters))
    # Answer = 6118
