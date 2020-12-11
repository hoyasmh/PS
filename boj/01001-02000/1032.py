n=int(input())
s=[input() for i in range(n)]
l=[len(set(j)) for j in zip(*s)]
sc=''
for k in range(len(l)):
    if l[k]==1:
        sc+=s[0][k]
    else:
        sc+="?"
print(sc)
