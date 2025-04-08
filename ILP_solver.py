import pulp




def ILP(G):

    P = pulp.LpProblem("Vertex_cover_ILP", pulp.LpMinimize)
    X = {v: pulp.LpVariable(f'x_{v}', lowBound=0, cat='Integer') for v in G}
    for v, E in G.items():
        P += X[v]<=1
        for u in E:
            
            P += X[v] + X[u] >=1

    P+= sum(X.values())
            
            
            
    P.solve(pulp.PULP_CBC_CMD(msg=False))

    removedV=[ int((variable.name)[2:]) for variable in P.variables() if variable.varValue==1]
    return  removedV
        
