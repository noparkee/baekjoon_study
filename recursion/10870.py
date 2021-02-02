import sys

def pibo(num):
    if num <= 1:
        return num
    else:
        return pibo(num-1) + pibo(num-2)

num = int(sys.stdin.readline())
print(pibo(num))