while 1:
    s=input()
    if s=='0':
        break
    else:
        n,p=map(int,s.split())
        print(*sorted([n+1-p,n+1-(p+[-1,1][p%2]),(p+[-1,1][p%2])]))
