n=int(input())
l=sorted([*map(int,input().split())])
s=0
for i in range(n-1):
    s+=sum(l[:i+1])*l[i+1]
print(s)
