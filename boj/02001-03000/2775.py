def f(a,b):
    if a==0:
        return b
    elif b==1:
        return 1
    else:
        return f(a-1,b)+f(a,b-1)
n=int(input())
for i in range(n):
    for j in range(2):
        k=int(input())
        n=int(input())
        print(f(k,n))
        break
