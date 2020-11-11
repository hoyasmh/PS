m,n=map(int,input().split())
l=[list(map(int, list(input()))) for k in range(m)]
a=max(l[0]+[x[0] for x in l])
for i in range(1,m):
    for j in range(1,n):
        if l[i][j]!=0:
            l[i][j]=min(l[i-1][j],l[i-1][j-1],l[i][j-1])+1
            a=max(a,l[i][j])
print(a**2)
