m,n=map(int, input().split())
l=[0]+list(map(int, input().split()))
for i in range(2,m+1):
    l[i]=l[i]+l[i-1]
for i in range(n):
    a,b=map(int,input().split())
    print(l[b]-l[a-1])
