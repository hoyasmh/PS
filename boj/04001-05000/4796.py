i=0
while 1:
    i+=1
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    print('Case {}: {}'.format(i,c//b*a+min(c%b,a)))
