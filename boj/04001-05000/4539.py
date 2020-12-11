for i in range(int(input())):
    n=int(input())
    c=0
    while n>9:
        c+=1
        if n%10>4:
            n=n//10+1
        else:
            n//=10
    print(10**c*n)
