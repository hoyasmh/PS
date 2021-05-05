m, a, c, x, n, g = map(int, input().split())
ans = 1
while(n):
    if n % 2:
         ans = ans * a % m
    a = (a * a) % m
    n //= 2
print(((x - c//(1 - a)) * ans + c//(1 - a)) % m)