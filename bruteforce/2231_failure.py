import sys

def check():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                ms = i + j + k + (100 * i + 10*j + k)
                if ms == n:
                    return ms - (i+j+k)

    return 0    

n = int(sys.stdin.readline())
print(check())

# 이거 왜 안 되지..?