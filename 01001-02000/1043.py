n,m=map(int,input().split())
a=set(input().split()[1:])
c=m
for i in range(m):
    b=set(input().split()[1:])
    if a & b:
        c-=1
        a=a|b
print(c)
