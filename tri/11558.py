n=int(input())
for i in range(n):
    m=int(input())
    l=[int(input()) for j in range(m)]
    x=l[0]
    c=1
    while x!=m:
        x=l[x-1]
        c+=1
        if c>m:
            break
    print([c,'0'][c>m])
