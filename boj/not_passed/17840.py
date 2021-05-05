import sys
def mat(a, b, m):
	ret = [[0]*2 for i in range(2)]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%m
	return ret
def fib(n, m):
    l = [[1,1],[1,0]]
    ans = [[1,0],[0,1]]
    while(n):
        if n%2:
            ans = mat(ans, l, m)
        l = mat(l, l, m)
        n//=2
    return ans[1][0]        
q, m = map(int, input().split())
for i in range(q):
    a = int(sys.stdin.readline())
    print(fib(a, m)%m)