import sys

a = []

xy = []
bangmon = []
h = []
num = int(sys.stdin.readline())

for i in range(num):
    a.append(sys.stdin.readline()[:-1])

for i in range(num):
    b = []
    for j in range(num):
        b.append(0)

    bangmon.append(b)
    
def dfs(x, y):
    #print(x, y)
    hnum = 0
    if 0<=x<num and 0<=y<num and a[x][y] == '1' and bangmon[x][y] == 0:
        hnum += 1
        bangmon[x][y] = 1
        hnum += dfs(x, y-1)
        hnum += dfs(x, y+1)
        hnum += dfs(x-1, y)
        hnum += dfs(x+1, y)
    
    return hnum

        

for i in range(num):
    for j in range(num):
        if a[i][j] == '1' and bangmon[i][j] == 0:
            k = dfs(i, j)
            h.append(k)

print(len(h))
h.sort()
for i in h:
    print(i)
        