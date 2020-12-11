n=int(input())
l=[1]
i=1
while i<=n:
    k=0
    for j in range(i):
        k+=l[j]*l[i-1-j]
    l.append(k)
    i+=1
print(l[-1])
