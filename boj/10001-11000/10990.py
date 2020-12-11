import math
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'+' '*(2*i-3)+'*'*math.ceil((i-1)/n))
