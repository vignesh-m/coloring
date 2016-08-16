"""Graph functions"""


def read_graph(filename):
    """
    Reads graph from file.

    graph format:
    n m
    <m lines of> u v
    where n=no. of vertices , m=no. of edges
    0<=u,v<n and there is an edge from u to v
    """
    file = open(filename, mode='r')
    n, m = map(int, file.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, file.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph


def cycle_graph(n):
    """
    Constructs C_n - the cycle graph with n vertices
    """
    if n < 2:
        return None
    elif n == 2:
        return complete_graph(2)
    else:
        return [[(v + 1) % n, (v - 1 + n) % n]
                for v in range(n)]


def complete_graph(n):
    """
    Constructs K_n - the complete graph with n vertices
    """
    if n < 1:
        return None
    else:
        graph = [list(range(n)) for _ in range(n)]
        for i in range(n):
            graph[i].remove(i)
        return graph


def is_coloring(graph, coloring):
    """
    Checks if a coloring is valid
    """
    for u, row in enumerate(graph):
        for v in row:
            if coloring[u] == coloring[v]:
                return False
    return True


def max_degree(graph):
    """Returns max degree of the graph."""
    return max(map(len, graph))


def permute_graph(graph, permutation):
    """Permutes the vertices of graph according to given list.
    List indices are permuted to values, i.e,
    [2,0,1] is the permutation 0->2 1->0 2->1
    """
    n = len(graph)
    graph = [graph[permutation[i]] for i in range(n)]
    for i, row in enumerate(graph):
        graph[i] = [permutation[v] for v in row]
    return graph
