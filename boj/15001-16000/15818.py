a,b=map(int,input().split())
c=1
for i in map(int,input().split()):
    c*=i%b
print(c%b)
