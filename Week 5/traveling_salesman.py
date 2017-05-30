import numpy as np
import itertools
from sklearn.metrics.pairwise import euclidean_distances
from time import time


def traveling_salesman(source, cities, num_cities):
    '''
    INPUT: List, Int
    OUTPUT:

    Find the minimum distance that a traveling salesman must travel, in order
    to visit all cities once, before returning back to origin (source) city.
    '''
    distances = euclidean_distances(cities)  # Calculates pairwise distances.
    # Base Case
    t1 = time()
    A = np.zeros((binary_hash(range(num_cities)) + 1, num_cities)) + np.inf
    A[binary_hash([source]), 0] = 0
    t2 = time()
    print('Initialization:\t{:>6.1f} Seconds'.format(t2 - t1))
    # List of cities that excludes source city that salesperson starts from.
    other_cities = [i for i in range(num_cities) if i != source]
    for m in range(1, num_cities):  # m = Subproblem (Subset) Size - 1
        t1 = time()  # Time
        for combination in itertools.combinations(other_cities, m):
            subset = (source,) + combination  # Add source city back to subset.
            subset_key = binary_hash(subset)  # Compute binary hash for subset.
            for j in combination:  # Only cities in subset that are not source.
                # A[S, j] = min_[k in S, k ≠ j] { A[S - j, k] + c[k, j] }
                min_distance = float('inf')
                for k in subset:
                    if k != j:
                        prev_key = subset_key - (2 ** j)
                        min_distance = min(min_distance,
                                           A[prev_key, k] + distances[k, j])
                A[subset_key, j] = min_distance
        t2 = time()  # Time
        print('Iteration {:>2}:\t{:>6.1f} Seconds'.format(m, t2 - t1))  # Time
    # Return final distance including last hop from last city back to source.
    min_distance = float('inf')
    subset_key = binary_hash(range(num_cities))
    for j in range(num_cities):
        if j != source:
            min_distance = min(min_distance,
                               A[subset_key, j] + distances[j, source])
    return min_distance


def binary_hash(subset):
    '''
    INPUT: List
    OUTPUT: Int

    Calculate a (unique) key given a sequence of (unique) numbers. Return hash.
    '''
    return sum(2 ** i for i in subset)


def read_file(filename):
    '''
    INPUT: String
    OUTPUT: Numpy Array, Int

    Read the given file. The first line contains the numbers of cities. Each
    subsequent line contains the x- and y- coordinate, respectively, of a city.
    '''
    with open(filename) as f:
        num_cities = int(f.readline())
        cities = np.zeros((num_cities, 2))
        for i, line in enumerate(f):
            cities[i, :] = list(map(float, line.split()))
    print('Finished Reading {}\n'.format(filename))
    return cities, num_cities


if __name__ == '__main__':
    cities, num_cities = read_file('tsp.txt')
    time1 = time()
    min_distance = traveling_salesman(0, cities, num_cities)
    time2 = time()
    print('\nMinimum Distance:\t{}'.format(min_distance))
    print('Time Required:\t{} Seconds'.format(time2 - time1))
    # Answer = 26442
    # Time Required: 5400 Seconds = 90 Minutes
