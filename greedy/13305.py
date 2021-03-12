while 1:
    n = int(input())

    Llst = list(map(int, input().split()))
    priceList = list(map(int, input().split()))

    break

sum = Llst[0] * priceList[0]
price = priceList[0]

for i in range(1, n-1):
    if price > priceList[i]:
        price = priceList[i]
    
    sum += price * Llst[i]

print(sum) 
