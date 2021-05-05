mod = 1000000007
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
n, m = map(int, input().split())
l = []
begin = 2;
while n > 1 and begin * begin <= n:
    cnt = 0
    while n % begin == 0:
        cnt += 1
        n //= begin
    if cnt:
        l.append([begin, cnt * m])
    begin += 1
if n != 1:
    l.append([n, m]) 
ans = 1
for i in l:
    ans = ans * _sum(i[1] + 1, i[0], mod) % mod
print(ans)   