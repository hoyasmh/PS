n=int(input())
s=0
for i in range(n):
    a,x=map(int, input().split())
    s+=a*x
print(s)
