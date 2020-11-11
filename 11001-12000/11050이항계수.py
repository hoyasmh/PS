n,r=map(int, input().split())
r=min(r,n-r)
n1=1
r1=1
for i in range(r):
    n1*=n-i
    r1*=r-i
print(n1//r1)
