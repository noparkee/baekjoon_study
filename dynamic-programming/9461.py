import sys

def findLength(n, array):
    if n <= 4:
        return array[n-1]
    
    if array[n-1] != 0:
        return array[n-1]
    
    array[n-1] = findLength(n-2, array) + findLength(n-3, array)
    return array[n-1]



l = [0 for _ in range(100)]
l[0] = 1
l[1] = 1
l[2] = 1
l[3] = 2
l[4] = 2
t = int(sys.stdin.readline()[:-1])
for i in range(t):
    n = int(sys.stdin.readline()[:-1])
    print(findLength(n, l))
    