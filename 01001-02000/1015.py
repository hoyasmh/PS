n=int(input())
l=[[i,j] for i,j in enumerate(map(int, input().split()))]
l.sort(key = lambda x: x[1])
l=[k[0] for k in l]
a=[0]*n
u=0
for m in l:
    a[m]=u
    u+=1
print(a)
