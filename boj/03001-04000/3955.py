for i in range(int(input())):
    a,b=map(int,input().split())
    if a%b==0:
        print('IMPOSSIBLE')
        continue
    n=1
    while n%b!=0:
        n+=a
    print(n//b)
