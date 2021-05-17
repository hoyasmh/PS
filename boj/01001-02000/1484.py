n = int(input())
i = 1
l = []
while i * i <= n:
    if n % i == 0 and (n // i + i) % 2 == 0 and n // i != i:
        l.append((n // i + i) // 2)
    i += 1
if l:
    print(*sorted(l), sep = "\n")
else:
    print(-1)