import sys
import collections
n=int(input())
l=collections.deque([i for i in range(1,n+1)])
a=[int(sys.stdin.readline()) for i in range(n)]
s=[]
d=[]
for i in range(n):
    while len(l)!=0 and l[0]<=a[i]:
        s.append(l.popleft())
        d.append('+')
    if a[i]!=s.pop():
        print('NO')
        exit()
    d.append('-')
print(*d,sep='\n')
