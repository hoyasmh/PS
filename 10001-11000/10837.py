x=int(input())
for i in range(int(input())):
    a,b=map(int,input().split())
    if (a>b and b+x+3>2*a) or (a<b and a+x+2>2*b) or a==b:
        print(1)
    else:
        print(0)
