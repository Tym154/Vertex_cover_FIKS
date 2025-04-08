from graph_class import graph
from input_loader import load_input

V, E_num, E = load_input()

this_is_a_graph = graph(E_num,V,E)

print(this_is_a_graph.nodes)

