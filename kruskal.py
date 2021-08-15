from biblioteca_grafo import Grafo

def kruskal(grafo):

    arvore = []
    s = [0]

    for i in range(1, grafo.qtdVertices() + 1):
        lista = [i]
        s.append(lista)
    pesos_ordenados = sorted(grafo.pesos.items(), key=lambda x: x[1])
    arestas_ord = []
    for elem in pesos_ordenados:
        arestas_ord.append(elem[0])
    
    for aresta in arestas_ord:
        u = aresta[0]
        v = aresta[1]
        su = s[u]
        sv = s[v]
        if su != sv:
            arvore.append(aresta)
            x = []
            x = su + sv
            for y in x:
                s[y] = x
    custo = 0
    for aresta in arvore:
        custo += grafo.peso(aresta[0], aresta[1])
    print(custo)
    print(arvore)

grafo_teste = Grafo("teste_kruskal.txt")

kruskal(grafo_teste)

