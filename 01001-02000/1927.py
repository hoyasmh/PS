import sys
n=int(input())
h=[]
for i in range(n):
    c=int(sys.stdin.readline())
    if c==0:
        if len(h)==0:
            print(0)
        else:
            print(h.pop(h.index(min(h))))
    else:
        h.append(c)
