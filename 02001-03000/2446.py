n=5
for i in range(2*n-1):
    print(' '*(n-abs(n-i-1)-1)+'*'*(2*abs(n-i-1)+1))
