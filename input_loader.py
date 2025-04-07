import sys

""" Načíta input, žádnej error handeling, musí se dát správný input
aby fungoval správně, sry skillissue"""

def load_input():
    input=sys.stdin.readlines()

    V=0
    E_num=0
    E=[]

    for line in input:
        if line[0]=="p":
            ls1="".join(c for c in line if  c.isdecimal())
            V=int(ls1[0])
            E_num=int(ls1[1])
        elif line[0]!="c":
            ls2=line.strip().replace(" ","")
            #print(ls2)
            E.append([int(ls2[0]), int(ls2[1])])
    return V, E_num, E

print(load_input())