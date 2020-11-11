a,b,n,w=map(int,input().split())
c=0
m=0
for i in range(1,n):
    if a*i+b*(n-i)==w:
        c+=1
        m=i
print(*[[-1],[m,n-m]][c==1])
