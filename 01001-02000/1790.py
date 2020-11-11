a,b=map(int,input().split())
n,k=0,0
while b>0:
    n+=1
    k=9*n*10**(n-1)
    b-=k
b+=k
p,q=divmod(b-1,n)
m=10**(n-1)+p
print([str(m)[q],-1][m>a])


saito 풀이
N,k=map(int,input().split());l,h=1,N+1
while l<h:
 m=l+h>>1;s=len(str(m));y=-~m*s-10**s//9
 if y<k:l=m+1
 else:h=m;z=~y
print(-(l>N)or str(l)[k+z])
