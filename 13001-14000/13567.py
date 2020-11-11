n,m=map(int, input().split())
x,y,d=0,0,0
for i in range(m):
    d=d%4
    c=input().split()
    if c[0]=='TURN':
        if c[1]=='0':
            d+=1
        else:
            d-=1
    if c[0]=='MOVE':
        if d==0:
            x+=int(c[1])
        elif d==1:
            y+=int(c[1])
        elif d==2:
            x-=int(c[1])
        else:
            y-=int(c[1])
    if x not in range(0,m+1) or y not in range(0,m+1):
        print(-1)
        break
    if i+1==m:
         print(x,y)
