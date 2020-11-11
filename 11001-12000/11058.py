n=int(input())
l=[1]+[0]*99
for i in range(1,n):
    l[i]=max(l[i-1]+1,l[i-3]*2,l[i-4]*3,l[i-5]*4)
print(l[n-1])
