a=[1,2,3,3,4,10]
b=[1,2,2,2,3,5,10]
for i in range(int(input())):
    h=sum([i*j for i,j in zip(a,list(map(int,input().split())))])
    o=sum([i*j for i,j in zip(b,list(map(int,input().split())))])
    print('Battle {}:'.format(i+1),[['Evil eradicates all trace of Good','Good triumphs over Evil'][h>o],'No victor on this battle field'][h==o])
