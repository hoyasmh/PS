a,b,c=map(int,input().split())
l=[sorted([*map(int,input().split())],reverse=True) for i in range(3)]
x=[i+j+k for i,j,k in zip(*l)]
s=sum(x)
m=0
for i in l:
    m+=sum(i[len(x):])
print(s+m,int(s*0.9+m),sep='\n')
