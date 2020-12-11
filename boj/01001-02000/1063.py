a,b,n=input().split()
S='0ABCDEFGH'
f='RLTB'
c=[1,-1]
k=[S.index(a[0]),int(a[1])]
s=[S.index(b[0]),int(b[1])]
for i in range(int(n)):
    l,t=k[:],s[:]
    d=input()
    for j in d:
        l[f.index(j)//2]+=c[f.index(j)%2]
    if l==t:
        for m in d:
            t[f.index(m)//2]+=c[f.index(m)%2]
    if 0 in l+t or 9 in l+t:
        continue
    else:
        k,s=l[:],t[:]
print(S[k[0]]+str(k[1]),S[s[0]]+str(s[1]),sep='\n')
