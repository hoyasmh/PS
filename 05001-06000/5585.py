n=1000-int(input())
c=0
l=[500,100,50,10,5,1]
for i in l:
    c+=n//i
    n=n%i
print(c)
