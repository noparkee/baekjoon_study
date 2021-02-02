import sys

num = int(sys.stdin.readline())
s = []
for i in range(num):
    temp = []
    for j in range(num):
        temp.append(' ')
    s.append(temp)

def star(num, x, y):
    if num == 1:
        s[y][x] = '*'
    else:
        num = num//3
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    star(num, x + i*num, y + j*num)

star(num, 0, 0)

for i in range(num):
    print(''.join(s[i]))

### 다시 해보기