a,b=map(int,input().split())
l=[0]*(a+b)
c=0
for i in range(a):
    s=input().split()
    for j in range(b):
        n=s[j].count('9')
        l[i]+=n
        l[a+j]+=n
        c+=n
print(c-max(l))
