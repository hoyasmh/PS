n=input()
while n!='0':
    l=[n]
    while len(n)>1:
        m=1
        for i in n:
            m*=int(i)
        n=str(m)
        l.append(n)
    print(*l)
    n=input()
