import sys
n = int(sys.stdin.readline())

for i in range(n+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s==n:
        print(i)
        break

if i==n:
    print(0)
