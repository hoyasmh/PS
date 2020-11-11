a=[0,0,0]
for i in range(int(input())):p=int(input());a=[a[1]+p,a[2]+p,max(a[:2])]
print(max(a[:2]))




a=0
b=0
c=0
for _ in range(int(input())):
    n=int(input())
    d=a
    a=c
    c=max(d+n,b+n)
    b=d+n
print(c)
