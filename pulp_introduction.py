import pulp

P = pulp.LpProblem("Vertex_cover_ILP", pulp.LpMinimize)

#pulp_edges=[]
nodes= {1:[2,3, 4],
        2:[1,3, 4],
        3:[1,4, 2],
        4:[1,2]
}

X = {v: pulp.LpVariable(f'x_{v}', lowBound=0, cat='Integer') for v in nodes}
for v, E in nodes.items():
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
    
    

