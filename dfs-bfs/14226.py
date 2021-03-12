from collections import deque

n = int(input())
emo = [[0 for _ in range(n+1)] for _ in range(n+1)]

q = deque()
q.append([1, 0])
emo[1][0] = 1

while q:
    screen, clip = q.popleft()

    if emo[screen][screen] == 0:
        emo[screen][screen] = emo[screen][clip] + 1
        q.append([screen, screen])
    if screen + clip <= n and emo[screen+clip][clip] == 0:
        emo[screen+clip][clip] = emo[screen][clip] + 1
        q.append([screen+clip, clip])
    if screen-1 >= 0 and emo[screen-1][clip] == -1:
        emo[screen-1][clip] = emo[screen][clip] + 1
        q.append([screen-1, clip])

res = emo[n][1]
for i in range(n):
    if emo[n][i] != 0:
        res = min(res, emo[n][i])

print(res-1)
