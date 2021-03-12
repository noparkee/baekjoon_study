from collections import deque
n, k = map(int, (input().split()))

if n >= k:
    print(n-k)
else:
    q = deque()    
    v = [0 for _ in range(k*2)]
    q.append(n)
    v[n] = 1
    
    while q:
        t = q.popleft()
        if 0<=t+1<k*2 and (v[t+1] == 0 or v[t+1] > v[t]):
            q.append(t+1)
            v[t+1] = v[t] + 1
        if 0<=t-1<k*2 and (v[t-1] == 0 or v[t-1] > v[t]):
            q.append(t-1)
            v[t-1] = v[t] + 1
        if 0<=2*t<k*2 and (v[2*t] == 0 or v[2*t] > v[t]):
            q.append(2*t)
            v[2*t] = v[t]
    
    print(v[k]-1)
