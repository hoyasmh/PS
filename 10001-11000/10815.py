n=int(input())
a=sorted(list((input().split())))
m=int(input())
b=list(input().split())
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
for i in b:
    print(f(i,a),end=' ')
