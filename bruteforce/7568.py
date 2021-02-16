import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

r = ""
for i in a:
    cnt = 1
    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    r = r + str(cnt) + " "

print(r)