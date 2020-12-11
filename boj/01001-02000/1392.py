m,n=map(int,input().split())
l=[int(input()) for i in range(m)]
for i in range(n):
    b=int(input())
    for j in range(len(l)):
        b=b-l[j]
        if b<0:
            print(j+1)
            break
