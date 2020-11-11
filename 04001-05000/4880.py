while 1:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    print('GA'[a+c==2*b]+'P',2*c-b if a+c==2*b else c**2//b)
