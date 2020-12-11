n=int(input())
l=list(map(int,input().split()))
m=l[0]
for i in range(1,n):
    if l[i-1]>0:
        l[i]=l[i]+l[i-1]
    if l[i]>m:
        m=l[i]
print(m)
