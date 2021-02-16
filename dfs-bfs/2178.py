# BFS를 사용해야 하나봐

import sys

n, m = map(int, sys.stdin.readline().split())
miro = []
q = [(0, 0)]

for i in range(n):
    t = list(map(int, sys.stdin.readline()[:-1]))
    miro.append(t)

def navi(graph):
    
    num = 1
    while q:
        t = q.pop(0)
        temp = [(t[0]+1, t[1]), (t[0]-1, t[1]), (t[0], t[1]+1), (t[0], t[1]-1)]
        for i in temp:
            if 0<=i[0]<n and 0<=i[1]<m and graph[i[0]][i[1]] == 1:
                q.append((i[0], i[1]))
                graph[i[0]][i[1]] = graph[t[0]][t[1]] + 1

navi(miro)
print(miro[n-1][m-1])
