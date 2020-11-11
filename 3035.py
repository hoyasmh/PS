a,b,c,d=map(int,input().split())
l=[]
for i in range(a):
    l=l+[''.join([j*d for j in input()])]*c
print(*l,sep='\n')
