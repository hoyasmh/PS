n,k=map(int,input().split())
m=0
for i in range(k):
    a=int(str(n*(i+1))[::-1])
    if a>m:
        m=a
print(m)
