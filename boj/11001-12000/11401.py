a,b=map(int,input().split())
c=1
for i in range(min(a-b,b)):
    c=c*(a-i)//(i+1)%1000000007
print(c)
