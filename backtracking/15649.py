import sys

n, m = (map(int, sys.stdin.readline().split()))
p = []
v = []
for i in range(n):
    v.append(0)

def permutation(m):
    if m == 0:
        for i in p:
            print(str(i) + ' ', end='')
        print('\n', end='')
        return 

    for i in range(n):
        if v[i] == 0 :
            v[i] = 1
            p.append(i+1)
            permutation(m-1)
            v[i] = 0
            p.pop()

if m == 1:
    for i in range(1, n+1):
        print(i)
else:
    permutation(m)



    
        
    
    

