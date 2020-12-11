m,n=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
for j in range(n):
    a,b,c,d=map(int,input().split())
    print((2*a+b+d-2)*(d-b+1)//2+(d-b+1)*(c-a+1))
