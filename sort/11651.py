num = int(input())
a = []
for i in range (num):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda x:(x[1], x[0]))

for i in range(num):
    print(a[i][0], a[i][1])
