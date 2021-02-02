import sys

def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)

num = int(sys.stdin.readline())
print(factorial(num))