n=int(input())
l=[list(map(int, input().split())) for k in range(n)]
if n==1:
    print(l[0])
for i in range(1,n):
    for j in range(i+1):
        if j==0 or j==i:
            l[i][j]+=l[i-1][-bool(j)]
        else:
            l[i][j]+=max(l[i-1][j-1],l[i-1][j])
print(max(l[-1]))

# cl=[]
# for __ in range(int(input())):
#     nl=[int(x) for x in input().split()]
#     cl=[max(a, b) + c for a, b, c in zip([0] + cl, cl + [0], nl)]
# print(max(cl))
