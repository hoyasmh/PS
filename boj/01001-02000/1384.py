n=int(input())
c=1
while n!=0:
    l=[input().split() for i in range(n)]
    print('Group',c)
    k=0
    for i in range(n):
        for j in range(1,n):
            if l[i][j]=='N':
                print('{} was nasty about {}'.format(l[(n-j+i)%n][0],l[i][0]))
                k+=1
    if k==0:
        print('Nobody was nasty')
    c+=1
    print('')
    n=int(input())
