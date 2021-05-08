def mat(a, b, n):
	ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%1000003
	return ret
	   
n, s, e, t = map(int, input().split())
l = [[int(j) for j in input()] for i in range(n)]
ans = [[1 if i==j else 0 for i in range(n)] for j  in range(n)]
while(t):
	if t%2:
		ans = mat(ans, l, n)
	l = mat(l, l, n)
	t//=2
for i in ans:
	print(*i)