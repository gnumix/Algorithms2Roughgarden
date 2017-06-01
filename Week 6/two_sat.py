from kosaraju_algorithm import kosaraju_algorithm
from collections import defaultdict


def two_sat(n, forward, reverse):
    '''
    INPUT: Int, DefaultDict, DefaultDict
    OUTPUT: Boolean

    Compute the SCCs (strongly connected components) for the given graph. If a
    node and its complement are in the same SCC, then return False (i.e., the
    conditions of the 2SAT problem are not satisfiable). Elsewise, return True.
    '''
    components, sizes = kosaraju_algorithm(forward, reverse)
    for leader in components:
        nodes = set(components[leader])
        for node in nodes:
            if -node in nodes:
                return False
    return True


def read_file(filename):
    '''
    INPUT: String
    OUTPUT: Int, DefaultDict, DefaultDict

    Read the given file. The first line contains the number of variables, which
    is also the number of clauses. Each subsequent line specifies a clause
    consisting of 2 literals, with '-' denoting logical "not". Create the
    forward and reverse graphs that are needed for Kosaraju's algorithm. Each
    clause (x1, x2) results in 2 directed edges: (-x1, x2) and (-x2, x1).
    '''
    forward, reverse = defaultdict(list), defaultdict(list)
    with open(filename) as f:
        n = int(f.readline())
        for line in f:
            v1, v2 = map(int, line.split())
            # Forward Graph
            forward[-v1].append(v2)
            forward[-v2].append(v1)
            # Reverse Graph
            reverse[v2].append(-v1)
            reverse[v1].append(-v2)
    print('Finished Reading {}\n'.format(filename))
    return n, forward, reverse


if __name__ == '__main__':
    divider = '\n{}\n'.format('-' * 60)
    filenames = ['2sat{}.txt'.format(i + 1) for i in range(6)]
    satisfied = []

    for filename in filenames:
        n, forward, reverse = read_file(filename)
        s = two_sat(n, forward, reverse)
        print(s)
        satisfied.append(s)
        print(divider)

    print('Answer:\t{}'.format(''.join(str(int(s)) for s in satisfied)))
    # Answer = 101100
