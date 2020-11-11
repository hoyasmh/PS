for i in [0]*int(input()):
    s=(j for j in input())
    l=[]
    n=0
    for j in s:
        if j=='>':
            n+=1
            n=min(len(l),n)
        elif j=='<':
            n-=1
            n=max(0,n)
        elif j=='-':
            if l:
                l.pop()
                n-=1
            else:
                continue
        else:
            l.insert(n,j)
            n+=1
    print(''.join(l))
