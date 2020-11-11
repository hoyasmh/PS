for i in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    c=0
    while len(l)>1:
        a=[]
        for j in range(len(l)-1):
            a.append(l[i]+l[i+1])
            c+=l[i]+l[i+1]


        print(l)
    print(c)
