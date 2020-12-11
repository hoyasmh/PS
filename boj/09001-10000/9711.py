import sys
l=[1,1]
for i in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    while len(l)<a:
        l.append(l[-1]+l[-2])
    print('Case #{}: {}'.format(i+1,l[a-1]%b))
