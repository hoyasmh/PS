n=int(input())
i=121
c=0
while n>0:
    c+=n//((i**3+i**2*3+2*i)//6)
    n=n%((i**3+i**2*3+2*i)//6)
    i-=1
    print(n,i,c)
print(c)

# n=int(input())
# i=150
# c=0
# while i>0:
#     c+=n//((i**3+i**2*3+2*i)//6)
#     n=n%((i**3+i**2*3+2*i)//6)
#     i-=1
# print(c)
