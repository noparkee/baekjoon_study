import sys

n, m = map(int, sys.stdin.readline().split())
miro = []

for i in range(n):
    t = list(sys.stdin.readline()[:-1])
    miro.append(t)

def explore(r, c):
    temp = 0
    temp_lst = []
    if r == n and c == m:
        return 1, 1

    elif 0<r<=n and 0<r<=m and miro[r-1][c-1] == '1':
        temp += 1
        miro[r-1][c-1] = '2'
        
        rc, num = explore(r+1, c)
        if rc == 1:
            temp_lst.append(temp+num)
        
        rc, num = explore(r-1, c)
        if rc == 1:
            temp_lst.append(temp+num)

        rc, num = explore(r, c+1)
        if rc == 1:
            temp_lst.append(temp+num)

        rc, num = explore(r, c-1)
        if rc == 1:
            temp_lst.append(temp+num)

        if len(temp_lst) == 0:
            return 0, 0

        temp += min(temp_lst)

    return 1, temp

print(explore(1, 1))
