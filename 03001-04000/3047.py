a,b,c = sorted(map(int, input().split()))
l=list(input())
l[l.index('A')]=a
l[l.index('B')]=b
l[l.index('C')]=c
print(*l)
