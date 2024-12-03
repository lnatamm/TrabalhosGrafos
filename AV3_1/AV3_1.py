import os

INF = 999999

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.split()
    variable = int(variable[0])
    return variable

#Lê a matriz de adjacência do arquivo "adjMatrix.txt"
def readFile():
    filePath = os.getcwd() + "\\AV3_1\\adjMatrix.txt"
    file = open(filePath)
    n = file.readline()
    n = removeLineBreak(n)
    line = file.readline().split()
    s = int(line[0])
    t = int(line[1])
    G = []
    for i in range(n):
        G.append([])
        line = file.readline().split()
        for j in range(n):
            G[i].append(float(line[j]))
    return G, s, t

#Inicializa a primeira matriz de adjacência
def DefineMatrix(G):
    n = len(G)
    M = []
    for u in range(n):
        M.append(([0]*n).copy())
        for v in range(n):
            if(G[u][v] > 0):
                M[u][v] = 1
    return M


#Inicializa os arrays d e 𝑃i
def InitializeSingleSource(G, s):
    n = len(G)
    d = [INF]*n
    Pi = [-1]*n
    d[s] = 0
    return d, Pi

#Método que permite a soma de 2 números funcione caso um deles seja infinito
def Sum(x, y):
    if(x == INF or y == INF):
        return INF
    return x + y

#Relaxa a aresta, atualizando a distância do vértice v para a fonte e alterando seu predescessor caso encontre um mais curto
def Relax(d, Pi, u, v, G):
    #Se a distância atual de v para a fonte for maior que a soma entre a distância de u para a fonte com a aresta u,v
    if(d[v] > Sum(d[u], G[u][v])):
        d[v] = Sum(d[u], G[u][v])
        Pi[v] = u
    return d, Pi

#Retorna o array das distâncias de cada vértice e a lista de predecessores do caminho mínimo de G partindo de s
def BellmanFord(G, M, s, t):
    n = len(G)
    d, Pi = InitializeSingleSource(G, s)
    #O algoritmo de Bellman-Ford necessita ser realizado N-1 vezes
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if(M[u][v] == 1):
                    #Relaxamos cada aresta do grafo
                    d, Pi = Relax(d, Pi, u, v, G)
    return d[t], Pi

#Retorna o caminho de s a t basedo na lista de predecessores
def GetPath(Pi, s, t):
    current = t
    path = [current]
    while current != s:
        path.append(Pi[current])
        current = Pi[current]
    return path

#Copia o conteúdo do grafo G
def Copy(G):
    n = len(G)
    Gi = []
    for u in range(n):
        line = G[u].copy()
        Gi.append(line)
    return Gi

#Retorna um novo grafo e matriz de adjacência não orientado (bilateral) onde todas as arestas originais tem peso 0 e as contrárias tem o da original
def TwoWayConnections(G, M):
    n = len(G)
    #Grafo de retorno
    Gi = Copy(G)
    #Matriz de adjacência de retorno
    Mi = Copy(M)
    #Lista das arestas que foram invertidas
    edges = []
    for u in range(n):
        for v in range(n):
            if(M[u][v] == 1):
                #Verifica se existe aresta voltando
                if(Mi[v][u] == 0):
                    Gi[v][u] = Gi[u][v]
                    Mi[v][u] = 1
                    edges.append([u, v])
                Gi[u][v] = 0
    return Gi, Mi, edges

#Retorna todas as arestas que foram invertidas que estão no caminho mínimo gerado pelo Bellman Ford
def GetEdges(path, edges):
    invertedEdges = []
    for i in range(len(path) - 1):
        if([path[i], path[i+1]] in edges):
            invertedEdges.append([path[i], path[i+1]])
    return invertedEdges

#Pegamos os dados do arquivo
G, s, t = readFile()
#Definimos a matriz de adjacência
M = DefineMatrix(G)
#Pegamos o novo grafo não direcionado (bilateral) e as arestas que foram invertidas
Gi, Mi, edges = TwoWayConnections(G, M)
#Executamos o Bellman Ford no grafo não direcionado. Como o peso das arestas originais agora é 0 o Bellman Ford já retorna a soma das arestas invertidas usadas
edgesSum, Pi = BellmanFord(Gi, Mi, s, t)
print(f"Soma das arestas a serem invertidas: {edgesSum}")
print(f"Arestas a serem invertidas: {GetEdges(GetPath(Pi, s, t), edges)}")