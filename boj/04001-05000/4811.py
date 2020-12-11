while 1:
    n=int(input())
    if n==0:
        break
    c=1
    for i in range(n):
        c=c*(n*2-i)//(i+1)
    print(c//(n+1))
