n,m,k=map(int,input().split())
l=(j for j in [int(input()) for i in range(n)])
def c(a,b):
    global l
    i=0
    for j in l:
        yield b if a==i else j
        i+=1
def p(a,b):
    global l
    i=0
    s=0
    for j in l:
        if a-1<=i<b:
            s+=j
            i+=1
    return s
for i in range(m+k):
    x,y,z=map(int,input().split())
    if x==1:
        l=c(y,z)
        print(list(l))
    else:
        print(p(y,z))
