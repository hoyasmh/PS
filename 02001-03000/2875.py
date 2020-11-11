m,n,k=map(int, input().split())
if m>=2*n:
    print((3*n-max(0,k-m+2*n))//3)
else:
    print((m//2*3-max(0,k-n+m//2-m%2))//3)
