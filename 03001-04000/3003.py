l=list(map(int, input().split()))
c=[1,1,2,2,2,8]
print(*[c[i]-l[i] for i in range(6)])
