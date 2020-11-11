n=int(input())
l=[1,1,1]
for i in range(n-3):
    l.append(l[-1]+l[-3])
print(l[-1])    
