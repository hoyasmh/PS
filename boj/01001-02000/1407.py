def s(n):
    cnt = 0
    b = 1
    while n:
        cnt += n // 2 * b + n % 2 * b
        b *= 2
        n //= 2
    return cnt    
a, b = map(int, input().split())
print(s(b) - s(a - 1))
