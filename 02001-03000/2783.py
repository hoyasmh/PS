a,b=map(int, input().split())
l=[a/b]
for i in [0]*int(input()):
    m,n=map(int, input().split())
    l.append(m/n)
print(round(1000*min(l),2))
