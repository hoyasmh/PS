import math
for i in [0]*int(input()):
    m,n,x,y=map(int,input().split())
    for j in range(0,m//math.gcd(m,n)+1):
        if (n*j+y-x)%m==0:
            print(n*j+y)
            break
        elif j==m//math.gcd(m,n):
            print(-1)
