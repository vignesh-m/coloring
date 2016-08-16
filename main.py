from graph import read_graph, complete_graph
from coloring import brute_force_color, greedy_color


def main():
    graph = read_graph('sample_graph')
    print(graph)
    print(brute_force_color(graph, 3))
    print('greedy color of K_10', greedy_color(complete_graph(10)))

if __name__ == '__main__':
    main()
