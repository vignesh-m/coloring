""" Graph vertex coloring algorithms."""
from itertools import product
from graph import is_coloring, max_degree, permute_graph
from random import choice


def brute_force_color(graph, k=None):
    """
    Finds a k-coloring of graph by trying all k^n possibilities.
    Returns coloring if it exists, none otherwise
    Finds minimum coloring upto limit of 10 if no k is given.
    """
    n = len(graph)

    def color(k):
        for coloring in product(range(k), repeat=n):
            if is_coloring(graph, coloring):
                return coloring
        return None
    if k is None:
        for i in range(10):
            coloring = color(i)
            if coloring is not None:
                return (i, color(i))
        return (k, None)
    else:
        return (k, color(k))


def greedy_unordered_color(graph, k=None, random=True):
    """
    Tries a greedy coloring of the graph.
    If k is given returns None if the coloring is invalid, otherwise returns the coloring.
    Returns a coloring of size max_degree(graph)+1 (which always exists) if k is None.
    If random is True, colors are chosen randomly, otherwise smallest available is chosen
    """
    n = len(graph)

    def color(k):
        all_colors = set(range(n))
        colors = [-1 for _ in range(n)]
        for v in range(n):
            neighbours = set([colors[u] for u in graph[v]])
            left = all_colors.difference(neighbours)
            if left:
                if random:
                    colors[v] = choice(tuple(left))
                else:
                    colors[v] = min(left)
            else:
                return None
        return (max(colors) + 1, colors)

    if k is None:
        return color(k)
    else:
        return color(max_degree(graph) + 1)


def greedy_ordered_color(graph, k=None):
    """
    Similar to greedy_unordered_color but assigns to largest degree first.
    If d1>=d2>=... dn are the degrees, finds a 1+max_i(min(di,i-1)) coloring
    """
    if k is not None:
        return greedy_unordered_color(graph, k)
    else:
        degrees = [(len(row), i) for i, row in enumerate(graph)]
        degrees.sort(reverse=True)
        return greedy_unordered_color(permute_graph(graph, [x[1] for x in degrees]), random=False)

greedy_color = greedy_ordered_color
