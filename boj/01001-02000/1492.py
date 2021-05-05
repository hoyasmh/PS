l = []
for i in range(0, 51):
    sub =[1]
    n = i + 1
    r = 1
    while n:
        sub.append(sub[-1] * n // r)
        n -= 1
        r += 1
    l.append(sub)
n, k = map(int, input().split())
ans = [n]
for i in range(0, k):
    temp = (pow(n + 1, i + 2) - 1)
    for j in range(i + 1):
        temp = (temp - (ans[-(j + 1)] * l[i + 1][j + 2]))
    ans.append(temp//l[i + 1][1])    
print(ans[-1]%1000000007)
