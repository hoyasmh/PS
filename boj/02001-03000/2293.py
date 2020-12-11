n,k=map(int,input().split())
l=[int(input()) for i in range(n)]
s=set(l)
u=set()
c=1
while s:
    for i in l:
        for j in list(s):
            if i+j<=k:
                u.add(i+j)
    s=u
    u=set()
    c+=1
    if k in s:
        print(c)
        exit()
print(-1)
