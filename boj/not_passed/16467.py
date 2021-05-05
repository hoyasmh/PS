import sys
def mat(a, b):
	ret = [[0,0], [0,0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%100000007
	return ret

def _pow(n):
    ret = 1
    exp = 2
    while n:
        if n % 2:
            ret = ret * exp % 100000007
        exp = exp * exp
        n //= 2
    return ret    
	   
t = int(sys.stdin.readline())
for i in range(t):
    n, b = map(int, sys.stdin.readline().split())
    if n == 0:
        print(_pow(b))
        continue
    n += 1
    l = [[1,1],[1,0]]
    ans = [[1,0],[0,1]]
    while(b):
        if b%2:
            ans = mat(ans, l)
        l = mat(l, l, n)
        b//=2
    print(ans[0][0])