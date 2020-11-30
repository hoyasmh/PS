n=int(input())
l=list(map(int,input().split()))
if n==1:
    print('B')
elif n==2:
    print(l[0] if l[0]==l[1] else 'A')
else:
    m=l[:3]
    for i in range(n-3):
        print(m)
        p,q=(m[-1]-m[0])*(m[2]-m[1]),m[1]-m[0]
        r=p//q+l[1]
        if r!=l[i+3] or p%q>0:
            print('B')
            exit()
        m.append(r)
    print((l[-1]-l[0])*(l[2]-l[1])//(l[1]-l[0])+l[1])
