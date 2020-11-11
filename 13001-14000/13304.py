import sys
import math
n,k=map(int, input().split())
l=[0]*5
for i in range(n):
    a=list(map(int, sys.stdin.readline().split()))
    if a[0]==1:
        if a[1]>4:
            l[0]+=1
        elif a[1]>2:
            l[1]+=1
        else:
            l[4]+=1
    else:
        if a[1]>4:
            l[2]+=1
        elif a[1]>2:
            l[3]+=1
        else:
            l[4]+=1
print(sum([math.ceil(j/k) for j in l]))
