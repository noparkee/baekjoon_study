import sys
from itertools import combinations

str = sys.stdin.readline().split()
cardnum = int(str[0])
limit = int(str[1])
max = 0

card = list(map(int, sys.stdin.readline().split()))

a = list(combinations(card, 3))

for i in a:
    sum = i[0] + i[1] + i[2]
    if sum > max and sum <= limit:
        max = sum

print(max)