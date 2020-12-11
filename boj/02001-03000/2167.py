m,n=map(int,input().split())
l=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for i in range(m)]
for i in range(1,m+1):
    for j in range(1,n+1):
        l[i][j]=(l[i-1][j]+l[i][j-1]+l[i][j]-l[i-1][j-1])
k=int(input())
for j in range(k):
    a,b,x,y=map(int,input().split())
    print(l[x][y]-l[x][b-1]-l[a-1][y]+l[a-1][b-1])
