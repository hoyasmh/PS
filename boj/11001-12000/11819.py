a, b, c = map(int, input().split())
ans = 1
while b:
    if b % 2:
        ans = (ans * a) % c
    a = a * a % c
    b //= 2
print(ans)    