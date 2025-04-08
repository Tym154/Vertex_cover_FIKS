from pulp_introduction import ILP
from graph_class import graph
from input_loader import load_input
import time

V, E_num, E = load_input()
#print(E)

this_is_a_graph = graph(E_num,V,E)

start = time.time()
ILP(this_is_a_graph.vertices)
