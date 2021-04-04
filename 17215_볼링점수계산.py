l = list(input())
integer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def score(x, i):
    if x[i] == '-':
        return 0
    elif x[i] == 'P' and i-1>=0:
        return 10 - score(x, i-1)
    elif x[i] == 'S':
        return 10
    else:
        return int(x[i])

sum = 0
plus = 0
frame = 1
for i in range(len(l)):
    if l[i] in integer:
        sum += score(l, i)     
        frame += 0.5
    
    elif l[i] == '-':
        frame += 0.5
    
    elif l[i] == 'P':
        sum += score(l, i)
        if frame < 10:
            sum += score(l, i+1)
        frame += 0.5

    elif l[i] == 'S':
        sum += score(l, i)
        if frame < 10:
            sum += score(l, i+1)
            sum += score(l, i+2)
        
        frame += 1
    
print(sum)