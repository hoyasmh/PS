# m,n=map(int,input().split())
# l=list(map(int,input().split()))
# a,b,c=0,0,0
# for i in range(m):
#     b+=1
#     if sum(l[a:b])==n:
#         c+=1
#     while sum(l[a:b])>n:
#         a+=1
#         if sum(l[a:b])==n:
#             c+=1
# print(c)

m,n=map(int,input().split())
l=list(map(int,input().split()))
a,b,c=0,0,0
for i in range(m):
    b+=1
    while sum(l[a:b])>=n:
        print(l[a:b])
        if sum(l[a:b])==n:
            c+=1
        a+=1
print(c)
