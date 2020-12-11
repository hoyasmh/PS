n,k=map(int,input().split())
l=[int(input()) for i in range(n)]
def g(A,B,X):
    c=0
    for i in A:
        c+=i//B
    if c>=X:
        return 1
    else:
        return 0

def f(a,b,c,x):
    m=(b+c)//2
    if b==c and g(a,m,x):
        print(b)
        return
    elif b==c and not g(a,m,x):
        print(b-1)
        return

    if g(a,m,x)==1:
        f(a,m+1,c,x)
    else:
        f(a,b,m-1,x)
f(l,1,sum(l)//k,k)
