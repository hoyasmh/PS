a,b=1,0
for i in range(1000000):
    a,b=(a+b)%1000000,a
print(a)
