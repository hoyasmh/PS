n,k=map(int,input().split())
c=n
for i in range(n):
    if len(set(input()))>k:
        c-=1
print(c)
    
