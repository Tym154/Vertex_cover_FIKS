from algorithms.ILP import ILP

from infrastructure.graph_class import graph
from infrastructure.input_loader import load_input
import time
import os, sys



def get_num(data):
    return int(data.split("-")[0])

E_arr=[]
runtime_arr=[]
V_arr=[]

dir = os.listdir("input_ET_ILP")

sorted_dir=sorted(dir, key=get_num)
for file in sorted_dir:
    
    V, E_num, E = load_input(dir,file)

    this_is_a_graph = graph(E_num,V,E)

    start = time.time()
     
    removedV=ILP(this_is_a_graph.vertices)
     
    runtime=(time.time()-start)
    
    E_arr.append(E_num)
    runtime_arr.append(runtime)
    V_arr.append(V)
    
    print(f"""
          Problém-ILP V:{V}, E:{E_num}
          Doba běhu: {runtime},
          ID oddělaných hran: {removedV}
          """)
    
print(E_arr)
print()
print(runtime_arr)
    
    
#