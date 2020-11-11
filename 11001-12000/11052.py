# n=int(input())
# l=[0]+list(map(int,input().split()))
# d=[0]*(n+1)
# d[1]=l[1]
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         d[i]=max(d[i],d[i-j]+l[j])
#     print(d)
# print(d[-1])

n=int(input())
l=list(map(int,input().split()))
d=[0]*n
d[0]=l[0]
for i in range(n):
    for j in range(i):
        d[i]=max(d[i],d[i-j]+l[j])
    print(d)
print(d[-1])
