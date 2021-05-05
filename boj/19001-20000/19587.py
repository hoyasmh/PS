def mat(a, b, n):
	ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%1000000007
	return ret
def fib(n):
    l = [[0,1,1],[1,0,1],[1,1,1]]
    ans = [[1,0,0],[0,1,0],[0,0,1]]
    while(n):
        if n%2:
            ans = mat(ans, l, 3)
        l = mat(l, l, 3)
        n//=2
    return sum(ans[-1])
print(fib(int(input()))%1000000007)