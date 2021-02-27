import sys

n = int(sys.stdin.readline()[:-1])
arr = list(map(int, sys.stdin.readline().split()))
len = [[1 for _ in range(n)], [1 for _ in range(n)]]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            len[0][i] = max(len[0][i], len[0][j]+1)

arr.reverse()
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            len[1][i] = max(len[1][i], len[1][j]+1)

len[1].reverse()

ans = []
for i in range(n):
    ans.append(len[0][i] + len[1][i])

print(max(ans)-1)
