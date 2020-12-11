a,b=map(int,input().split())
for i in range(1,b+1):
    if b%i==0 and i+b//i==(a-4)//2:
        print(b//i+2,i+2)
        break
