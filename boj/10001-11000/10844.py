n=10
m=1000000000
d=[[0]*10 for i in range(n+1)]
for k in range(1,10):
    d[1][k]=1
for i in range(2,n+1):
    for j in range(10):
        d[i][j]=0
        if j-1>=0:
            d[i][j]+=d[i-1][j-1]
        if j+1<=9:
            d[i][j]+=d[i-1][j+1]
        d[i][j]%=m
for i in d:
    print(sum(i), sum(i[1:-2]),i[0],i[-1])
