from itertools import permutations

def func(lst):
    sum = 0
    for i in range(len(lst)-1):
        temp = lst[i]-lst[i+1]
        if temp > 0:
            sum += temp
        else:
            sum -= temp
    
    return sum


n = int(input())
lst = list(map(int, input().split()))

ans=[]
for i in list(permutations(lst, n)):
    ans.append(func(i))

print(max(ans))
