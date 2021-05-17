import math
n,m=map(int,input().split())
if n>m:
    n,m = m,n
l=[1]*(n+1)
cnt=0
for i in range(1,n+1):
    if l[i]:
        cnt+=int(math.sqrt(n//i))*int(math.sqrt(m//i))
        j=2
        while i*j*j<= n:
            l[i*j*j] = 0
            j+=1
print(cnt)
        
    