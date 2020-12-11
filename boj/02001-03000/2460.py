c=[]
d=0
for i in range(10):
    a,b=map(int, input().split())
    d=d-a+b
    c.append(d)
print(max(c))
