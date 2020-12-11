a=int(input())
b=int(input())
l=[i for i in range(a,b+1) if int(i**0.5)**2==i]
if not l:
    print(-1)
else:
    print(*[sum(l),l[0]], sep='\n')
