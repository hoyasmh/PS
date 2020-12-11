a,b=map(int,input().split())
s=1
for i in range(a,b+1):
    s*=(i*i+i)//2%14579
print(s%14579)
