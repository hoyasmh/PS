def _pow(n, r, mod):
    ret = 1
    while n:
        if n % 2:
            ret = ret * r % mod
        r = r * r % mod
        n //= 2    
    return ret
def _sum(n, r, mod):
    if n == 1:
        return 1
    if n % 2 == 0:
        return _sum(n//2, r, mod) * (1 + _pow(n//2, r, mod)) % mod
    return (_sum(n//2, r, mod) * (1 + _pow(n//2, r, mod)) + _pow(n - 1, r, mod)) % mod
    
a,r,n,mod = map(int, map(int, input().split()))
print(_sum(n, r, mod) * a % mod)