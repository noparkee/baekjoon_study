from itertools import combinations

while 1:
    a = list(map(int, input().split()))
    k = a[0]
    if k == 0:
        break
    lst = a[1:]
    c = list(combinations(lst, 6))
    for i in c:
        for j in i:
            print(j, end=' ')
        print('\n', end='')
    
    print('\n', end='')
