import sys

w = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]        # 0 ~ 20
def funW(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return funW(20, 20, 20)
    
    if w[a][b][c] != 0:
        return w[a][b][c]

    if a < b < c:
        w[a][b][c] = funW(a, b, c-1) + funW(a, b-1, c-1) - funW(a, b-1, c)
    
    else:
        w[a][b][c] = funW(a-1, b, c) + funW(a-1, b-1, c) + funW(a-1, b, c-1) - funW(a-1, b-1, c-1)
    
    return w[a][b][c]
    


while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    
    res = funW(a, b, c)
    print('w(%d, %d, %d) = %d' %(a, b, c, res))
