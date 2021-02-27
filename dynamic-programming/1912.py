n = int(input())
arr = list(map(int, input().split()))
        
ans = [-10000 for _ in range(n)]
ans[0] = arr[0]
