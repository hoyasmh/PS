n=int(input())
l=sorted([int(input()) for j in range(n)],reverse=True)
m=0
for i in range(len(l)):
    if m<l[i]*(i+1):
        m=l[i]*(i+1)
print(m)
