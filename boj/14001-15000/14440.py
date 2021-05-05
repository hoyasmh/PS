def mat(a, b, n):
	ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%100
	return ret
def fib(n, x, y, a0, a1):
    if n < 0:
        return a0
    l = [[x, y], [1, 0]]
    ans = [[1,0],[0,1]]
    while(n):
        if n%2:
            ans = mat(ans, l, 2)
        l = mat(l, l, 2)
        n//=2
    return (ans[0][0] * a1 + ans[0][1] * a0) % 100
x, y, a0, a1, n = map(int, input().split())
num = format(fib(n-1, x, y, a0, a1), '02')
print(num)