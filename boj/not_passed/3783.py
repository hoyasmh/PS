import sys, math
def troot(n):
    left = 0
    rignt = n
    t = math.sqrt(n)
    while 1:
        if abs(t**3 - n) < 0.00000000001:
            return t
        if t**3 < n:
            left = t
            t = (t + right) / 2
        else:
            right = t
            t /= 2
n = int(sys.stdin.readline())
for i in range(n):
    t = int(sys.stdin.readline())
    if t == 1:
        print(1.0000000000)
    else:
        print(troot(t))