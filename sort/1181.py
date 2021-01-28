num = int(input())
a = []
for i in range(num):
    str = input()
    a.append((len(str), str))

a = list(set(a))
a.sort(key=lambda x:(x[0], x[1]))

for i in a:
    print(i[1])