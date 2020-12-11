m,n=map(int, input().split())
l=list(map(int, input().split(',')))
def f(a,b):
    if b==0:
        return a
    else:
        a=[a[i+1]-a[i] for i in range(len(a)-1)]
        return f(a,b-1)
print(*f(l,n),sep=',')
