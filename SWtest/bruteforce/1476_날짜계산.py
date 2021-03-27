e, s, m = map(int, input().split())

def change(o, n):
    t = o%n
    if t == 0:
        return n
    else:
        return t  

if e==s==m:     # 15이하
    print(e)

else:   # 15초과
    num = 16
    while 1:
        e2 = change(num, 15)
        s2 = change(num, 28)
        m2 = change(num, 19)
        
        if e2==e and s2==s and m2==m:
            break
            
        num += 1
        
    print(num)
