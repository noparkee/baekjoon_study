import sys

n = int(sys.stdin.readline()[:-1])
podo = [0 for _ in range(n)]
for i in range(n):
    podo[i] = int(sys.stdin.readline()[:-1])

yang = [[0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]]
yang[0][0] = podo[0]
yang[1][0] = podo[0]
yang[2][0] = podo[0]

if n >= 2:
    yang[0][1] = podo[1]
    yang[1][1] = podo[0] + podo[1]
    yang[2][1] = podo[0]
    for i in range(2, n):
        yang[1][i] = max(yang[0][i-1], yang[2][i-1]) + podo[i]
        yang[0][i] = max(yang[0][i-2], yang[1][i-2], yang[2][i-1]) + podo[i]
        yang[2][i] = max(yang[1][i], yang[0][i]) - podo[i]

print(max(yang[0] + yang[1]))

# 2579와 비슷! 단, 2579는 최대 하나만 건너 뛸 수 있는데 이 문제는 여러 개 건너 뛰어도 됨
'''
6
1000
1000
1
1
1000
1000
3001
'''