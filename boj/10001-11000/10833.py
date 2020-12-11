c=0
for i in [0]*int(input()):
    a,b=map(int, input().split())
    c+=b%a
print(c)
