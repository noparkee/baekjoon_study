import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
# m = max(n, k)
z = [0 for i in range(k*2+1)]
q = deque()

def soom(z):
    while q:
        s = q.popleft()
        lst = [s-1, s+1, 2*s]     
        for i in lst:
            if (2*k+1> i >= 0 and 2*k+1 > s >=0) and (z[i] == 0 or z[i] > z[s]):
                z[i] = z[s] + 1
                q.append(i)

            
    
if k > n:
    z[n] = 1
    q.append(n)
    soom(z)
    print(z[k]-1)
    
else:
    print(n-k)
