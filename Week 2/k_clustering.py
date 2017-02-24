import networkx as nx


def k_clustering(k, distances, n):
    '''
    INPUT: Int, List, Int
    OUTPUT: Int

    Given a number of clusters, find the minimum distance between the clusters.
    '''
    # Use the UnionFind data structure provided by the NetworkX graph module.
    unionfind = nx.utils.UnionFind()
    # Sort the list of distances and their corresponding nodes, by distance.
    distances = sorted(distances, key=lambda x: x[0])
    i = 0
    while n >= k:
        distance, (node1, node2) = distances[i]
        i += 1
        if unionfind[node1] != unionfind[node2]:
            unionfind.union(node1, node2)
            n -= 1
    return distance


if __name__ == '__main__':
    distances = []
    with open('clustering1.txt') as f:
        # First line is number of nodes; also the initial number of clusters.
        n = int(f.readline())
        for line in f:
            node1, node2, distance = map(int, line.split())
            distances.append((distance, (node1, node2)))

    k = 4
    min_distance = k_clustering(k, distances, n)
    print('Number Of Clusters:\t{}'.format(k))
    print('Minimum Distance:\t{}'.format(min_distance))
    # Answer = 106
