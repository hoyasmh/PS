s,k=map(int,input().split())
q,r=s//k,s%k
print((q+1)**r*q**(k-r))
