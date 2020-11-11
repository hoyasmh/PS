m,n=map(int,input().split())
l=[j for j in zip(*[list(map(int,input().split())) for i in range(n)])]
a,b=min(l[0]),min(l[1])
print(min(m//6*a+m%6*b,m*b,m//6*a+a))
