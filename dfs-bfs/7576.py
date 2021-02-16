import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())       # column, row
box = []

for i in range(n):
    t = list(map(int, sys.stdin.readline()[:-1].split()))
    box.append(t)

def alloldtomato(graph):
    for i in graph:
        if 0 in i:
            return False
    
    return True

def checktomato(graph):
    #start = []
    start = deque()
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                start.append((i, j))        # 시작점
    
    q.append(start)
    
    while q:
        ws = q.popleft()
        while ws:
            s = ws.popleft()
            temp = [(s[0], s[1]-1), (s[0]-1, s[1]), (s[0]+1, s[1]), (s[0], s[1]+1)]
            # temp_q = []
            temp_q = deque()
            for i in temp:
                if 0<=i[0]<n and 0<=i[1]<m and graph[i[0]][i[1]] == 0:
                    temp_q.append((i[0], i[1]))
                    graph[i[0]][i[1]] = graph[s[0]][s[1]] + 1 
            
            q.append(temp_q)



if alloldtomato(box):
    print(0)
else:
    checktomato(box)
    if alloldtomato(box) == False:
        print(-1)
    else:
        a = max(map(max, box))
        print(a-1)

# list 보다 deque가 더 빠르다!