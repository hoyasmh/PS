for i in range(int(input())):
    n=int(input())
    if n<3:
        print(n)
    else:
        a,b,c=1,2,4
        for i in range(n-3):
            a,b,c=b,c,a+b+c
        print(c)
