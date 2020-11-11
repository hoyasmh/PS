m,n=map(int,input().split())
l=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for i in range(m)]
for j in range(1,m+1):
    for k in range(1,n+1):
        l[j][k]+=max(l[j-1][k],l[j][k-1])
print(max(l[-1]))
