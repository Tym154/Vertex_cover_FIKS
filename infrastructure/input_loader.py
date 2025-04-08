import sys

""" Načíta input, žádnej error handeling, musí se dát správný input
aby fungoval správně, sry skillissue"""

def load_input(dir="input",file=None,):
    if file!=None:
        with open(f"{dir}/{file}","r") as f:
        
            input= f.readlines()
    else:
        input=sys.stdin.readlines()

    V=0
    E_num=0
    E=[]

    for line in input:
        if line[0]=="p":
            _, _, V, E_num=line.split(" ")
            V=int(V)
            E_num=int(E_num)
        elif line[0]!="c":
            u,v=line.split(" ")
            E.append([int(u), int(v)])
    
    return V, E_num, E

