import sys

n = int(input())
d = []

for i in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

d = sorted(d, key = lambda x: [x[1], x[0]])

f = 0
num = 0

for i in d:
    if i[0] >= f:
        num += 1
        f = i[1]

print(num)