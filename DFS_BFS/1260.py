import sys
sys.setrecursionlimit(99999)

n, e, s = map(int, sys.stdin.readline().split())
b = [0 for i in range(n)]
dfs = []
bfs = []
q = []

graph = [[0 for i in range(n)] for i in range(n)]       # n x n
graph2 = [[0 for i in range(n)] for i in range(n)]

for i in range(e):      # make graph
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1 - 1][n2 - 1] = 1
    graph[n2-1][n1-1] = 1

    graph2[n1 - 1][n2 - 1] = 1
    graph2[n2-1][n1-1] = 1

def DFS(g, s):
    if s not in dfs:
        dfs.append(s)   # real number
    for i in range(n):      
        if g[s-1][i] == 1:
            g[s-1][i] = 2
            g[i][s-1] = 2
            if (i+1) not in dfs:
                DFS(g, i+1)

def BFS(g, s):
    if s not in bfs:
        bfs.append(s)
    
    for i in range(n):
        if g[s-1][i] == 1:
            g[s-1][i] = 2
            g[i][s-1] = 2
            if (i+1) not in q:
                q.append(i+1)
            if (i+1) not in bfs:
                bfs.append(i+1)
    
    while q:
        temp = q.pop(0)
        BFS(g, temp)

DFS(graph, s)
BFS(graph2, s)
print(' '.join(map(str, dfs)))
print(' '.join(map(str, bfs)))
