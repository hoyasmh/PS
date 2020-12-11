n=int(input())
l=list(map(int,input().split()))
a,b,m,M=0,1,0,0
while b<n:
    if l[a]>l[b]:
        m+=1
        b+=1
    else:
        M,m=max(m,M),0
        a,b=b,b+1
print(max(M,m))
