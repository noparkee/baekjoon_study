import sys
from collections import deque

def findpath(graph, s, f, l):
    q = deque()
    q.append(s)
    while q:
        t = q.popleft()
        r = t[0]
        c = t[1]
        if r == f[0] and c == f[1]:
            return graph[f[0]][f[1]]

        lst = [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]
        for i in lst:
            if 0<=i[0]<l and 0<=i[1]<l:     # index range
                if graph[i[0]][i[1]] == 0:
                    graph[i[0]][i[1]] = graph[r][c] + 1
                    q.append([i[0], i[1]])

    return graph[f[0]][f[1]]



ans = []
num = int(input())

for i in range(num):
    l = int(input())
    chess = [[0 for _ in range(l)] for _ in range(l)]
    p = []
    for i in range(2):
        p.append(list(map(int, sys.stdin.readline().split())))
    
    if p[0] == p[1]:
        ans.append(0)
    else:
        ans.append(findpath(chess, p[0], p[1], l))

for i in ans:
    print(i)
    