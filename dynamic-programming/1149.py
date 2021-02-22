import sys

n = int(sys.stdin.readline()[:-1])
cost = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    cost.append(temp)

home =  [[0 for _ in range(3)] for _ in range(n)]
home[0] = cost[0]

for i in range(1, n):
    home[i][0] = min(home[i-1][1], home[i-1][2]) + cost[i][0]
    home[i][1] = min(home[i-1][0], home[i-1][2]) + cost[i][1]
    home[i][2] = min(home[i-1][0], home[i-1][1]) + cost[i][2]

print(min(home[n-1]))
