l=list(map(int,input().split()))
a=sorted(l)
while l!=a:
    for i in range(4):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            print(*l)
