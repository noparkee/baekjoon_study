'''
뒤에서 부터 자신보다 뒤에 있는 수가 작은 수 찾기.
그 두 개 스왑하고 내림차순 정렬
'''

n = int(input())
lst = list(map(int, input().split()))
sor = sorted(lst)
if lst == sor:
    print(-1)
else:
    for i in range(n-1, -1, -1):
        cnt = 0
        for j in range(n-1, i, -1):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                cnt += 1
                break
        if cnt > 0:
            break

    ans = lst[i+1:]
    ans = sorted(ans, key=lambda x: -x)
    lst[i+1:] = ans

    print(' '.join(list(map(str, lst))))

'''
[(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]
'''