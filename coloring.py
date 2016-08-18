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


def greedy_unordered_color(graph, k=None, random=False):
    """
    Tries a greedy coloring of the graph.
    If k is given returns None if the coloring is invalid, otherwise returns the coloring.
    Returns a coloring of size max_degree(graph)+1 (which always exists) if k is None.
    If random is True, colors are chosen randomly, otherwise smallest available is chosen
    """
    n = len(graph)
    print(graph)

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
        if is_coloring(graph, colors):
            return (max(colors) + 1, colors)
        else:
            return None

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
        n = len(graph)
        degrees = [(len(row), i) for i, row in enumerate(graph)]
        degrees.sort(reverse=True)
        perm = [x[1] for x in degrees]
        n_cols, permuted_cols = greedy_unordered_color(permute_graph(graph, perm), random=False)
        actual_cols = [0 for _ in range(n)]
        for i in range(n):
            actual_cols[perm[i]] = permuted_cols[i]
        return n_cols, actual_cols

greedy_color = greedy_ordered_color


def planar_6_color(graph):
    """
    Gives a 6-coloring of a graph.
    This can be done greedily as a planar graph always has a vertex with
    degree<=5, and removing that vertex leaves a planar graph
    """
    INF = 100000
    n = len(graph)
    degrees = [[len(row), i] for i, row in enumerate(graph)]
    # We remove the smallest deg vertex and color the rest recursively.
    # To do this we use a fill order list which tells us the order of removal.
    # This is enough to color the graph.

    def color(order):
        colors = [-1 for _ in range(n)]
        all_colors = set(range(6))
        for v in order:
            adj_colors = set([colors[u] for u in graph[v]])
            colors[v] = min(all_colors - adj_colors)
        return colors

    fill_order = []
    for _ in range(n):
        deg, idx = min(degrees)
        if deg >= 5:
            print('Error: graph is not planar - reduction has min degree > 5')
            return None
        elif deg == INF:
            print('Error: ran out of vertices')
        else:
            fill_order.append(idx)
            for v in graph[idx]:
                # update undeleted neighbours
                if degrees[v][0] != INF:
                    degrees[v][0] -= 1
            # setting to inf deletes
            degrees[idx][0] = INF
    cols = color(fill_order)
    return max(cols) + 1, cols
