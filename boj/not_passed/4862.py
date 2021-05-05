import sys
def period(m, n):
    chk = [0] * 10000000
    mod = pow(10, n)
    temp = m % mod
    m = temp
    i = 1
    while 1:
        if chk[temp]:
            return [i, chk[temp]]
        chk[temp] = i
        i += 1
        temp = temp * m % mod

b = int(sys.stdin.readline())
while b:
    i, n = int(sys.stdin.readline()), int(sys.stdin.readline())
    ans = b
    p = period(b, n)
    for j in range(i - 1):
        ans = p[1] + (ans - p[1]) % (p[0] - p[1])
        ans = pow(b, ans)
    ans %= pow(10, n)    
    print(str(ans).rjust(n, '0'))
    b = int(sys.stdin.readline())
        