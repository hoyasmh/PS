n=int(input())
l=[list(map(int,input().split())) for k in range(n)]
for j in range(1,n):
    for i in range(3):
        l[j][i]+=min(l[j-1][i-1],l[j-1][i-2])
print(min(l[-1]))
