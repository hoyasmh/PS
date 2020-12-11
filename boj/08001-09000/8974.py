l=[]
for j in range(50):
    l+=[j+1 for i in range(1,j+2)]
a,b=map(int,input().split())
print(sum(l[a-1:b]))
