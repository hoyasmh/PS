while 1:
    a,b=map(int,input().split())
    if a==b==0:
        exit()
    c=1
    for i in range(min(b,a-b)):
        c=c*(a-i)//(i+1)
    print(c)
