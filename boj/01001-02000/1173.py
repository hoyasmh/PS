N,m,M,T,R=map(int,input().split())
t,x=0,m
if m+T>M:
    print(-1)
    exit()
while N>0:
    if x+T<=M:
        x+=T
        N-=1
        t+=1
    else:
        x=max(m,x-R)
        t+=1
print(t)
