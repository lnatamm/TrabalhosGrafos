# TrabalhosGrafos
Repositório para os trabalhos finais da disciplina de Grafos

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