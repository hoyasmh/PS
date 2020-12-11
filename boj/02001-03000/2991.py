a,b,c,d=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in l:
    print(bool(0<i%(a+b)<=a)+bool(0<i%(c+d)<=c))
