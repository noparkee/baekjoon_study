import sys

def bipartite(adj, v):
    flag = 1

    for i in adj:
        
        if len(i) != 0:
            if v[i[0][0]] == 0:
                v[i[0][0]] = flag
            elif v[i[0][0]] != 0:
                flag = v[i[0][0]]
        
            flag *= (-1)

            for j in i:
                if v[j[1]] == 0:
                    v[j[1]] = flag
                elif v[j[1]] != flag:
                    return "NO"
        
        flag *= (-1)
    
    return "YES"    
    


ans = []
num = int(input())

for i in range(num):
    v, e = map(int, (input().split()))
    vertex = [0 for _ in range(v)]
    edges = []    
    adj = [[] for _ in range(v - 1)]

    for j in range(e):
        n, m = (map(int, sys.stdin.readline().split()))
        if n > m:
            edges.append([m-1, n-1])
        else:
            edges.append([n-1, m-1])
    
    edges.sort()
    for i in edges:
        adj[i[0]].append(i)    
    
    print(adj)
    input()

    ans.append(bipartite(adj, vertex))

for i in ans:
    print(i)