# -*- coding: UTF-8 -*-
from biblioteca_grafo import Grafo

def ordem_topologica(grafo):
    c = [False] * (grafo.qtdVertices()+1)
    ordem_T = []
    for i in range(grafo.qtdVertices()+1):
        if c[i] == False:
            c, ordem_T = dfs_Visit_OT(grafo,i,c,ordem_T)
    
    new_ordem_T = []
    ordem_T.pop()
    ordem_T = [int(x-1) for x in ordem_T]
    for k in ordem_T:
        new_ordem_T.append(grafo.rotulo(k))
    
    for x in range(len(new_ordem_T)):
        new_ordem_T[x] = (' '.join(new_ordem_T[x]))
    
    print(" -> ".join(new_ordem_T))

def dfs_Visit_OT(grafo,i,c,ordem_T):
    c[i] = True
    vizinhos = grafo.vizinhos(i)
    for j in vizinhos:
        if c[j] == False:
            c, ordem_T = dfs_Visit_OT(grafo,j,c,ordem_T)
    
    ordem_T.insert(0,i)
    return (c,ordem_T)

grafo1 = Grafo("teste3.txt")
ordem_topologica(grafo1)
