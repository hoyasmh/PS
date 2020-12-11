def bs(l,a,key):
    c=0
    idx=0
    i=0
    while(i<len(a)):
        if a[i]<=l[idx]:
            if c<key:
                c+=1
                i+=1
            else:
                c=0
                idx+=1
        else:
            idx+=1
            c=0
        if idx==len(l):
            return 0
    return 1

n=int(input())
l=sorted(list(map(int,input().split())))
m=int(input())
a=sorted(list(map(int,input().split())))

if a[-1]>l[-1]:
    print(-1)
    exit()
lp=m//n
rp=m
mid=(lp+rp)//2
while(lp<=rp):
    if bs(l,a,mid):
        rp=mid-1
    else:
        lp=mid+1
    mid=(lp+rp)//2
print(lp)
