import math
n=int(input())
s=list(map(int, input().split()))
for i in range(1,n):
    g=math.gcd(s[0],s[i])
    print('{}/{}'.format(s[0]//g,s[i]//g))
