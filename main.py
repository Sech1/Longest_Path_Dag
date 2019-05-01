import networkx as nx

from graph import *


def main():
    graphs = read_in_files()
    for graph in graphs:
        dag_sp(graph, graph.sources, 14)


def read_in_files():
    graphs = list()
    files = ['input/BAinCS.gml', 'input/BSinCS.gml', 'input/BSinECE.gml']

    for file in files:
        with open(file) as file:
            gml = file.read()
        graph = nx.parse_gml(gml)
        print(graph)
        graph = nx.convert_node_labels_to_integers(graph)
        num_nodes = int(graph.number_of_nodes())
        out_graph = Graph(num_nodes)
        out_graph.sources = list(graph.nodes)

        for u, v, a in graph.edges(data=True):
            out_graph.graph_edges_weights[u].append([v, 1])
        graphs.append(out_graph)
    return graphs


def topological_sort(graph, current_vertex, visited, stack):
    # creating a list of bools for visited, index 0 is null because we're starting at 1
    # visited = [False] * (graph.vertices + 1)
    # creating a recursion stack to detect for cycle 0 is null because we're starting at 1
    # top_list = []
    visited[current_vertex] = True
    stack = stack

    if current_vertex in graph.graph_edges_weights.keys():
        for node, weight in graph.graph_edges_weights[current_vertex]:
            if not visited[node]:
                topological_sort(graph, node, visited, stack)

    stack.append(current_vertex)


def dag_sp(graph, source_node_list, target_node):
    out_list = defaultdict(list)
    for source in source_node_list:
        visited = [False] * int(graph.vertices + 1)
        stack = []

        for i in range(1, graph.vertices + 1):
            if not visited[i]:
                topological_sort(graph, source, visited, stack)

        distance = [float("-inf")] * int(graph.vertices + 1)
        distance[source] = 0
        shortest_path = [-1] * int(graph.vertices)
        while stack:
            index = stack.pop()
            for node, weight in graph.graph_edges_weights[index]:
                if distance[node] < distance[index] + weight:
                    distance[node] = distance[index] + weight
                    shortest_path[node] = int(index)
        for k in range(target_node, int(target_node + 1)):
            print_recursive(shortest_path, k, out_list, source)
    source_longest = max(out_list, key=lambda x: len(out_list[x]))
    longest_path = out_list[source_longest]
    print("DAG SP Longest Path Output: ")
    print("SOURCE: " + str(source_longest))
    print("It's path is:")
    print(longest_path)
    print('\n')


def print_recursive(shortest_path, vertex, out_list=None, source=None):
    if vertex < 0:
        return
    print_recursive(shortest_path, shortest_path[vertex], out_list, source)
    out_list[source].append(int(vertex))


if __name__ == '__main__':
    main()
