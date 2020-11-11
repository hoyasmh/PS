import math
n,k=map(int,input().split())
s='0'
for i in range(1,2**(int(math.log2(5*n))+1)):
    s+=bin(i)[2:]
for i in range(5):
    print(s[k-1+i*n])

n,k=map(int,input().split())
s='0'
for i in range(1,90):
    s+=bin(i)[2:]
print(*[s[k-1+i*n] for i in range(5)])
