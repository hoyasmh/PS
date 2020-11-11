n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(a-len(set([int(input()) for j in range(a)])))
