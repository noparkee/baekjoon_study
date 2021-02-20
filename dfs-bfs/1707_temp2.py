import sys
from collections import deque

# visited는 edge 정보
def bipartite(e, v, visited):       
    for i in range(len(visited)):
        if visited[i] == 0:
            s = e[i][0]
            break

    q = deque()
    
    flag = 1
    q.append(s)
    v[s] = flag

    while q:
        t = q.popleft()     
        for i in range(len(visited)):
            if e[i][0] == t and visited[i] == 0:
                if v[e[i][1]] == 0:
                    q.append(e[i][1])
                    v[e[i][1]] = v[t] * (-1)
                    visited[i] = 1
                elif v[e[i][1]] == v[t]:
                    return "NO"
            elif e[i][1] == t and visited[i] == 0:
                if v[e[i][0]] == 0:
                    q.append(e[i][0])
                    v[e[i][0]] = v[t] * (-1)
                    visited[i] = 1
                elif v[e[i][0]] == v[t]:
                    return "NO"
    
    if 0 in visited:
        return (bipartite(e, v, visited))
    elif 0 not in v:
        return "YES"
    else:
        return "YES"



ans = []
num = int(sys.stdin.readline())

for i in range(num):
    v, e = map(int, (sys.stdin.readline().split()))
    vertex = [0 for _ in range(v)]
    edges = []
    visited = []

    for j in range(e):
        n, m = (map(int, sys.stdin.readline().split()))
        visited.append(0)
        edges.append([n-1, m-1])
    

    ans.append(bipartite(edges, vertex, visited))
    
for i in ans:
    print(i)