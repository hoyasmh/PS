mod = 10**9 +7
n = int(input()) - 1
ans = 1
r = 2
while n >0:
    if n % 2:
        ans = (ans * r) % mod
    r = r * r % mod    
    n //= 2
print(ans)    