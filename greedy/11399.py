n = int(input())
sum = 0

lst = list(map(int, input().split()))
lst.sort()

for i in range(n):
    sum += (lst[i] * (n-i))

print(sum)
