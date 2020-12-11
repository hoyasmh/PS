n=10000000
r=min(9,n)
n1=1
r1=1
for i in range(r):
    n1*=n+9-i
    r1*=r-i
print(n1//r1%10007,1)

d=[1]*10
p=[0]*10
for i in range(n-1):
    for j in range(10):
        p[j]=sum(d[:j+1])%10007
    d=p[:]
print(sum(d)%10007,2)
