import sys
from collections import deque

def findpath(graph, visited):
    while q:
        s = q.popleft()
        z = s[0]
        r = s[1]
        c = s[2]
        
        lst = [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]
        
        
        for i in lst:            
            if 0<=i[0]<n and 0<=i[1]<m:     # index range
                if graph[i[0]][i[1]] == 0 and visited[z][i[0]][i[1]] == 0:
                    visited[z][i[0]][i[1]] = visited[z][r][c] + 1
                    q.append((z, i[0], i[1]))
                if z == 0 and graph[i[0]][i[1]] == 1:       # break
                    visited[1][i[0]][i[1]] = visited[z][r][c] + 1
                    q.append((1, i[0], i[1]))



n, m = map(int, sys.stdin.readline().split())
wall = []
q = deque()

for i in range(n):
    temp = list(map(int, sys.stdin.readline()[:-1]))
    wall.append(temp)

visited = [[[0 for _ in range(m)] for _ in range(n)], [[0 for _ in range(m)] for _ in range(n)]]

q.append((0, 0, 0))     # depth, row, column
findpath(wall, visited)

if n == 1 and m == 1:
    print(1)
else:
    if visited[0][n-1][m-1] == 0 and visited[1][n-1][m-1] == 0:
        print(-1)
    elif visited[0][n-1][m-1] != 0 and visited[1][n-1][m-1] == 0:
        print(visited[0][n-1][m-1] + 1)
    elif visited[0][n-1][m-1] == 0 and visited[1][n-1][m-1] != 0:
        print(visited[1][n-1][m-1] + 1)
    else:
        print(min(visited[0][n-1][m-1], visited[1][n-1][m-1]) + 1)
