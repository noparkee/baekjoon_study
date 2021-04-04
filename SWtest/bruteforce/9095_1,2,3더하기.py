n = int(input())

ans = [1,2,4]   

for i in range(3, 10):
    ans.append(ans[i-3] + ans[i-2] + ans[i-1])
for i in range(n):
    num = int(input())
    print(ans[num-1])

### brute-force이지만 DP로!
### 나중에 다시