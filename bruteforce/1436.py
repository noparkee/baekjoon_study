n = int(input())
a = [666, 1666, 2666, 3666, 4666, 5666]
num = 6660
cnt = 6

if n >= 1 and n <= 6:
    print(a[n-1])
else:
    while True:
        if '666' in str(num):
            cnt += 1
            if n == cnt:
                print(num)
                break

        num += 1
