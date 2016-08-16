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


def is_coloring(graph, coloring):
    for u, row in enumerate(graph):
        for v in row:
            if coloring[u] == coloring[v]:
                return False
    return True
