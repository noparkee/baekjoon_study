import sys

zero = [(-1) for _ in range(41)]
one = [(-1) for _ in range(41)]


def findZero(a):
    if a == 0:
        return 1
    if a == 1:
        return 0
    if zero[a] != -1:
        return zero[a]
    
    zero[a] = findZero(a-1) + findZero(a-2)
    return zero[a]

def findOne(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if one[a] != -1:
        return one[a]
    
    one[a] = findOne(a-1) + findOne(a-2)
    return one[a]



t = int(sys.stdin.readline())

zero[0] = 1
zero[1] = 0

one[0] = 0
one[1] = 1

ans = []
for i in range(t):
    a = int(sys.stdin.readline())
    ans.append(a)
    findZero(a)
    findOne(a)

for i in ans:
    print(zero[i], one[i])
