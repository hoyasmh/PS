n=int(input())
l=[1,1,3]
for i in range(30):
    l.append(l[-1]+2*l[-2])
t=l[n//2] if n%2 else l[n//2-1]*3+l[n//2-2]*(n>2)*2
print((l[n]-t)//2+t)