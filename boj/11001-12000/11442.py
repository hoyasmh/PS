def mat(a, b):
	ret = [[0]*2 for i in range(2)]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%1000000007
	return ret
def fib(n):
    l = [[1,1],[1,0]]
    ans = [[1,0],[0,1]]
    while(n):
        if n%2:
            ans = mat(ans, l)
        l = mat(l, l)
        n//=2
    return ans[1][0]        
n = int(input())
print(fib(n + n%2))