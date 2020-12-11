m,n=map(int,input().split())
s=[]
while m>0:
    if m%n>9:
        s.append(chr(m%n+55))
    else:
        s.append(str(m%n))
    m=m//n
print(''.join(s)[::-1])
