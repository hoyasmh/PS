N=input()
n=int(input())
Y=sorted([input() for i in range(n)])
m=0
w=Y[0]
for i in range(n):
    l=[0]*4
    s='LOVE'
    for j in range(4):
        l[j]=(Y[i]+N).count(s[j])
    M=((l[0]+l[1])*(l[0]+l[2])*(l[0]+l[3])*(l[1]+l[2])*(l[1]+l[3])*(l[2]+l[3]))%100
    if M>m:
        m=M
        w=Y[i]
print(w)
