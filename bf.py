from ILP_solver import ILP
from graph_class import graph
from input_loader import load_input
import time
import os, sys
import brute_force

V, E_num, E = load_input()

this_is_a_graph = graph(E_num,V,E)

start = time.time()
     
removedV=brute_force.brute_force(this_is_a_graph) 
runtime=(time.time()-start)
print(f"""
          Problém-ILP V:{V}, E:{E_num}
          Doba běhu: {runtime},
          ID oddělaných Vrcholů: {removedV}
          """)
    