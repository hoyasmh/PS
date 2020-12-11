n=int(input())-1
for i in range(2*n+1):
    print(' '*(n-abs(n-i))+'*'+'* '[n-abs(n-i)>0]*(n-1)+'*'+' '*(2*abs(n-i)-1)+'*'*[1,0][n==i]+'* '[n-abs(n-i)>0]*(n-1)+'*')
