import sys
d={}
for i in range(int(input())):
    n=sys.stdin.readline()
    d[n]=d.get(n,0)+1
print(sorted([int(i) for i,j in d.items() if j==max(d.values())])[0])
