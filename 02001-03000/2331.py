n, k =map(int, input().split())
s=[n]
c=1
while 1:
    n=sum([int(i)**k for i in str(n)])
    if n in s:
        print(s.index(n))
        break
    else:
        s.append(n)
