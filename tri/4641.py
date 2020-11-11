while 1:
    l=list(map(int, input().split()))
    if len(l)==1:
        exit()
    c=0
    for i in range(len(l)-1):
        if l[i]*2 in l:
            c+=1
    print(c)
