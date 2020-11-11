a,x=int(input()),bin(int(input()))[2:][::-1]
l=[a]
m,n=1,1000000007
for i in range(len(x)):
    l.append(l[-1]**2%n)
    if x[i]=='1':
        m*=l[-2]%n
print(m%n)
