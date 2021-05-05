import sys
def mat(a, b, n):
	ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%10000
	return ret   
n = int(input())
while n != -1:
    l = [[1,1],[1,0]]
    ans = [[1,0],[0,1]]
    while(n):
        if n%2:
            ans = mat(ans, l, 2)
        l = mat(l, l, 2)
        n//=2
    print(ans[1][0])
    n = int(sys.stdin.readline())