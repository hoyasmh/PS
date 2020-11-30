for j in range(int(input())):
    a,b,c=0,0,1
    for i in range(int(input())):
        a,b,c=b,c,(a+b+c)%1000000009
    print(c)
