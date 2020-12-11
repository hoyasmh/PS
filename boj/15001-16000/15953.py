l=[0,500,300,200,50,30,10]
for i in range(int(input())):
    a,b=map(int,input().split())
    j,k=0,0
    while a<22 and a>0:
        j+=1
        a-=j
    while b<32 and b>0:
        b-=2**k
        k+=1
    print((l[j]+bool(k)*2**(10-k))*10000)
