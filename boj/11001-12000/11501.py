for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    while l:
        m=max(l)
        d=l.index(m)
        s+=m*d-sum(l[:d])
        l=l[d+1:]
    print(s)
