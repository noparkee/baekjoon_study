from itertools import permutations
n = int(input())
lst = [i+1 for i in range(n)]

temp = list(permutations(lst))
for i in temp:
    for j in i:
        print(j, end=' ')
    print('\n', end='')
    