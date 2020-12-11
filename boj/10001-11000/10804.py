l=list(range(1,21))
for i in range(10):
    a,b=map(int, input().split())
    l=l[:a-1]+l[a-1:b][::-1]+l[b:]
print(*l)
