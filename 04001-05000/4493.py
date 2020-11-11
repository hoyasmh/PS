for i in range(int(input())):
    s='RPSR'
    l=[0,0]
    for j in range(int(input())):
        a=input().split()
        if a[1]!=a[0]:
            if len({s[k:k+3].index(a[k]) for k in range(2)})==1:
                l[1]+=1
            else:
                l[0]+=1
    print('TIE' if l[0]==l[1] else 'Player '+'12'[l[0]<l[1]])
