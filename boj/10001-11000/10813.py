m,n=map(int, input().split())
l=[i+1 for i in range(m)]
for j in range(n):
    a,b=map(int, input().split())
    l[a-1],l[b-1]=l[b-1],l[a-1]
print(*l)
