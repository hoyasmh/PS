n=int(input())
l=[int(input()) for i in range(n)]
if n<3:
    print(sum(l))
d=[0]*n
d[0],d[1],d[2]=l[0],l[1]+l[0],max(l[2]+l[1],l[0]+l[2])
for j in range(3,n):
    d[j]=max(d[j-3]+l[j-1]+l[j],d[j-2]+l[j],d[j-1])
print(d[-1])
