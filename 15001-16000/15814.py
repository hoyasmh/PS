s=list(input())
for i in range(int(input())):
    n,m=map(int,input().split())
    s[n],s[m]=s[m],s[n]
print(''.join(s))
