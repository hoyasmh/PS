s=0
t=0
for i in range(int(input())):
    a,b,c=input().split()
    if c!='F':
        s+=int(b)*(69-(ord(c[0]))+.3*('-0+'.index(c[1])-1))
        t+=int(b)
    else:
        t+=int(b)
print(round(s/t+0.000000000001,2))
