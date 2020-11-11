l=['z0','o0','t1','t0','f1','f0','s1','s0','e0','n0',]
m,n=map(int,input().split())
d=dict()
t=[]
for i in range(m,n+1):
    s=''
    for j in str(i):
        s+=l[int(j)]
    t.append(s)
    d[s]=i
c=1
for k in sorted(t):
    print(d[k], end=' ')
    if c%10==0:
        print('')
    c+=1
