import sys
l=[0]
c=0
for k in range(int(input())):
    n=int(sys.stdin.readline())
    while l and n>=l[-1]:
        l.pop(-1)
    l.append(n)
    c+=len(l)-1
print(c)
