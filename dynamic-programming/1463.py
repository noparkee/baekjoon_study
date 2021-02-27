import sys

n = int(input())
a = [-1 for _ in range(n)]
a[0] = 0

for i in range(1, n):
    a[i] = a[i-1] + 1
    if (i + 1)%3 == 0:
        temp = a[(i+1)//3 - 1] + 1
        if a[i] >  temp:
            a[i] = temp
    if (i+1)%2 == 0:
        temp = a[(i+1)//2 - 1] + 1
        if a[i] > temp:
            a[i] = temp    

print(a[n-1])
