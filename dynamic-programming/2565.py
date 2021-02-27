import sys

n = int(input())
e = []
eb = []
len = [0 for _ in range(n)]
for i in range(n):
    e.append(list(map(int, sys.stdin.readline().split())))

e = sorted(e)

for i in range(n):
    eb.append(e[i][1])

for i in range(n):
    for j in range(i):
        if eb[i] > eb[j]:
            len[i] = max(len[i], len[j]+1)

print(n - max(len) - 1)
