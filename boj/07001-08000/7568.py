n=int(input())
l=[list(map(int, input().split())) for i in range(n)]
c=[1]*n
for j in range(len(l)):
    for k in l:
        if l[j][0]<k[0] and l[j][1]<k[1]:
            c[j]+=1
print(*c)
