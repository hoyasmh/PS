m,n=map(int, input().split())
s=[]
for j in range(1,46):
    s+=[j]*j
print(sum(s[m-1:n]))
