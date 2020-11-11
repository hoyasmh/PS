n=int(input())
l=sorted(list(set([input() for i in range(n)])))
print(*sorted(l,key=len), sep='\n')
