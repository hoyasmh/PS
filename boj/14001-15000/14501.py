n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
d=[0]*(n+1)
for i in range(n-1,-1,-1):
    if i+l[i][0]<=n:
        d[i]=max(d[i+1],l[i][1]+d[i+l[i][0]])
    else:
        d[i]=d[i+1]
print(d[0])
