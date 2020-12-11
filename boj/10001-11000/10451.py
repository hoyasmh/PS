for s in [0]*int(input()):
    m=int(input())
    n=map(int,input().split())
    l={i+1:j for i,j in enumerate(n)}
    a=[]
    c=0
    for k in range(1,m+1):
        if k not in a:
            while 1:
                a.append(k)
                k=l[k]
                if k in a:
                    c+=1
                    break
    print(c)
