# TrabalhosGrafos
Repositório para os trabalhos finais da disciplina de Grafos

## Pré requisitos
Para rodar o código do trabalho de Seleção de Projetos você vai da biblioteca [ortools](https://developers.google.com/optimization/install) instalada.

## Running

### AV3_1 - Problema de Redirecionamento de Conexões
Abra a pasta "AV3_1", altere o conteúdo do arquivo adjMatrix.txt da seguinte maneira

<pre>
𝑛, o número de vértices do grafo
i j, os vértices de início e fim onde queremos realizar a comunicação
A matriz de adjacência do grafo, os vértices são 0-indexados
</pre>

No exemplo padrão do adjMatrix.txt temos:
<pre>
5
1 4
0 0 0 0 0
4 0 0 0 0
0 10 0 0 0
5000 0 8 0 0
22 50 0 3 0

5 vértices
i = 1
j = 4

Vértice 0: Não se conecta a ninguém
Vértice 1: Se conecta ao vértice 0 com custo 4
Vértice 2: Se conecta ao vértice 1 com custo 10
Vértice 3: Se conecta ao vértice 0 com custo 5000 e ao vértice 2 com custo 8
Vértice 4: Se conecta ao vértice 0 com custo 22, ao vértice 1 com custo 50 e ao vértice 3 com custo 3
</pre>

Por fim, execute o comando:

    py AV3_1.py

### AV3_2 - Problema de Seleção de Projetos

Abra a pasta "AV3_2", altere o conteúdo do arquivo project.txt da seguinte maneira
<pre>
𝑛, o número de vértices do grafo
A matriz de adjacência do grafo, os vértices são 1-indexados
𝙘1 𝙘2 𝙘3… 𝙘n, os custos dos projetos
</pre>

No exemplo padrão do project.txt temos:

<pre>
8
0 0 0 0 1 1 0 0
0 0 1 0 0 1 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
4 6 2 3 -2 -3 -5 -8

8 vértices (projetos)
Vértice 1: Tem como depêndencia os vértices 5 e 6
Vértice 2: Tem como depêndencia os vértices 3 e 6
Vértice 3: Tem como depêndencia o vértice 7
Vértice 4: Tem como depêndencia os vértices 7 e 8
Vértice 5: Não possui nenhuma depêndencia
Vértice 6: Tem como depêndencia o vértice 5
Vértice 7: Não possui nenhuma depêndencia
Vértice 8: Não possui nenhuma depêndencia

Custos dos projetos:
Vértice 1: Tem custo 4
Vértice 2: Tem custo 6 
Vértice 3: Tem custo 2
Vértice 4: Tem custo 3
Vértice 5: Tem custo -2
Vértice 6: Tem custo -3
Vértice 7: Tem custo -5
Vértice 8: Tem custo -8
</pre>

Por fim, execute o comando:

    py AV3_2.py