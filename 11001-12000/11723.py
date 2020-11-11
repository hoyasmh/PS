import sys
s=[0]*21
for i in range(int(input())):
    c=sys.stdin.readline().split()
    if c[0]=='add':
        s[int(c[1])]=1
    if c[0]=='remove':
        s[int(c[1])]=0
    if c[0]=='check':
        print(s[int(c[1])])
    if c[0]=='toggle':
        s[int(c[1])]=(s[int(c[1])]+1)%2
    if c[0]=='all':
        s=[1]*21
    if c[0]=='empty':
        s=[0]*21
