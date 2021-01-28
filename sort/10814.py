import sys

num = int(sys.stdin.readline())
a=[]
for i in range(num):
    str=input()
    c = str.split()
    a.append((int(c[0]), c[1]))

a.sort(key=lambda x: x[0])

for i in a:
    print(i[0], i[1])

# sys.stdin.readline()