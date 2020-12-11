def p(x,y):
    while x%y!=0:
        x,y=y,x%y
    return [0,1][y==1]
for i in range(int(input())):
    c=0
    a,b,n=map(int,input().split())
    for j in range(a,b+1):
        c+=p(n,j)
    print('Case #{}: {}'.format(i+1,c))
