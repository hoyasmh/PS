n=int(input())
l=sorted([list(map(int, input().split())) for i in range(n)])
for j in l:
    print(*j)
