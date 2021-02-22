import sys

n = int(input())

tri = []
ans = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    tri.append(temp)
    #tri.extend(temp)
    ans.append([0 for _ in range(len(temp))])
# ans = [0 for _ in range(len(tri))]

ans[0][0] = tri[0][0]

for i in range(n-1):
    for j in range(len(tri[i])):
        for k in range(2):
            temp = ans[i][j] + tri[i+1][j+k]
            if ans[i+1][j+k] < temp:
                ans[i+1][j+k] = temp

print(max(ans[n-1]))
