import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())       # column, row, heignt
box = []

for i in range(h):
    temp = []
    for j in range(n):      # row
        t = list(map(int, sys.stdin.readline()[:-1].split()))
        temp.append(t)
    box.append(temp)

# box[i][j][k] height, row, columns

def oldtomato(graph):
    for i in range(h):
        for j in range(n):
            if 0 in graph[i][j]:
                return False
    
    return True

def checktomato(graph):
    start = deque()
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    start.append((i, j, k))
    
    q.append(start)

    while q:
        ws = q.popleft()
        while ws:
            s = ws.popleft()
            temp = [(s[0]-1, s[1], s[2]), (s[0], s[1]-1, s[2]), (s[0], s[1], s[2]-1), (s[0]+1, s[1], s[2]), (s[0], s[1]+1, s[2]), (s[0], s[1], s[2]+1)]
            temp_q = deque()
            for i in temp:
                if 0<=i[0]<h and 0<=i[1]<n and 0<=i[2]<m and graph[i[0]][i[1]][i[2]]==0:
                    temp_q.append((i[0], i[1], i[2]))
                    graph[i[0]][i[1]][i[2]] = graph[s[0]][s[1]][s[2]] + 1
            
            q.append(temp_q)

if oldtomato(box):
    print(0)
else:
    checktomato(box)
    if oldtomato(box) == False:
        print(-1)
    else:
        max_lst = []
        for i in range(h):
            for j in range(n):
                max_lst.append(max(box[i][j]))

        print(max(max_lst)-1)
        