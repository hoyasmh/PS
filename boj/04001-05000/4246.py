n=int(input())
while n!=0:
    s=input()
    m=len(s)
    l=[s[i*n:i*n+n][::[1,-1][i%2]] for i in range(m//n)]
    for i in range(m):
        print(l[i%(m//n)][i//(m//n)],end='')
    print('')
    n=int(input())
