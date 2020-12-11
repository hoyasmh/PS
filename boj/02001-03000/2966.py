g=[['ABC'*34,'Adrian'],['BABC'*25,'Bruno'],['AABBCC'*17,'Goran']]
input()
l=[]
s=input()
for i in g:
    l.append(sum([1 for j,k in zip(i[0],s) if len(set([j,k]))==1]))
m=max(l)
print(m)
for a in range(3):
    if l[a]==m and m!=0:
        print(g[a][1])
