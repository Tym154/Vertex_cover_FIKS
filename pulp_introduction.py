import pulp



#pulp_edges=[]
G= {1:[2,3, 4],
        2:[1,3, 4],
        3:[1,4, 2],
        4:[1,2]
}

def ILP(G):
    P = pulp.LpProblem("Vertex_cover_ILP", pulp.LpMinimize)
    X = {v: pulp.LpVariable(f'x_{v}', lowBound=0, cat='Integer') for v in G}
    for v, E in G.items():
        P += X[v]<=1
        for u in E:
            
            P += X[v] + X[u] >=1

    P+= sum(X.values())
            
            
            
    P.solve()
    print(P)
    print(pulp.LpStatus[P.status])
    print(pulp.value(P.objective))
    for variable in P.variables():
        print(f"{variable.name} = {variable.varValue}")
        
