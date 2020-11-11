c=[2.2046,0.2642,0.4536,3.7854]
l=['kg','l','lb','g']
for i in range(int(input())):
    a,b=input().split()
    print('%.4f' % round(float(a)*c[l.index(b)],4),l[(l.index(b)+2)%4])
