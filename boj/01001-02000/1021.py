n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
i=1
while l:
    c+=min(abs(l[0]-i),n+l[0]-i,n-l[0]+i)
    i=l.pop(0)
    l=[l[j]-1 if l[j]>i else l[j] for j in range(len(l))]


    # t=[]
    # for j in range(1,len(l)):
    #     if l[j]>i:
    #         t.append(l[j]-1)
    #     else:
    #         t.append(l[j])
    # l=t
    n-=1
print(c)
