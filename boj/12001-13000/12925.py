def mat(la, lb):
    ret = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] = (ret[i][j]+la[i][k]*lb[k][j])%1000
    return ret
def exp(n):
    ret = [[1,0],[0,1]]
    a =[[6,-4],[1,0]]
    while(n):
        if n%2:
            ret = mat(ret,a)
        a = mat(a,a)
        n//=2
    return ret
T=int(input())
for i in range(T):
    n = int(input())
    lst = exp(n)
    b = (6*lst[1][0]+2*lst[1][1])%1000
    a = format(b-1,'03')
    print("Case #{}: {}".format(i+1, a))