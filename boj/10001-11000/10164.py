from math import factorial as f
def c(x,y):
    return f(x+y)//f(x)//f(y)
m,n,o=map(int,input().split())
if o==0:
    print(c(m-1,n-1))
else:
    a,b=(o-1)//n,(o-1)%n
    print(c(a,b)*c(m-a-1,n-b-1))
