from algorithms.edge_brute_force import edge_brute_force

from infrastructure.graph_class import graph
from infrastructure.input_loader import load_input
import time
import os, sys



def get_num(data):
    return int(data.split("-")[0])

E_arr=[]
runtime_arr=[]
V_arr=[]

dir_name="inputs/input_ET_BF"

dir = os.listdir(dir_name)

sorted_dir=sorted(dir, key=get_num)
for file in sorted_dir:
    
    V, E_num, E = load_input(dir_name,file)

    this_is_a_graph = graph(E_num,V,E)

    start = time.time()
     
    removedV=edge_brute_force(this_is_a_graph) 
    runtime=(time.time()-start)
    
    
    E_arr.append(E_num)
    runtime_arr.append(runtime)
    V_arr.append(V)
    
    print(f"""
          Problém-BF V:{V}, E:{E_num}
          Doba běhu: {runtime},
          ID oddělaných Vrcholů: {removedV}
          """)
    if runtime>=20:
        break
    
print(E_arr)
print()
print(V_arr)
print()
print(runtime_arr)
    