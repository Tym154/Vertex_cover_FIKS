from graph_class import graph

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
    
    for remove_vertice in vertices:
        new_edges = [edge for edge in edges if remove_vertice not in edge]
        new_vertices = [vertice for vertice in vertices if vertice != remove_vertice]

        result = edge_brute_force_solve(k-1, new_edges, new_vertices, removed_vertices + [remove_vertice])

        if result:
            return list(result)
    
    return False