import sys

n = int(sys.stdin.readline()[:-1])
b = [(-1) for _ in range(1000000)]
b[0] = 1
b[1] = 2

if n > 2: # n > 2 (3, 4, 5, ...)
    for i in range(2, n):
        b[i] = (b[i-1] + b[i-2]) % 15746

print(b[n-1])

# 메모리 주의