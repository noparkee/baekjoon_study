n, k = map(int, input().split())
lst = []
num = 0
for i in range(n):
    t = int(input())
    if t <= k:
        lst.append(t)

lst.sort()

idx = len(lst) - 1
while k > 0:
    if k // lst[idx] != 0:
        num += k//lst[idx]
        k = k%lst[idx]
    else:
        idx -= 1

print(num)
