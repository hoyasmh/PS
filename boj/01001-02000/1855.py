n=int(input())
s=input()
m=len(s)
l=[s[i*n:i*n+n][::(-1)**(i%2)] for i in range(m//n)]
c=0
for i in range(m):
    print(l[c%(m//n)][c//(m//n)],end='')
    c+=1
