import sys

str = sys.stdin.readline().split()
cardnum = int(str[0])
limit = int(str[1])
max = 0

card = list(map(int, sys.stdin.readline().split()))

for i in range(cardnum):
    for j in range(i+1, cardnum):
        for k in range(j+1, cardnum):
            sum = card[i] + card[j] + card[k]
            if sum > max and sum <= limit:
                max = sum

print(max)