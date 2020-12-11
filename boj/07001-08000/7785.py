import sys
d={}
for i in range(int(input())):
    a,b=sys.stdin.readline().split()
    if b=='enter':
        d[a]=1
    else:
        d[a]-=1
print(*sorted([i for i,j in d.items() if j>0],reverse=True),sep='\n')
