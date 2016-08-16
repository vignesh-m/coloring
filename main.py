from graph import read_graph
from coloring import brute_force_color


def main():
    graph = read_graph('sample_graph')
    print(graph)
    print(brute_force_color(graph, 3))

if __name__ == '__main__':
    main()
