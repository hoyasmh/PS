n,m=map(int,input().split())
l=[[1]*m for i in range(n)]
for i in range(1,n):
    for j in range(1,m):
        l[i][j]=(l[i-1][j]+l[i][j-1]+l[i-1][j-1])%1000000007
print(l[-1][-1])
