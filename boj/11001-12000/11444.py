def matmul(m, n):
    ret = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] = (ret[i][j] + m[i][k] * n[k][j])%(1000000007)
    return ret
n = int(input()) - 1
if (n == -1):
    print(0)
    exit()
ans = [[1 if i ==j else 0 for i in range(2)] for j in range(2)]
t = [[1, 1], [1, 0]]
while(n):
    if n % 2:
        ans = matmul(ans, t)
    t = matmul(t, t)
    n //= 2
print(ans[0][0])