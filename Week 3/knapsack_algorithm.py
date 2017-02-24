from time import time


def knapsack_algorithm(items, size):
    '''
    INPUT: List, Int
    OUTPUT: Int

    Solve the knapsack problem iteratively, rather than recursively, as Python
    doesn't deal well with deep recursion. Use two lists rather than a matrix
    to keep track of the knapsack and its items, to save on space. With each
    additional item seen, it only matters what the knapsack previously held.
    '''
    knapsack_1 = [0] * (size + 1)
    knapsack_2 = [0] * (size + 1)
    for i, (value, weight) in enumerate(items):
        if not (i + 1) % 100:
            print('Iteration {:4}'.format(i + 1))
        for s in range(size + 1):
            if (s - weight) < 0:
                knapsack_2[s] = knapsack_1[s]
            else:
                if knapsack_1[s] > (knapsack_1[s - weight] + value):
                    knapsack_2[s] = knapsack_1[s]
                else:
                    knapsack_2[s] = knapsack_1[s - weight] + value
        # Swap the 2 lists. The 'after' knapsack is now the 'before' knapsack.
        knapsack_1, knapsack_2 = knapsack_2, knapsack_1
    return knapsack_1[size]


def read_file(filename):
    '''
    INPUT: String
    OUTPUT: List, Int, Int

    Read the given file. The first line contains the size of the knapsack and
    the number of items. Each subsequent line corresponds to an item, with an
    associated value and weight, respectively. Save these items as a list of
    tuples. Return the list, as well as the knapsack size and number of items.
    '''
    items = []
    with open(filename) as f:
        size, n = map(int, f.readline().split())
        for line in f:
            items.append(tuple(map(int, line.split())))
    print('Finished Reading {}\n'.format(filename))
    return items, size, n


def print_answer(size, capacity, value):
    '''
    INPUT: String, Int, Int
    OUTPUT: None

    Print the knapsack capacity, and the maximum value the knapsack can hold.
    '''
    print('\nKnapsack ({}) - Size:\t{}'.format(size, capacity))
    print('Knapsack ({}) - Value:\t{}'.format(size, value))


if __name__ == '__main__':
    items_small, size_small, n_small = read_file('knapsack1.txt')
    value_small = knapsack_algorithm(items_small, size_small)
    print_answer('Small', size_small, value_small)
    # Answer 1 = 2493893

    print('\n{}\n'.format('-' * 60))

    items_large, size_large, n_large = read_file('knapsack_big.txt')
    time_0 = time()
    value_large = knapsack_algorithm(items_large, size_large)
    time_1 = time()
    print_answer('Large', size_large, value_large)
    print('Time Required (Seconds):\t{}'.format(time_1 - time_0))
    # Answer 2 = 4243395
    # Time Required: 1974 Seconds = 33 Minutes
