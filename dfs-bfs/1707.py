import sys
from collections import deque

def bipartite(adj, v, visited):
    q = deque()
    flag = 1
    for i in range(len(adj)):
        if len(adj[i]) != 0 and visited[i] == 0:
            v[i] = flag
            q.append(i)
            visited[i] = 1
            break

    while q:
        s = q.popleft()
        for i in adj[s]:
            if v[i] == 0 and visited[i] == 0:
                v[i] = v[s] * (-1)
                q.append(i)
                visited[i] = 1
            elif v[i] == v[s]:
                return "NO"

    if 0 in visited:
        return bipartite(adj, v, visited)
    else:
        return "YES"



ans = []
num = int(sys.stdin.readline())

for i in range(num):
    v, e = map(int, (sys.stdin.readline().split()))
    vertex = [0 for _ in range(v)]
    edges = []
        
    adj = [[] for _ in range(v)]
    visited = [(-1) for _ in range(v)]

    for j in range(e):
        n, m = (map(int, sys.stdin.readline().split()))
        adj[n-1].append(m-1)
        adj[m-1].append(n-1)
        visited[n-1] = 0
        visited[m-1] = 0

    
    ans.append(bipartite(adj, vertex, visited))
    
for i in ans:
    print(i)
    