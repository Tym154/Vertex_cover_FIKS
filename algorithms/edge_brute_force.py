from infrastructure.graph_class import graph

def edge_brute_force(input_graph : graph):
    vertices = input_graph.vertices
    edges = input_graph.get_edges()

    for k in range(1, len(vertices)):
        vertices_to_remove = edge_brute_force_solve(k, edges, vertices, [])
        if vertices_to_remove:
            return vertices_to_remove


def edge_brute_force_solve(k, edges, vertices, removed_vertices):
    if k == 0 and not edges:
        return removed_vertices
    
    if k == 0 and edges:
        return False
    
    edge = edges[0]
    for i in edge:
        new_edges = [e for e in edges if i not in e]
        new_vertices = [v for v in vertices if v != i]

        result = edge_brute_force_solve(k-1, new_edges, new_vertices, removed_vertices + [i])

        if result:
            return list(result)
    
    return False