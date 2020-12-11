n,m=map(int,input().split())
d=0
l=[0]*4
for i in range(m):
    d=d%4
    c=input().split()
    if c[0]=='TURN':
        if c[1]=='0':
            d+=1
        else:
            d-=1
    if c[0]=='MOVE':
        l[d]+=int(c[1])
    x,y=l[0]-l[2],l[1]-l[3]
    if  x not in range(n+1) or y not in range(n+1):
        print(-1)
        break
    if i+1==m:
        print(x,y)
