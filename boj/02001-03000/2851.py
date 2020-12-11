l=[int(input()) for i in range(10)]
i=1
while l[i-1]<100:
    l[i]=l[i]+l[i-1]
    i+=1
if l[i-1]-100<=100-l[i-2]:
    print(l[i-1])
else:
    print(l[i-2])
