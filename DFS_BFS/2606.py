import sys

num = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
graph = [[0 for i in range(num)] for i in range(num)]

v = [0 for i in range(num)]

for i in range(edge):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1-1][n2-1] = 1
    graph[n2-1][n1-1] = 1

def DFS(node):
    v[node-1] = 1

    for i in range(num):
        if graph[node-1][i] == 1:
            graph[node-1][i] = 2
            graph[i][node-1] = 2
            DFS(i+1)

DFS(1)

sum = 0
for i in range(1, num):
    if v[i] == 1:
        sum += 1

print(sum)
