l=[]
for i in range(9):
    l+=[j for j in map(int,input().split())]
print(max(l))
n=l.index(max(l))
print(n//9+1,n%9+1)
