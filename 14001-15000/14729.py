import sys
l=[]
for i in range(int(input())):
    n=float(sys.stdin.readline())
    if i>6:
        if l[-1]>n:
            l[-1]=n
            l.sort()
    else:
        l.append(n)
        l.sort()
for i in l:
    print('%.3f' % i)
