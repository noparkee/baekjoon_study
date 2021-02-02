import sys

num = int(sys.stdin.readline())
h = []
def hanoi(num, a, b, c):        # num개를 a에서 c로
    if num == 1:
        h.append((a, c))
        
    else:
        hanoi(num-1, a, c, b)
        h.append((a, c))     # 마지막 원판을 오른쪽으로
        hanoi(num-1, b, a, c)
        
hanoi(num, 1, 2, 3)

print(len(h))
for i in h:
    print(i[0], i[1])

### 다시