for i in range(int(input())):
    n,m=map(int,input().split())
    c=0
    for a in range(1,n-1):
        for b in range(a+1,n):
            if (b%a*b+a*a+m)%(b*a)==0:
                c+=1
    print(c)
