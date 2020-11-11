n, k=map(int, input().split())
a=sorted([list(map(int,input().split())) for i in range(n)])
b=a[k-1][1:]
c=[i[1:] for i in a]
c.sort(reverse=True)
print(c.index(b)+1)
