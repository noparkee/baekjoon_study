import sys
sys.setrecursionlimit(99999)

test = int(sys.stdin.readline())
t = []

def howMany(x, y, g, m, n):
    temp = 0
    if 0<= x < m and 0<= y < n and g[x][y] == 1:
        temp += 1
        g[x][y] = 2
        temp += howMany(x+1, y, g, m, n)
        temp += howMany(x-1, y, g, m, n)
        temp += howMany(x, y+1, g, m, n)
        temp += howMany(x, y-1, g, m, n)
    
    return temp



for i in range(test):       
    sum = 0
    m, n, num = map(int, sys.stdin.readline().split())
    graph = [[0 for i in range(n)] for j in range(m)]
    for i in range(num):       
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1][n2] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                if howMany(i, j, graph, m, n) != 0:
                    sum += 1
    
    t.append(sum)

print(' '.join(map(str, t)))
    