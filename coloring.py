""" Graph vertex coloring algorithms."""
from itertools import product
from graph import is_coloring


def brute_force_color(graph, k=2):
    """
    Finds a k-coloring of graph by trying all k^n possibilities.
    Returns coloring if it exists, none otherwise
    """
    n = len(graph)
    for coloring in product(range(k), repeat=n):
        if is_coloring(graph, coloring):
            return coloring
    return None
