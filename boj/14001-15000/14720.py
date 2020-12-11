input()
c,n=0,0
for i in (int(i) for i in input().split()):
    if i==c:
        n+=1
        c=(c+1)%3
print(n)
