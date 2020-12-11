import sys
n,m=map(int,input().split())
p={}
for i in range(n):
    p[str(i+1)]=sys.stdin.readline()
for j in range(m):
    a=sys.stdin.readline()
    if a.isdigit():
        print(p[a])
    else:
        print(p.keys(value==a))
