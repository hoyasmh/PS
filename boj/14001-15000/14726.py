for i in range(int(input())):
    s=0
    n=input()
    for i in range(1,17):
        m=int(n[i-1])*(i%2+1)
        s+=m//10+m%10
    print('FT'[s%10==0])
