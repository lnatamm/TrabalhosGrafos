import os

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
    i = line[0]
    j = line[0]
    G = []
    for i in range(n):
        G.append([])
        line = file.readline().split()
        for j in range(n):
            G[i].append(float(line[j]))
    return G