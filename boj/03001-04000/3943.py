import sys
for i in range(int(input())):
    n=int(sys.stdin.readline())
    m=n
    while n>1:
        if n%2==0:
            n//=2
        else:
            n=3*n+1
            if n>m:
                m=n
    print(m)
