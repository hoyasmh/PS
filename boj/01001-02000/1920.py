m=int(input())
a=sorted(list(map(int,input().split())))
n=int(input())
q=list(map(int,input().split()))
def f(i,l):
    if i<l[0] or i>l[-1]:
        return 0
    s,e=0,len(l)-1
    while s<=e:
        m=(s+e)//2
        if l[m]==i:
            return 1
        if l[m]>i:
            e=m-1
        else:
            s=m+1
    return 0
for j in q:
    print(f(j,a))
