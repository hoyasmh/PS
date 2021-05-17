def mat(l, m):
    ret = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] = (ret[i][j] + l[i][k] * m[k][j]) % 10007
    return ret
n = int(input()) - 1
ans = [[1, 0], [0, 1]]
m = [[2, 6], [1, 0]]
while n:
    if n % 2:
        ans = mat(ans, m)
    m = mat(m, m)
    n //= 2
print(ans[1][0] * 6 + ans[1][1] * 2)    
