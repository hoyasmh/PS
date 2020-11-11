c=1
n=int(input())
while n!=0:
    l=[input() for i in range(n)]
    k=[0]*n
    for i in range(2*n-1):
        k[int(input().split()[0])-1]+=1
    print(c,l[k.index(1)])
    c+=1
    n=int(input())
