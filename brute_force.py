from graph_class import graph
from itertools import combinations

def brute_force(input_graph : graph):
    nodes = input_graph.vertices.keys()
    edges = input_graph.get_edges()

    for i in range(1, len(nodes) + 1):
        for sub in combinations(nodes, i):
            if input_graph.is_vertex_cover(sub, edges):
                return list(sub)