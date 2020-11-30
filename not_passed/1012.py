n=int(input())
c=0
for i in range(n):
    m,n,k=map(int,input().split())
    l=[map(int,input().split()) for j in range(k)]
    while l:
        t=[]
        t.appent(l.pop(0))
        for a in l:
