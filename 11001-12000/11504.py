for i in range(int(input())):
    m,n=map(int,input().split())
    a,b=int(input()[::2]),int(input()[::2])
    l=input()[::2]*2
    c=0
    for i in range(m):
        x=l[i:i+n]
        if a<=int(x)<=b:
           c+=1
    print(c)         
