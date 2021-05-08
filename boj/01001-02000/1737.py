import math
n = int(input())
l = [[0] * (n + 1) for i in range (n + 1)]
def pib(n, p):
    if l[n][p]:
        return l[n][p]
    if n - p * math.pi <= math.pi:
        l[n][p] = 1
        return l[n][p]
    l[n][p] = (pib(n - 1, p) + pib(n , p + 1)) % int(1e18)
    return l[n][p]
print(pib(n, 0))
