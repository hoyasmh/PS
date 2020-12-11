n=int(input())
i=1
while n!=0:
    print('{}. {} {}'.format(i,['odd','even'][n%2==0],n//2))
    n=int(input())
    i+=1
