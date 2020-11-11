a,b=input()[::-1].split()
s=''
while a and b:
    s+=str(int(a[0])+int(b[0]))[::-1]
    a,b=a[1:],b[1:]
print((s+a+b)[::-1])
