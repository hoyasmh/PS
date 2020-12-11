x,y=map(int, input().split())
def f(x,y,n):
    if 100*y//x>=99:
        return -1
    else:
        return 100*(y+n)//(x+n)==100*y//x
l=0
r=2e9
while l<=r:
    m=(l+r)//2
    if f(x,y,m)==-1:
        print(-1)
        exit()
    elif f(x,y,m)==1:
        l=m+1
    else:
        r=m-1
print(int(l))

# r=x-100*y+100*y//x*x
# if r<0:
#     print(-1)
# else:
#     print(r)
