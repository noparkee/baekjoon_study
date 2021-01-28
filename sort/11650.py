num = int(input())
a = []
for i in range (num):
    str = input()
    str = str.split()
    a.append((int(str[0]), int(str[1])))

a.sort()

for i in range(num):
    print(a[i][0], a[i][1])

# 4, 5번 줄
# >> x, y = map(int, str.split())