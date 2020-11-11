m,n=map(int, input().split())
l=list(range(1,m+1))
for i in range(n):
    a,b=map(int, input().split())
    l=l[:a-1]+list(reversed(l[a-1:b]))+l[b:]
print(*l)
