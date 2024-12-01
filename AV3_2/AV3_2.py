from ortools.linear_solver import pywraplp
import os

#Remove o caractere de quebra de linha
def removeLineBreak(variable):
    variable = variable.rstrip()
    return variable

#Lê o arquivo "project.txt"
def readFile():
    filePath = os.getcwd() + "\\AV3_2\\project.txt"
    file = open(filePath)
    n = file.readline()
    n = int(removeLineBreak(n))
    G = []
    c = []
    for i in range(n):
        G.append([])
        line = file.readline().split()
        for j in range(n):
            G[i].append(float(line[j]))
    cString = file.readline().split()
    for string in cString:
        c.append(int(string))
    return G, c

def readAllFile():
    filePath = os.getcwd() + "\\AV3_2\\project.txt"
    file = open(filePath)
    return file.readlines()

def printFile():
    file = readAllFile()
    for line in file:
        line = removeLineBreak(line)
        print(line)

def hasCycle(G):
    n = len(G)
    visited = [False]*n
    stack = [False]*n

    def cycleAux(u):
        visited[u] = True
        stack[u] = True
        for v in range(len(G[u])):
            if(G[u][v] == 1):
                if(not visited[v]):
                    if(cycleAux(v)):
                        return True
                elif stack[v]:
                    return True
        stack[u] = False
        return False

    for u in range(n):
        if not visited[u]:
            if cycleAux(u):
                return True
    return False

def selectProjects(G, c):
    n = len(G)
    if(hasCycle(G)):
        return False
    else:
        #Cria um solver utilizando o "SCIP" para problemas de otimização inteiros
        solver = pywraplp.Solver.CreateSolver("SCIP")
        if(not solver):
            return None
        # Definição de Variáveis
        vars = []
        for i in range(n):
            vars.append(solver.IntVar(0, 1, f"x{i+1}"))
        #Função Objetivo de maximização
        solver.Maximize(solver.Sum(c[i]*vars[i] for i in range(len(c))))
        #Condições
        for i in range(n):
            for j in range(n):
                if(G[i][j] == 1):
                    solver.Add(vars[i] <= vars[j])
        viable = solver.Solve()
        if(viable == pywraplp. Solver.OPTIMAL):
            projects = []
            for var in vars:
                if(var.solution_value() == 1):
                    projects.append(f"{var}")
            return projects
        else:
            return "Solução Inviável"

G, c = readFile()
print("========================================")
print("ENTRADA")
printFile()
print()
print("SAÍDA")
projects = selectProjects(G, c)
print(f"x  = {projects}") if projects != False else print("Erro: DÍGRAFO INVÁLIDO")
print("========================================")