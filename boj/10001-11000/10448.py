from itertools import combinations_with_replacement
t=[i*(i+1)//2 for i in range(1,45)]
t2=[sum(j) for j in combinations_with_replacement(t,3) if sum(j)<1001]
n=int(input())
for i in range(n):
    if int(input()) in t2:
        print(1)
    else:
        print(0)
