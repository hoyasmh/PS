l=[1,1]
for i in range(int(input())-2):
    l.append(l[-1]+l[-2])
print(l[-1])
    
