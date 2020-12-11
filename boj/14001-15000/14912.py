a,b=input().split()
c=0
for i in range(1,int(a)+1):
    c+=str(i).count(b)
print(c)
