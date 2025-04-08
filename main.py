from ILP_solver import ILP
from graph_class import graph
from input_loader import load_input
import time
import os, sys


def get_num(data):
    return int(data.split("-")[0])



dir = os.listdir("input")
sorted_dir=sorted(dir, key=get_num)
for file in sorted_dir:
    
    V, E_num, E = load_input(file)

    this_is_a_graph = graph(E_num,V,E)

    start = time.time()
     
    removedV=ILP(this_is_a_graph.vertices) 
    runtime=(time.time()-start)
    
    print(f"""
          Problém-ILP V:{V}, E:{E_num}
          Doba běhu: {runtime},
          ID oddělaných hran: {removedV}
          """)
    
    
        