from itertools import combinations

h = []
for i in range(9):
    h.append(int(input()))

for i in list(combinations(h, 7)):
    if sum(i) == 100:
        ans = sorted(i)
        break

for k in ans:
    print(k)
    