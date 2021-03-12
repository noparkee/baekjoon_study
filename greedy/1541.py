s = input().split('-')

ans = 0
flag = 0
for i in s:
    temp = i.split('+')
    temp = map(int, temp)

    if ans == 0 and flag == 0:
        ans = sum(temp)
        flag = 1
    else:
        ans -= sum(temp)

print(ans)
