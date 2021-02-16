import sys

size = list(map(int, sys.stdin.readline().split())) # 행 / 열
board = []
for i in range(size[0]):
    board.append(sys.stdin.readline()[:-1])

wstr = 'WBWBWBWB'
bstr = 'BWBWBWBW'

min = 64

for i in range(size[0]-7):  
    for j in range(size[1]-7): 
        # 시작 위치
        w = 0
        b = 0
        for k in range(8):
            tmp = board[i+k][j:j+8]
            
            if (i+k)%2 == 0:
                for k in range(8):
                    if wstr[k] != tmp[k]:
                        w += 1
                    if bstr[k] != tmp[k]:
                        b +=1
            else:
                for k in range(8):
                    if bstr[k] != tmp[k]:
                        w += 1
                    if wstr[k] != tmp[k]:
                        b +=1
            
        if min > w:
            min = w
        if min > b:
            min =b

print(min)